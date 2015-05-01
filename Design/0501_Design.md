###[分布式系统的事务处理](http://coolshell.cn/articles/10910.html)
#### [Two phase Commit](http://en.wikipedia.org/wiki/Two-phase_commit_protocol)

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


#### [Three phase Commit](http://en.wikipedia.org/wiki/Three-phase_commit_protocol)

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


#### Paxos 
##### [Fast Paxos](http://research.microsoft.com/pubs/64624/tr-2005-112.pdf)
##### [知乎视频](http://www.zhihu.com/question/19787937)


#### 
