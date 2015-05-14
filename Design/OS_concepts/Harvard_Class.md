### [System Design example: shorten URL](http://www.hiredintech.com/system-design/the-system-design-process/)
#### 1. Use Cases
1. Shortening: take a URL => return a much shorter URL
2. Redirection: take a short URL => redirect to the original URL 
3. Custom URL
4. High availability of the system 

  Our of scope 
   4. Analytics
   5. Automatic link expiration
   6. Manural link removal 
   7. UI vs API 

#### 2. Constraints
1. Amount of the traffic the system should handle 
2. Amount of the data the system should work with

  Should ask the following questions: 
   1. How many requests per sec should be handle ?
   2. How many new URLs each sec should be handle ?

* 15 Billion new tweets
* All shortened URLs per month: 1.5BN
* We: 100 Million URLs each month 

Math:
1. New URLs per month: 100 Million (shortening requests)
2. 1 Billion requests per month 
3. 10% from shortening and 90% from redirection 
4. Requests per second: 400+ requests per sec (40 shortens, 360: redirects)
5. Total URLs: 5 years x 12 months x 100 mins = 6 billion URLs in 5 years
6. 500 bytes per URL, URL is case sensitive !
7. 6 bytes per hash 
8. 3 TBs for all urls, 36 GB for all hashes (over 5 years)
9. New data written per second: 40 * (500+6): 20K
10. Data read per second: 360 * 506 bytes: 180 K

* All shortened URLs per Month: 1.5 Billion 
* Sites below the top3: 300 M per month 

#### static numbers:
##### [Facebook](http://newsroom.fb.com/company-info/)
* 1.44 billion monthly active users as of March 31, 2015
* 1.25 billion mobile monthly active users as of March 31, 2015

##### [Twitter](https://about.twitter.com/company)
* 302 million monthly active users
* 500 million Tweets are sent per day
 
#### 3. Abstract Design
##### 1. Application service layer (serves the requests)
* Shortening service: 
    a) Generate the hash, checking if it is in the database, if already used, will keep generating until one unused is find
    b) For the customer URL, check if it is in the data store
* Rediction service 

##### 2. Data storage layer (keeps track of the hash => URL mapping)

* Acts like a big hash table: stores new mappings, and retrieves a value given a key.
  1) hashed_url = convert_to_base_62(md5(original_url + random_salt))[:6]
  2) Base 62 是一种short ulr的encoding, encode之后只有62种字符0-9 a-z A-Z
  3) The MD5 message-digest algorithm is a widely used cryptographic hash function producing a 128-bit (16-byte) hash value, typically expressed in text format as a 32 digit hexadecimal number.  

##### 3. Understanding Bottlenecks
  1) Traffic - not going to be very hard
  2) Lots of data - more interesting
  

#### 4. Scaling your abstract design 
