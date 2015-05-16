#### What are interviewers thinking about?
##### What do interviewers usually expect from system design questions?
* A working solution with a few lines of code. (not just discussion)
* Don’t need to be compilable. Just express idea through argument/return/functionality.
* Your logic and understanding of knowledge (not just knowledge)
* Good communication skill. (general background -> specific)

#### Design and implement Twitter.
* see the tweets of people you follow.
* follow/unfollow people
* post a tweet.
* comments on a tweet.

#### Level 1
##### Database design
* user
* comment

| UserId | Name | Age | 
|:---:|:---:|:---:|
| 1 | Jason | 25 | 
| 2 | Michael | 26 |

* News

| NewsId | AuthorId | Content | Time |
|:---:|:---:|:---:|:--:|
| 1 | 2 | “hehe” | 20150228 | 
| 2 | 1 | “haha” | 20150227 |

* Friend 

| FriendId | FollowerId | FollowId |
|:---:|:---:|:---:|
| 1 | 1 | 2 |
| 2 | 2 | 1 |

##### Database operation
* 1. get follow list
    * SELECT FollowId FROM friend
    * WHERE FollowerID = myid
* 2. get friend’s news
    * SELECT * FROM news
    * WHERE Time > xxx
    * AND Author IN friendlist

##### Problem:
* Repeatedly query follow list?
      1. Store each user’s follow as a list, create a new table which store the user's follows 
      2. Tip: save repeating computations, trade space for latency.
* It’s costly to check every news’ author id if it is in the friend list
      1. Store each user’s news id as a list.
      2. Extend the user table, add one more column which for each user's news. 

##### Level 2:
* Querying every follow’s news list is still slow.
      * How about storing my own list of follows’ news as well, and get updated when they post?
      * Tip: we can do some offline computations, for online latency.
* This is the choice of Pull and Push.
• Latency:
   
| | Refresh (read) (user-facing latency) | Post (write) |
|:---:|:---:|:---:|
| Pull | follows’ lists | my own list |
| Push | my own list | followers’ lists |

      * Pull: Refresh: read all my follow's news; Pose: write in my table
      * Push: Post: 每一次写都更新我的follower's list, Read: read my own list 
      * 类比: push 就像印好了报纸，然后一个一个送报纸到门口；pull 就像印好了报纸，放在门口，想看自己拿
   
• Pull: high latency, high user-facing latency 
      * Facebook post state用pull来完成，用很大的cache，不从data base拿，从内存拿，快很多
      * 一般情况下，名人的用pull，非名人的用push
      
• Push: news delay, 
• Push wins, 减少user-facing latency 

##### Level 3:
* A problem of Push (and solution), taking heterogenous popularity into account.
      * (usually everyone’s follow number doesn’t vary too much, but followers number varies a lot)
      * Celebrities (huge followers)
         * Push will be too slow (update every follower’s news list). at the same time, people is less tolerant to celebrities’ news delay. => use pull. (just a few celebrities, so latency is okay.)
* => Pull + Push hybrid solution
      * For celebrities’ post, don’t push.
      * When refresh, query celebrities’ news list and merge with my own news list.

##### Level 4:
* An improvement for Push, taking heterogeneous user activity into account.
      * Some users are more addictive than others.
         * How about push to them with higher priority, and let less frequent users pull. (reduce network traffic costed by useless push => reduce the delay of useful pushes.)
         
