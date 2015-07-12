* Build a failure detecter 
    * the failure we handle here is the crash-stop/fail-stop process failures, this essentially means the once member of 
    the group/process, it will never recoverd and take any actions, stop excuted any instructions 
    * Membership protocol
        * Failure dector
        * Dissemination 

![pic](https://cloud.githubusercontent.com/assets/9062406/8636373/92b3dbc6-2812-11e5-96e0-fae60b13cfe2.png)

* Failure dectors 
    * Properties
        * Completeness: each failure is detected
        * Accuracy = there is no mistaken detection 
        * Impossible together in lossy networks to achieve the above two goals, if so, they can solve consensus
  
! [pic](https://cloud.githubusercontent.com/assets/9062406/8636396/d39aba8c-2813-11e5-94db-a432c36b2330.png)

* Centralized Heartbeating (Bad)
    * problem: pj maybe hotsopt and if pj failure, it's loose dectors
    ![pic](https://cloud.githubusercontent.com/assets/9062406/8636411/6876ec7a-2814-11e5-8334-c3c179910d04.png)
    
* Ring Heartbeating (Bad)
    * problem: if pi's neighbors are all failure, then pi failure, no one could detect that 
    ![pic](https://cloud.githubusercontent.com/assets/9062406/8636413/74ba4428-2814-11e5-8bc4-214217b1297b.png)

* All-to-All heartbeating (Better)
    * equal load member
    * problem:if you has one pj is slow and is receiving packets at longer delay than others, it may end up
    marking all the other processes as filure, faluse postive 
    ![pic](https://cloud.githubusercontent.com/assets/9062406/8636428/2273a618-2815-11e5-8153-8cfd5c518561.png)

* Gossip Style Filure detection 

