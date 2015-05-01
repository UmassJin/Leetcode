##Table of Content
####[1. Two phase Commit](#two-phase-commit)
####[2. Three phase Commit](#three-phase-commit)
####[3. Paxos](#paxos)

-----------------------------------


##[分布式系统的事务处理](http://coolshell.cn/articles/10910.html)
## [Two phase Commit](http://en.wikipedia.org/wiki/Two-phase_commit_protocol)
#### [Two phase Locking](http://en.wikipedia.org/wiki/Two-phase_locking)

##### Basic Algorithm
##### Commit request phase or voting phase
  1. The coordinator sends a query to commit message to all cohorts and waits until it has received a reply from all cohorts.
  2. The cohorts execute the transaction up to the point where they will be asked to commit. They each write an entry to their undo log and an entry to their redo log.
  3. Each cohort replies with an agreement message (cohort votes Yes to commit), if the cohort's actions succeeded, or an abort message (cohort votes No, not to commit), if the cohort experiences a failure that will make it impossible to commit.

##### Commit phase or Completion phase
##### Success
If the coordinator received an agreement message from all cohorts during the commit-request phase:
  1. The coordinator sends a commit message to all the cohorts.
  2. Each cohort completes the operation, and releases all the locks and resources held during the transaction.
  3. Each cohort sends an acknowledgment to the coordinator.
  4. The coordinator completes the transaction when all acknowledgments have been received.

