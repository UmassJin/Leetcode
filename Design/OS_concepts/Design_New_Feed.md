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


• Pull: high latency
• Push: news delay
• Push wins.

