##### Facebook Messages Infrastructure 
* Combine the different channels Messages, Charts, Emails, SMS into one 

##### 1. Size
* 15B messages * 1024 bytes = 14TB per month 
* 120B chat * 100 bytes = 11TB
* size now: 300 TB / month, compressed and unreplicated size 

##### 2. Open Source Stack
* Memcached ---> App Server Cache
* ZooKeeper ---> Small Data Coordination Service 
* HBase  ---> Database Storage Engine
* HDFS  ---> Distributed File System
* Hadoop ---> Asynchronous Map-Reduce Jobs

##### 3. Two main storage database 
###### a) HBase (small/medium sized data)
* message metadata and indices 
* Search index
* Small Message bodies

##### b) Haystack (large msgs)
* Attachments 
* Large messages 
* used for facebook existing photo/video store

##### HBase Advantage 
* High write throughput 
* Horizontal scalability 
* Automatic Failover 
* Benefits of HDFSs

##### HDFS Advantage 
* Fault rolerance
* Scalability 
* Checksums (automatically check the wrong data )
* Map Reduce 

##### HBase-HDFS Architecture Overview 





