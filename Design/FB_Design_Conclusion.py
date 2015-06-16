'''
[转载]
这里原帖地址: http://blog.csdn.net/sigh1988/article/details/9790337
以下为转载内容
===========================我是分割线==================
稍微总结一下

1. 入门级的news feed
http://www.quora.com/What-are-best-practices-for-building-somet
http://www.infoq.com/presentations/Scale-at-Facebook
http://www.infoq.com/presentations/Facebook-Software-Stack
一般的followup question是估算需要多少server
另外这个帖子有讨论
http://www.mitbbs.ca/article_t/JobHunting/32463885.html
这篇文章稍微提到要怎么approach这种题，可以稍微看看
http://book.douban.com/reading/23757677/


2. facebook chat,这个也算是挺常问的
http://www.erlang-factory.com/upload/presentations/31/EugeneLet
https://www.facebook.com/note.php?note_id=14218138919
http://www.cnblogs.com/piaoger/archive/2012/08/19/2646530.html
http://essay.utwente.nl/59204/1/scriptie_J_Schipers.pdf

3. typeahead search/search suggestion，这个也常见
https://www.facebook.com/video/video.php?v=432864835468
问题在这个帖子里被讨论到，基本上每个问题，在视频里都有回答
http://www.mitbbs.com/article_t/JobHunting/32438927.html


4. Facebook Messaging System(有提到inbox search, which has been asked before）
messaging system就是一个把所有chat/sms/email之类的都结合起来的一个系统
    * http://www.infoq.com/presentations/HBase-at-Facebook
    * http://sites.computer.org/debull/A12june/facebook.pdf
    * http://www.slideshare.net/brizzzdotcom/facebook-messages-hbase/
    * https://www.youtube.com/watch?v=UaGINWPK068


5. 任给一个手机的位置信号(经纬度)，需要返回附近5mile 的POI
这个这里有讨论，这题貌似nyc很爱考...
http://www.mitbbs.ca/article0/JobHunting/32476139_0.html


6. Implement second/minute/hour/day counters
这题真不觉得是system design，但万一问道，还是要有准备，貌似在总部面试会被问
道....
这个帖子有讨论
http://www.mitbbs.com/article_t/JobHunting/32458451.html


7. facebook photo storage，这个不太会被问起，但是知道也不错
https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf
https://www.facebook.com/note.php?note_id=76191543919


8. facebook timeline,这个也不太是个考题，看看就行了
https://www.facebook.com/note.php?note_id=10150468255628920
http://highscalability.com/blog/2012/1/23/facebook-timeline-bro


除了这些，准备一下这些题目
implement memcache
http://www.adayinthelifeof.nl/2011/02/06/memcache-internals/

implement tinyurl（以及distribute across multiple servers)
http://stackoverflow.com/questions/742013/how-to-code-a-url-sho

determine trending topics(twitter)
http://www.americanscientist.org/issues/pub/the-britney-spears-
http://www.michael-noll.com/blog/2013/01/18/implementing-real-t

copy one file to multiple servers
http://vimeo.com/11280885

稍微知道一下dynamo key value store，以及google的gfs和big table


另外推荐一些网站
http://highscalability.com/blog/category/facebook
这个high scalability上有很多讲system design的东西，不光是facebook的，没空的
话，就光看你要面试的那家就好了..
facebook engineering blog
http://www.quora.com/Facebook-Engineering/What-is-Facebooks-arc
http://stackoverflow.com/questions/3533948/facebook-architectur

其他家的
http://www.quora.com/What-are-the-top-startup-engineering-blogs


==================================================================
在说说怎么准备这样的面试
首先如果你连availability/scalability/consistency/partition之类的都不是太有概
念的话，我建议先去wikipedia或者找一个某个大学讲这门课的网站稍微看一下，别一
点都不知道
这个链接也不错
http://www.aosabook.org/en/distsys.html

如果你这些基本的东西都还知道，那么我觉得你就和大部分毫无实际经验的人差不多一
个水平...
能做的就是一点一点去准备，如果你还有充足的时间的话，建议从你面试的那家公司的
engineering blog看起，把人家用的technology stack/product都搞清楚，然后在把能
找到的面试题都做一遍呗....我们做coding题说白了不也是题海战术...而且你如果坚
持看下去，真的会看出心得，你会发现很多地方都有相同之处，看多了就也能照葫芦画
瓢了...

再有就是面试的时候应该怎么去approach这种题，我说说我的做法
1. product spec/usage scenario 和面试者confirm这个东西到底是做什么的
可以先列出来几个major functionality，然后有时间的话，再补充一些不重要的
把你想的都写下来

2. define some major components
就是画几个圈圈框框的，每个发表一番您的高见....然后讲他们之间怎么interact

以上是question specific的东西，
这个讲完了，我们可以讲一些每道题都是用的，比如说
怎么scale/怎么partition/怎么实现consistency，这些东西，可以套用到任何题上



当然了，我们遇到的题和解题的方法可能都有些出入，不见得每道题有一个路数下来，
最重要的是，讲题的时候要有条理，画图要清楚，保持和面试官的交流，随时问一下人
家的意见。

我能想到的就这么多，欢迎大家交流，希望大家都能找到理想的工作.

'''

