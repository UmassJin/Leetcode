### Design Rate Limiter
#### Your service can only support requests up to a set rate (e.g. 1 qps~1000000 qps). How would you do that?

##### 1. Clarification:
* 1) If you determine that a request cannot be handled, is it okay to drop it?
    * Yes, we are asking for rate-limiter, not rate-smoother or rateshaper
* 2) Over what period should the rate be assessed? 1s? 1ms?
    * Excellent question! And it does matter. You already see that in our attempt, the “period” should also be a parameter.
     
##### 2. Interface:
* void setLimit(double qps) // Could we use int ? 支持整数，不支持double
* bool allowRequest()

##### 3. Initial Thought 
* 10 qps limit: we don’t want more than 10 requests per second.
   1. Looks like a limited “resource”, producer-consumer model!
   2. Maintain a counter, initialized to 10, and restore (produce) to 10 every second.
   3. allowRequest() will decrement the counter (consume) and return true if counter is larger than 0, or return false otherwise.

* Problem:
    1. What if our incoming qps is 1000?
    2. we will allow first 10, and deny later 990.
    3. our qps will be 1000 for 0.01s, and 0 for 0.99s.
    
##### 4. Further Thought 
* Use the timestamp: 
* In order to allow/reject current request, you only need the timestamp of the last allowed request!
* Just guarantee 0.1s between requests.
* Check this solution:
    1. If 0.1s gap is guaranteed, rate cannot exceed 10 qps; (sufficient solution)
    2. If 0.1s gap is not guaranteed, rate will exceed 10 qps. (necessary solution)

```c++
long long last_timestamp = now();
bool allowRequest() {
    // we need an accurate enough timer 
    long long cur_timestamp = now();
    if (cur_timestamp - last_timestamp >= 1 / QPS) {
            last_timestamp = cur_timestamp;
            return true;
    }
    return false;
} 
```

##### 5. Followup Question
* 1) What if there are multiple threads asking for requests?
    * Race condition => Serialization by critical section => Implement using lock or simply add “synchronized” keyword in java.
    
* 2) What if requests are coming from different users, and we want limit per-user qps?
    * 每个user分别记录
    
* 3) This throttler can be installed on either front-end/backend server.
    * You can distribute QPS quota for different front-end/backend setups.
    
* 4）Your throttler is too rigid, how do you allow some variance?
    * You can look back more than 1 timestamp.
    * i.e. use a circular buffer of 2 timestamps, and guarantee 0.2s between current timestamp and the last timestamp in buffer. This way, we allow: 0.1s, 0.1001s, 0.3s, 0.3001s, but don’t allow: 0.1s, 0.1001s, 0.1002s, 0.4s.

* 5)  Any-1-sec problem 
We just don’t want more than 10 queries in any second. (but allow instantaneous QPS > 10, e.g. allow more than 1 query in 0.1s, etc), e.g: ```0.00, 0.01, 0.02, 0.03, …, 0.09, 1.00, 1.01 … ```all allowed. ```0.90, 0.91, 0.92, 0.93, …, 0.99, 1.00, 1.01 …1.00 and 1.01 ```should be rejected.
    * Use a 10-length circular buffer to record the most recently allowed 10 requests’ timestamp.
    * For every incoming request: if (now() - oldest_timestamp >= 1s) => allow.
    * e.g. in circular buffer: 0.03, 0.12, 0.15, 0.34, …, 0.56. We should only allow next request to come at 0.03 + 1 or later, since otherwise, there will be 11 requests between 0.03 and 0.03 + 1

* 6) Discussion
    * Given 1000 QPS limit.
    * Problem statement A: no more than 1000 requests in every wall-clock second. (restoring counter solution)
         * Maybe more than 1000 requests in certain 1-sec.
    * Problem statement B: 1-sec period: no more than 1000 requests in any 1 sec. (1000-length buffer solution)
         * maybe more than 100 requests in 0.1 sec.
         * guaranteed no more than 10,000 request in any 10 sec.
            * In fact guaranteed at all levels higher than 1 sec.
    * Problem statement B’: 0.1-sec period: no more than 100 request in any 0.1 sec (100-length buffer)
         * maybe more than 10 requests in 0.01 sec.
         * guaranteed no more than 1000 request in any 1 sec.
            * In face guaranteed at all levels higher than 0.1 sec.
    * …
    * Problem statement C: 1/QPS-sec period: no more than 1 request in any 1/QPS sec (our precise solution)
         * guaranteed at any level.
    * Problem A 是说在任意一个整数时间内，例如1s到2s, 2s到3s, 不要超过1000个request，但是有可能1.3s到2.3s超过了1000个request
    * Problem B, B', C是保证在任意一个1s内，不超过1000 requests，所以用length buffer solution记录每一个request的timestamp，如果有第1001个request，比较timestamp。这个算法保证了任意一个1s内，只有1000个request，但是不能保证任意一个0.1s内有100 requests，同样的, 0.1sec不能保证0.01s内的数量。所以我们可以用1/QPS sec来保证no more than 1 request.
    
##### 6. Scalability Issue (100kQPS?)
* Problem: huge memory consumption. (For ease of thinking, let’s use 1000 QPS.)
* Solution: still use a 10-length circular buffer, each element store the
timestamp of the 1st, 101st, 201st, 301st, 901st… allowed request.
    * The 1001st request should come 1s after the 1st request.
    * For the 1002nd request, should it come 1s after the 1st or the 101st (we don’t know when the 2nd request comes)?
       * 1s after the 101st (conservative), effectively limiting to 900~1000 QPS.   
       * 1s after the 1st, effectively limiting to 1000~1100 QPS.

##### 7. Cost-per-second
* What if each request takes various “permits”, and you want to limit total permits issued per second?
