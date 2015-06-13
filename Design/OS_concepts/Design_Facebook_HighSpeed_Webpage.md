#### A. Three Main components that contribute to the performance of a page load: 
##### Network time
      Reduce the number of bytes required to load a page
##### Generation time
      * Captures how long it takes from when our webserver receives a request from the user to the time it sends back a response
      * This metric measures the efficiency of our code itself and also our webserver, caching, database, and network hardware. 
##### Render time
      * Measures how much time the user's web browser needs to process a response from Facebook and display the resultant web page. 

#####  Time-to-Interact (TTI for short)
      roll three up into one number that would give us a high level sense of how fast the site is. 

#### B. How it works
*  a new library of reusable components, XHP
*  With the component library, it’s easy to optimize our HTML in one place and see it pay off all across the site.
*  reuse the CSS rules
*  BigPipe: it allows us to break our web pages up in to logical blocks of content, called Pagelets
*  Looking at the home page, for example, think of the newsfeed as one Pagelet, the Suggestions box another, and the advertisement yet another.

#### C. [How BigPipe Work](https://code.facebook.com/posts/162127837314007/bigpipe-pipelining-web-pages-for-high-performance/)
##### Traditional Mode
* Browser sends an HTTP request to web server.
* Web server parses the request, pulls data from storage tier then formulates an HTML document and sends it to the client in an HTTP response.
* HTTP response is transferred over the Internet to browser.
* Browser parses the response from web server, constructs a DOM tree representation of the HTML document, and downloads CSS and JavaScript resources referenced by the document.
* After downloading CSS resources, browser parses them and applies them to the DOM tree.
* After downloading JavaScript resources, browser parses and executes them.

##### New Mode 
Details check the link!
* BigPipe breaks the page generation process into several stages:

* Request parsing: web server parses and sanity checks the HTTP request.
* Data fetching: web server fetches data from storage tier.
* Markup generation: web server generates HTML markup for the response.
* Network transport: the response is transferred from web server to browser.
* CSS downloading: browser downloads CSS required by the page.
* DOM(Document Object Model) tree construction and CSS styling: browser constructs DOM tree of the document, and then applies CSS rules on it.
* JavaScript downloading: browser downloads JavaScript resources referenced by the page.
* JavaScript execution: browser executes JavaScript code of the page.


#### Reference:
* [Make Facebook Faster](https://www.facebook.com/note.php?note_id=307069903919)
* [BigPipe Line](https://code.facebook.com/posts/162127837314007/bigpipe-pipelining-web-pages-for-high-performance/)
* [High Performance Websites](http://stevesouders.com/hpws/rules.php)
