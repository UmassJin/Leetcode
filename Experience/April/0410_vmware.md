* Algorithm question: 2sum
* Network question:

1) If you enter "www.google.com", what happened? How the connection happened ?

* browser checks cache; if requested object is in cache and is fresh, skip to 9th step 
* browser asks OS for server's IP address
* OS makes a DNS lookup and replies the IP address to the browser(host/dig)
* browser opens a TCP connection to server (this step is much more complex with HTTPS)
* browser sends the HTTP request through TCP connection
* browser receives HTTP response and may close the TCP connection, or reuse it for another request
* browser checks if the response is a redirect (3xx result status codes), authorization request (401), error (4xx and 5xx), etc.; these are handled differently from normal responses (2xx)
* if cacheable, response is stored in cache
* browser decodes response (e.g. if it's gzipped)
* browser determines what to do with response (e.g. is it a HTML page, is it an image, is it a sound clip?)
* browser renders response, or offers a download dialog for unrecognized types

2) How the hop/router between them connect to the next one ?

3) What's the difference between UDP and TCP ? 

See the [knowledge](https://github.com/UmassJin/Leetcode/blob/master/knowledge.md)

4) How the router table looks like in the router ? 

5) If we "ping <IP address>" does not successful, how could we troubleshoot ?

[Solution](http://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r4-0/troubleshooting/guide/tr40asr9kbook/tr40con.pdf)

