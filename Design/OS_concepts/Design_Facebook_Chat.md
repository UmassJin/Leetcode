* Real Time
    * Facebook choose a technique whereby the client pulls updates from the server, similar to 
     [Comet's XHR Long Polling](https://en.wikipedia.org/wiki/Comet_(programming)#XHR_long_polling) Process
    * The method we chose to get text from one user to another involves loading an iframe on each Facebook page, and 
    having that iframe's Javascript make an HTTP GET request over a persistent connection that doesn't return until 
    the server has data for the client. 

* Client Side
   * Regular AJAX for sending messages
   * Regular AJAX for pull list of friends
   * AJAX Long Polling for message
* Server Side
   * Communication between service: Thrift
   * Channel - Erlang - Message queuing and delivery
      * Queue message in each user's channel
      * Deliverer message as long-polling HTTP request
   * Presence - aggregation of online info in memory
   * Chat logger - store conversation at server side
   * Web tier
* 过程
  * Browser -> Web Tier -> Channel -> Browser (发信收信)
  * 1-ajax -> 2-thrift -> 3->long poll
  * Web Tier -> via thrift <- Chat logger
  * Presence和Channel talk(via thrift) 用来获得在线列表
    

* Reference 
* https://github.com/UmassJin/Python-Study/blob/master/img/Facebook_Chat.pdf
* http://www.cnblogs.com/piaoger/archive/2012/08/19/2646530.html
* https://www.facebook.com/note.php?note_id=14218138919
* http://www.infoq.com/news/2008/05/facebookchatarchitecture
