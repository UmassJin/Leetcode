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
http://www.infoq.com/presentations/HBase-at-Facebook
http://sites.computer.org/debull/A12june/facebook.pdf
http://www.slideshare.net/brizzzdotcom/facebook-messages-hbase/
https://www.youtube.com/watch?v=UaGINWPK068


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
