### Functionality 
* News Feed is the constantly updating list of stories in the middle of your home page. 
News Feed includes status updates, photos, videos, links, app activity and likes from people, 
Pages and groups that you follow on Facebook

#### Goal
* The goal of News Feed is to deliver the right content to the right people 
at the right time so they don’t miss the stories that are important to them.

#### Challenge
* The ranking of the news
    * Every users may have around 1500 news feed, how to ranking them and highlight the most important ?
* highight the major updates to news feed 
* How will you save those pictures in the cache?
* How the machine will sync up each other ? 

#### How we decide the news feed algorithm 
The News Feed algorithm responds to signals from you, including, for example:
* How often you interact with the friend, Page, or public figure (like an actor or journalist) who posted
* The number of likes, shares and comments a post receives from the world at large and from your friends in particular
* How much you have interacted with this type of post in the past
* Whether or not you and other people across Facebook are hiding or reporting a given post

#### How could we test whether it works better or not ?
* In a recent test with a small number of users, this change resulted in a 5% increase in the number of likes, 
comments and shares on the organic stories people saw from friends and an 8% increase in likes, comments and 
shares on the organic stories they saw from Pages
* Previously, people read 57% of the stories in their News Feeds, on average. They did not scroll far enough to 
see the other 43%. When the unread stories were resurfaced, the fraction of stories read increased to 70%


### Design 

#### Detime the importance, more about "EdgeRank"
##### Factor 
* Basic Factor:
      * Affinity — i.e., how close is the relationship between the user and the content/source?
         * personal interactions
         * global interactions 
      * Weight — i.e., what type of action was taken on the content?
      * Decay — i.e., how recent/current is the content?
* [More Factor: (the latest one)](http://marketingland.com/edgerank-is-dead-facebooks-news-feed-algorithm-now-has-close-to-100k-weight-factors-55908)
      * relationship setting
      * post types -  i.e. Users that often interact with photo posts are more likely to see more photo posts in the News Feed
      * Hide Post / Spam Reporting
      * Clicking On Ads, Viewing Other Timelines

##### Other two factors: Story Bumping and Last Actor 
* With Story Bumping, Facebook doesn’t just look at what stories have been published since you last looked at the feed, but at all the recent stories you hadn’t seen — not just “new” but “new to you”. This way you see more relevant stories, even if they’re a little bit older.
* “Last Actor” looks at the 50 people you most recently interacted on Facebook such as viewing someone’s profile or photos, and liking their feed stories. Facebook then shows you more of them in your feed in the short-term. Say you browse through 100 photos of a girl you have a crush on, you’ll see more of her in your feed later that day. Note that this doesn’t mean anyone knows about your private Facebook browsing habits. This feature only affects what you see. The Last Actor algorithm change has been rolled out and is now impacting the web and mobile News Feed.

##### [NoSQL vs Relational SQL](https://github.com/UmassJin/Leetcode/blob/master/Design/OS_concepts/System_Design_OS_Basic.md#relational-sql-vs-nonesql)

##### Some static number
* 1.44 billion active user per month
* 1.25 billion mobile user per month
* 936 million daily active user per day (远大于Monthly因为monthly的active user不能重复计算)
* 798 million mobile daily active users on average for March 2015
* 18 million pages(2013)
* Facebook says that the typical user has about 1,500 stories that could show in the News Feed on every visit

#### Pull and Push


#### Reference
* http://www.quora.com/What-are-the-scaling-issues-to-keep-in-mind-while-developing-a-social-network-feed
* http://www.quora.com/Software-Engineering-Best-Practices/What-are-best-practices-for-building-something-like-a-News-Feed
