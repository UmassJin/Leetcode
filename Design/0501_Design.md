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

