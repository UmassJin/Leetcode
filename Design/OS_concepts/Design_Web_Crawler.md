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
    * Flexibility
    * Low Cost and High Performance:
    * Robustness
         * it has to tolerate bad HTML, strange server behavior and configurations, and many other odd issues. The system needs to be able to tolerate crashes and network interruptions without losing (too much of) the data.
    * Etiquette and Speed Control
    * Manageability and Reconfigurability
  
* Different Component details(paper)
      * Crawl Manager 
            * The crawl manager is responsible for receiving the URL input stream from the applications and forwarding it to the available downloaders and DNS resolvers while enforcing rules about robot exclusion and crawl speed. 
      * Downloader
            * A downloader is a high-performance asynchronous HTTP client capable of downloading hundreds of web pages in parallel
      * DNS resolver is an optimized stub DNS resolver that forwards queries to local DNS servers.
      * Communication in our system is done in two ways: via sockets for small messages, and via network file system (NFS) for larger data streams. The use of NFS in particular makes the design very flexible and allows us to tune system performance by redirecting and partitioning I/O between disks. 
![pic](https://cloud.githubusercontent.com/assets/9062406/8274179/b0a0f9b6-1840-11e5-83c0-caa9f5978cbd.png)

* Some static number
      * The downloader component, implemented in Python, fetches files from the web by opening up to 1000 connections to different servers, and polling these connections for arriving data.
      * First, since each page contains on average about 8􀀀 hyperlinks, the set of encountered (but not necessarily downloaded) URLs will grow very quickly beyond the size of main memory, even after eliminating duplicates.
      * Thus, after downloading 20 million pages, the size of the set of encountered URLs will be well above 100 million
      * Second, at this point, any hyperlink parsed from a newly downloaded page and sent to the manager will only be downloaded several days or weeks later.
      * in our crawl application, which is currently able to parse and process up to 400 pages per second on a typical workstation, and 13 KB per page. 

* Process
      * 1. our breadth-first crawl application parses the newly downloaded documents for hyperlinks, then checks a data structure to see which of the URLs in the hyperlinks have already been encountered, and then sends the new URLs to the manager for downloading.
      * 2. A parsing speed of 300 pages per second results in more than 2000 URLs per second that need to be checked and possibly inserted. Each URL has an average length of more than 50 bytes, and thus a naive representation of the URLs would quickly grow beyond memory size.
      * 300 pages * 8 URLs/page = 2400 URLs total, each URL around 50 bytes, 2400 * 50 Bytes = 120KB per sec
      so 1 min: 120KB * 60 = 7.2B = 7.2G, RAM per server is 16G, after 2 hours the RAM may full 

* URL Handling 
      * Thus, we take the following approach, based on well-known techniques:
      * We initially keep the URLs in main memory in a Red-Black tree. When the structure grows beyond a certain size, we
write the sorted list of URLs out to disk and switch to bulk mode.
      * We now use the Red-Black tree in main memory to buffer newly encountered URLs, and periodically merge the memory-resident data into the disk-resident data using a simple scan-and-copy operation, during which all necessary lookups and insertions are performed.

* Domain-Based Throttling 
      