'''

2) design
解这种题是个*交流*的过程，或者说是给出方案然后获取反馈的不断循环的过程。
一般的流程：
首先你要问清楚requirement；
然后可以讲一下high level architecture，就是分成哪几个component，互相之间如果
interact，在白板上画一画；
之后面试官可能会让你深入某个component detail讨论；
也有可能变换requirement让你重新设计

另外，f家还喜欢让你估算机器之类的，做一些back-of-envelopme calculation。所以
最好对一些计算机相关的基本常数，fb的用户量等等有个大概的了解。

准备的时候建议看看fb的design高频题。一方面有可能面试的时候刚好碰到这几个
topic，另一方面其实很多design都是相通的。
之前有个帖子讲这个，原帖已经被删了，这儿有个备份http://blog.csdn.net/sigh1988/article/details/9790337

另外补充一点我收集的材料

a) 首先你可以从整体上了解一下facebook的architecture
http://www.quora.com/Facebook-Engineering/What-is-Facebooks-arc
http://www.ece.lsu.edu/hpca-18/files/HPCA2012_Facebook_Keynote.
http://www.quora.com/Facebook-Engineering/What-have-been-Facebo
除了下面给出的一些资料，fb engineering page里还有很多不错的内容
https://www.facebook.com/Engineering

b) news feed
这里有个talk
http://www.infoq.com/presentations/Facebook-News-Feed
对应的slides
http://readme.skplanet.com/wp-content/uploads/2012/11/0-3_Faceb
还有一些quora上的讨论
http://www.quora.com/Activity-Streams/What-are-the-scaling-issu
http://www.quora.com/What-are-best-practices-for-building-somet
http://www.quora.com/What-is-the-best-storage-solution-for-buil

c) facebook chat
这里有两个notes，其中第二个里面还有相应的tech talk links
https://www.facebook.com/notes/facebook-engineering/facebook-chat/
14218138919
https://www.facebook.com/notes/facebook-engineering/chat-stability-and-
scalability/51412338919

d) typeahead search & graph search
关于typeahead search的tech talk和notes
https://www.facebook.com/video/video.php?v=432864835468
https://www.facebook.com/note.php?note_id=365915113919
https://www.facebook.com/note.php?note_id=389105248919

关于graph search的paper, tech talk, notes。其中paper很值得一看。
http://db.disi.unitn.eu/pages/VLDBProgram/pdf/industry/p871-cur
https://newsroom.fb.com/Photos-and-B-Roll/4362/Graph-Search-Whiteboard
https://www.facebook.com/note.php?note_id=10151240856103920
https://www.facebook.com/note.php?note_id=10151347573598920
https://www.facebook.com/note.php?note_id=10151361720763920
https://www.facebook.com/note.php?note_id=10151432733048920
https://www.facebook.com/note.php?note_id=10151755593228920

e) facebook messages
两个tech talks
http://www.youtube.com/watch?v=XAuwAHWpzPc
http://www.infoq.com/presentations/HBase-at-Facebook
以及eng notes
https://www.facebook.com/note.php?note_id=10150148835363920
https://www.facebook.com/note.php?note_id=10150162742108920

f) photo storage
相关的papers和notes
https://www.usenix.org/conference/osdi10/finding-needle-haystack-facebooks-
photo-storage
https://www.usenix.org/legacy/events/osdi10/tech/full_papers/Beaver.pdf
https://www.usenix.org/legacy/events/osdi10/tech/slides/beaver.pdf
https://www.facebook.com/note.php?note_id=76191543919

g) social graph data store
相关的note, video, paper
https://www.facebook.com/notes/facebook-engineering/tao-the-power-of-the-
graph/10151525983993920
https://www.usenix.org/conference/atc13/technical-sessions/presentation/
bronson
http://www.cs.cmu.edu/~pavlo/courses/fall2013/static/papers/117

h) tiny URL
这里有一些讨论
http://n00tc0d3r.blogspot.com/2013/09/big-data-tinyurl.html
http://stackoverflow.com/questions/742013/how-to-code-a-url-sho
http://stackoverflow.com/questions/3376163/what-are-the-things-

i) POI
参考这里
http://www.slideshare.net/mmalone/scaling-gis-data-in-nonrelati
http://www.mitbbs.ca/article_t/JobHunting/32476139.html

'''
