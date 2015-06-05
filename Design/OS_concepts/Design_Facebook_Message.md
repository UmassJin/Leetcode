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

##### c) HBase Advantage 
* High write throughput 
* Horizontal scalability 
* Automatic Failover 
* Benefits of HDFSs

##### d) HDFS Advantage 
* Fault rolerance
* Scalability 
* Checksums (automatically check the wrong data )
* Map Reduce 

##### 4. HBase-HDFS Architecture Overview 
![pic](https://cloud.githubusercontent.com/assets/9062406/7948193/f73b83f0-0936-11e5-8b75-f512cc4f091f.png)

##### 5. How it works in msg systems 
* Each user will sticky to the Cell (Application Server and HBase/HDFS/ZK)
* Cell is the independent failure domain
* User Directory Service: a server which cell does the this user living 

* 1. User gets message, Clients will look at the User Directory Service to find which cell the user belong to 

![pic](https://cloud.githubusercontent.com/assets/9062406/7948338/0193aa70-0938-11e5-9202-50d0fc885436.png)

* 2. Then the Clients will find the exact the Application Server if can find it or will send to random Application Server then forward to the correct AS 

![pic](https://cloud.githubusercontent.com/assets/9062406/7948346/120ef9a4-0938-11e5-8da8-fd231df8854a.png)

* 3. If the msg contains attachment, the AS will talk to the Haystack, strip and add attachments 

![pic](https://cloud.githubusercontent.com/assets/9062406/7948357/25d7b8cc-0938-11e5-92f8-dda309123e36.png)

* 4. And then add into the HBase with msgs and search index 

![pic](https://cloud.githubusercontent.com/assets/9062406/7948363/2fc90dfe-0938-11e5-9249-a83108e9445e.png)

##### 6. Multiple Cells 
* Limits failure domain 
* Different versions of HDFS and Cells

##### 7. Typical Cell Layout
* 5 or more racks per cell 
* 20 servers/rack 
* the top server is the master and for the other 19 server are slaves, it has the HBase process: Region Server; HDFS process: Data node, and Map-Reduce process: Task Tracker 

* ![pic](https://cloud.githubusercontent.com/assets/9062406/7948583/f5c8bbfc-0939-11e5-96d9-2bda7c0ed860.png)

##### 8. Separate backup system 
* uses scribe 
* double logging to reduce loss
* merge and de-dup system
* ability to restore data 
* keep testing it often 
* replication + backups 

##### 9. HBase and HDFS enhancement 
* HBase Master re-write to allow failover 
* Block placement policy to restrict data loss
* Lots and lots of monitoring 
    * remove bad machines automatically 

##### 10. HBase Rolling Upgrades
* Upgrade and restart primary master, secondary takes over
* Upgrade and restart secondary master, secondary upgradeed 
* restart 10% of region servers at a time 

##### 11. Messages Migration 
Check the following video 

* Reference: [Karthik Ranganathan Hadoop Summit 2011 Facebook Messages Infrastructure with Q&A](https://www.youtube.com/watch?v=XAuwAHWpzPc&feature=iv&src_vid=UaGINWPK068&annotation_id=annotation_65559)
* [paper about HBase](http://sites.computer.org/debull/A12june/facebook.pdf)
* [HBase wiki](http://en.wikipedia.org/wiki/Apache_HBase)
* [HBase at Facebook](http://www.infoq.com/presentations/HBase-at-Facebook)

