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
1) What if there are multiple threads asking for requests?
    * Race condition => Serialization by critical section => Implement using lock or simply add “synchronized” keyword in java.
    
2) What if requests are coming from different users, and we want limit per-user qps?
    * 每个user分别记录
    
3) This throttler can be installed on either front-end/backend server.
    * You can distribute QPS quota for different front-end/backend setups.
    
4）Your throttler is too rigid, how do you allow some variance?
    * You can look back more than 1 timestamp.
    * i.e. use a circular buffer of 2 timestamps, and guarantee 0.2s between current timestamp and the last timestamp in buffer. This way, we allow: 0.1s, 0.1001s, 0.3s, 0.3001s, but don’t allow: 0.1s, 0.1001s, 0.1002s, 0.4s.

