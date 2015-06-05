#### How would you implement Google Search?

##### Related questions:
1. web crawler 
2. cache system 
3. map reduce 

##### 1. Google Search Features 
* First, it makes use of the link structure of the Web to calculate a quality ranking for each web page. This ranking is called PageRank and is described in detail in [Page 98]. 
* Second, Google utilizes link to improve search results.

##### 2. Google Search Architecture 
![pic](http://i.stack.imgur.com/aogj9.gif)

1. In Google, the web crawling (downloading of web pages) is done by several distributed crawlers. There is a URLserver that sends lists of URLs to be fetched to the crawlers. 
2. The web pages that are fetched are then sent to the storeserver. The storeserver then compresses and stores the web pages into a repository. 
3. Every web page has an associated ID number called a docID which is assigned whenever a new URL is parsed out of a web page.
4. The indexing function is performed by the indexer and the sorter. The indexer performs a number of functions. It reads the repository, uncompresses the documents, and parses them. 
5. Each document is converted into a set of word occurrences called hits. The hits record the word, position in document, an approximation of font size, and capitalization. 
6. The indexer distributes these hits into a set of "barrels", creating a partially sorted forward index. 
7. The indexer performs another important function. It parses out all the links in every web page and stores important information about them in an anchors file. This file contains enough information to determine where each link points from and to, and the text of the link.
8. The URLresolver reads the anchors file and converts relative URLs into absolute URLs and in turn into docIDs. It puts the anchor text into the forward index, associated with the docID that the anchor points to. It also generates a database of links which are pairs of docIDs. The links database is used to compute PageRanks for all the documents.
9. The sorter takes the barrels, which are sorted by docID (this is a simplification, 4.2.5), and resorts them by wordID to generate the inverted index. This is done in place so that little temporary space is needed for this operation. The sorter also produces a list of wordIDs and offsets into the inverted index. 
10. A program called DumpLexicon takes this list together with the lexicon produced by the indexer and generates a new lexicon to be used by the searcher. The searcher is run by a web server and uses the lexicon built by DumpLexicon together with the inverted index and the PageRanks to answer queries.

##### 3. Major Data Structures


##### 4. Google Query Evaluation
* Parse the query.
* Convert words into wordIDs.
* Seek to the start of the doclist in the short barrel for every word.
* Scan through the doclists until there is a document that matches all the search terms.
* Compute the rank of that document for the query.
* If we are in the short barrels and at the end of any doclist, seek to the start of the doclist in the full barrel for every word and go to step 4.
* If we are not at the end of any doclist go to step 4.

Sort the documents that have matched by rank and return the top k.


##### Reference:
* [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/~backrub/google.html#data)
* [How to implement google search](http://programmers.stackexchange.com/questions/38324/interview-question-how-would-you-implement-google-search)
