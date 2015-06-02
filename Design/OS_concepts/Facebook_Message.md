##### Facebook Messages Infrastructure 
* Combine the different channels Messages, Charts, Emails, SMS into one 

##### Size
* 15B messages * 1024 bytes = 14TB per month 
* 120B chat * 100 bytes = 11TB
* size now: 300 TB / month, compressed and unreplicated size 

##### Open Source Stack
* Memcached ---> App Server Cache
* ZooKeeper ---> Small Data Coordination Service 
* HBase  ---> Database Storage Engine
* HDFS  ---> Distributed File System
* Hadoop ---> Asynchronous Map-Reduce Jobs

##### Two main storage database 
###### HBase (small/medium sized data)
* message metadata and indices 
* Search index
* Small Message bodies

##### Haystack (large msgs)
* Attachments 
* Large messages 
* used for facebook existing photo/video store



