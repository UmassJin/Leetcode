* Consideration 
    * First, it has to have a good crawling strategy, i.e., a strategy for deciding which pages to download next. 
    * Second, it needs to have a highly optimized system architecture that can download a large number of pages per second while
being robust against crashes, manageable, and considerate of resources and web servers.

* Crawling Applications Requirement
    * Breadth-First Crawler
      * In reality, the web pages are often not traversed in a strict breadth-first fashion, but using a variety of policies, e.g., for pruning crawls inside a web site, 
      or for crawling more important pages first1.
    * Recrawling Pages for Updates
    * Focused Crawling
      * More specialized search engines may use crawling policies that attempt to focus only on certain types of pages
    * Random Walking and Sampling
    * Crawling the “Hidden Web”

* Simple stratigy
    * crawling application
      * The crawling application decides what page to request next given the current state and the previously crawled pages, 
      and issues a stream of requests (URLs) to the crawling system.
    *  crawling system
      * The crawling system (eventually) downloads the requested pages and supplies them to the crawling application 
      for analysis and storage.
      * The crawling system is in charge of tasks such as robot exclusion, speed control, and DNS resolution
    ![pic](https://cloud.githubusercontent.com/assets/9062406/8274175/988b7f36-1840-11e5-9ed6-ae5ba429e872.png)
    
    
* Requirement
    * Flexity
    * Low Cost and High Performance:
    * Robustness
    * Etiquette and Speed Control
    * Manageability and Reconfigurability
  
* Different Component details(paper)
![pic](https://cloud.githubusercontent.com/assets/9062406/8274179/b0a0f9b6-1840-11e5-83c0-caa9f5978cbd.png)
  
  