##### Failure 
If any cohort votes No during the commit-request phase (or the coordinator's timeout expires):
  1. The coordinator sends a rollback message to all the cohorts.
  2. Each cohort undoes the transaction using the undo log, and releases the resources and locks held during the transaction.
  3. Each cohort sends an acknowledgement to the coordinator.
  4. The coordinator undoes the transaction when all acknowledgements have been received.

##### Disadvantage 
The greatest disadvantage of the two-phase commit protocol is that it is a blocking protocol. If the coordinator fails permanently, some cohorts will never resolve their transactions: After a cohort has sent an agreement message to the coordinator, it will block until a commit or rollback is received.


##[Three phase Commit](http://en.wikipedia.org/wiki/Three-phase_commit_protocol)

![Another Pic](https://cloud.githubusercontent.com/assets/9062406/7437312/49905918-f00b-11e4-9862-d3b3b3acd6cb.gif)
#####Coordinator
  1. The coordinator receives a transaction request. If there is a failure at this point, the coordinator aborts the transaction (i.e. upon recovery, it will consider the transaction aborted). Otherwise, the coordinator sends a canCommit? message to the cohorts and moves to the waiting state.
  2. If there is a failure, timeout, or if the coordinator receives a No message in the waiting state, the coordinator aborts the transaction and sends an abort message to all cohorts. Otherwise the coordinator will receive Yes messages from all cohorts within the time window, so it sends preCommit messages to all cohorts and moves to the prepared state.
  3. If the coordinator succeeds in the prepared state, it will move to the commit state. However if the coordinator times out while waiting for an acknowledgement from a cohort, it will abort the transaction. In the case where all acknowledgements are received, the coordinator moves to the commit state as well.
  
#####Cohort
  1. The cohort receives a canCommit? message from the coordinator. If the cohort agrees it sends a Yes message to the coordinator and moves to the prepared state. Otherwise it sends a No message and aborts. If there is a failure, it moves to the abort state.
  2. In the prepared state, if the cohort receives an abort message from the coordinator, fails, or times out waiting for a commit, it aborts. If the cohort receives a preCommit message, it sends an ACK message back and awaits a final commit or abort.
If, after a cohort member receives a preCommit message, the coordinator fails or times out, the cohort member goes forward with the commit.

![Another Pic](https://cloud.githubusercontent.com/assets/9062406/7437416/0539e774-f00c-11e4-87fa-b80260507f38.png)

## Paxos 
##### Introduction
  1. Google的Chubby, Megastore, Spanner都采用Paxos来对数据副本的更新序列达成一致
  

#### Paxos Reference:
##### [Paxos wiki](http://en.wikipedia.org/wiki/Paxos_(computer_science)#Phase_1a:_Prepare)
##### [Fast Paxos](http://research.microsoft.com/pubs/64624/tr-2005-112.pdf)
##### [知乎视频](http://www.zhihu.com/question/19787937)
##### [Paxos 算法形成过程](http://blog.csdn.net/chen77716/article/details/6166675)


#### [ACID concept](http://en.wikipedia.org/wiki/ACID)
ACID (Atomicity, Consistency, Isolation, Durability

####Reference:
分布式系统在互联网时代，尤其是大数据时代到来之后，成为了每个程序员的必备技能之一。分布式系统从上个世纪80年代就开始有了不少出色的研究和论文，我在这里只列举最近15年范围以内我觉得有重大影响意义的15篇论文（15 within 15）。

1. The Google File System: 这是分布式文件系统领域划时代意义的论文，文中的多副本机制、控制流与数据流隔离和追加写模式等概念几乎成为了分布式文件系统领域的标准，其影响之深远通过其5000+的引用就可见一斑了，Apache Hadoop顶顶大名的HDFS就是GFS的模仿之作；

2. MapReduce: Simplified Data Processing on Large Clusters：这篇也是Google的大作，通过Map和Reduce两个操作，大大简化了分布式计算的复杂度，使得任何需要的程序员都可以编写分布式计算程序，其中使用到的技术值得我们好好学习：简约而不简单！Hadoop也根据这篇论文做了一个开源的MapReduce；
3. Bigtable: A Distributed Storage System for Structured Data：Google在NoSQL领域的分布式表格系统，LSM树的最好使用范例，广泛使用到了网页索引存储、YouTube数据管理等业务，Hadoop对应的开源系统叫HBase（我在前公司任职是也开发过一个相应的系统叫BladeCube，性能较HBase有数倍提升）；
4. The Chubby lock service for loosely-coupled distributed systems：Google的分布式锁服务，基于Paxos协议，这篇文章相比于前三篇可能知道的人就少了，但是其对应的开源系统zookeeper几乎是每个后端同学都接触过，其影响力其实不亚于前三篇；
5. Finding a Needle in Haystack: Facebook's Photo Storage：facebook的在线图片存储系统，目前来看是对小文件存储的最好解决方案之一，facebook目前通过该系统存储了超过300PB的数据，一个师兄就在这个团队工作，听过很多有意思的事情（我在前公司的时候开发过一个类似的系统pallas，不仅支持副本，还支持LRC，性能也有较多优化）；
6. Windows Azure Storage: a highly available cloud storage service with strong consistency：windows azure的总体介绍文章，其中通过分层来同时保证可用性和一致性的思路在现实工作中也给了我很多启发；
7. GraphLab: A New Framework for Parallel Machine Learning：CMU基于图计算的分布式机器学习框架，目前已经成立了专门的商业公司，在分布式机器学习上很有两把刷子，其单机版的GraphChi在百万维度的矩阵分解都只需要2~3分钟；
8. Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing：其实就是 Spark，目前这两年最流行的内存计算模式，通过RDD和lineage大大简化了分布式计算框架，通常几行scala代码就可以搞定原来上千行MapReduce代码才能搞定的问题，大有取代MapReduce的趋势；
9. Scaling Distributed Machine Learning with the Parameter Server：百度少帅李沐大作，目前大规模分布式学习各家公司主要都是使用ps，ps具备良好的可扩展性，使得大数据时代的大规模分布式学习成为可能，包括Google的深度学习模型也是通过ps训练实现，是目前最流行的分布式学习框架，豆瓣的开源系统paracell也是ps的一个实现；
10. Dremel: Interactive Analysis of Web-Scale Datasets：Google的大规模（近）实时数据分析系统，号称可以在3秒相应1PB数据的分析请求，内部使用到了查询树来优化分析速度，其开源实现为Drill，在工业界对实时数据分析也是比价有影响力；
11. Pregel: a system for large-scale graph processing: Google的大规模图计算系统，相当长一段时间是Google PageRank的主要计算系统，对开源的影响也很大（包括GraphLab和GraphChi）；
12. Spanner: Google's Globally-Distributed Database：这是第一个全球意义上的分布式数据库，Google的出品。其中介绍了很多一致性方面的设计考虑，简单起见，还采用了GPS和原子钟，20ns保证了事务的时间顺序，同样在分布式系统方面具有很强的借鉴意义；
13. Dynamo: Amazon’s Highly Available Key-value Store：Amazon的分布式NoSQL数据库，意义相当于BigTable对于Google，于BigTable不同的是，Dynamo保证CAP中的AP，C通过vector clock做弱保证，对应的开源系统为cassandra；
14. S4: Distributed Stream Computing Platform：Yahoo出品的流式计算系统，目前最流行的两大流式计算系统之一（另一个是storm），Yahoo的主要广告计算平台；
15. Storm @Twitter：这个系统不多说，开启了流式计算的新纪元，几乎是所有公司流式计算的首选，绝对值得关注；



