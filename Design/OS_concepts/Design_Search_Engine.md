### How would you implement Google Search?

### Related questions:
1. web crawler 
2. cache system 
3. map reduce 

### 1. Google Search Features 
* First, it makes use of the link structure of the Web to calculate a quality ranking for each web page. This ranking is called PageRank and is described in detail in [Page 98]. 
* Second, Google utilizes link to improve search results.

### 2. Google Search Architecture 
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

### 3. Major Data Structures


### 4. Google Query Evaluation
* Parse the query.
* Convert words into wordIDs.
* Seek to the start of the doclist in the short barrel for every word.
* Scan through the doclists until there is a document that matches all the search terms.
* Compute the rank of that document for the query.
* If we are in the short barrels and at the end of any doclist, seek to the start of the doclist in the full barrel for every word and go to step 4.
* If we are not at the end of any doclist go to step 4.

Sort the documents that have matched by rank and return the top k.

### 5. Design Thought 
1. Create the index by going through the documents
2. Answering the search queries using the index we created.
3. ranking, classification, compression, and duplicate detection mechanisms.

#### A. Create the Index 
##### 1) Crawling the Web 
1. crawling the web 实际上是扒下一个网址的html网页
2. 存在的challenge：
    * A major performance stress is DNS lookup. Each crawler maintains a its own DNS cache so it does not need to do a DNS lookup before crawling each document. Each of the hundreds of connections can be in a number of different states: looking up DNS, connecting to host, sending request, and receiving response. These factors make the crawler a complex component of the system. It uses asynchronous IO to manage events, and a number of queues to move page fetches from state to state.
    * There are maybe garbage information get from the webs 
3. [Robots Exclusion Standard](http://en.wikipedia.org/wiki/Robots_exclusion_standard)
4. The web crawler's job is to spider web page links and dump them into a set. The most important step here is to avoid getting caught in infinite loop or on infinitely generated content. 

##### 2) Inverted Index
1. After we get the html from crawling the web, we need to parse these webpages and assignt the index for searching 
2. Inverted index is a data structure that we build while parsing the documents that we are going to answer the search queries on. Given a query, we use the index to return the list of documents relevant for this query. The inverted index contains mappings from terms (words) to the documents that those terms appear in. Each vocabulary term is a key in the index whose value is its postings list. 
3. Query Types:
    * one word queries
    * free text queries
    * phrase queries 
4. Parsing the collections 
    * 1) Concatenate the title and the text of the page. 
    * 2) Lowercase all words. 
    * 3) Get all tokens, where a token is a string of alphanumeric characters terminated by a non-alphanumeric character. The alphanumeric characters are defined to be [a-z0-9]. So, the tokens for the word ‘apple+orange’ would be ‘apple’ and ‘orange’. 
    * 4) Filter out all the tokens that are in the stop words list, such as ‘a’, ‘an’, ‘the’. 
    * 5) Stem each token using Porter Stemmer to finally obtain the stream of terms. [Porter Stemmer](http://tartarus.org/~martin/PorterStemmer/) removes common endings from words. For example the stemmed version of the words fish, fishes, fishing, fisher, fished are all fish. 

##### 3) Building Inverted Index   
1. Use the hastable (python's dictionary) to store the inverted index in memory.
2. Key: every term(word); Value: a) the list of documents that the term appears in and b) the positions of term occurrences within the document
3. The reason is to answer the phrase queries we need positional information, because we want to check whether the terms in the query appear in the specified order. Without knowing the positions of the terms in the document, we can only check whether the query terms simply appear in a document. To verify the order, we need to know their positions. 
4. Then we merge the index of the current page with the main inverted index, which is the index for the whole corpus. The merging is simple. For every term in the current page, we append its postings list to the postings list of that term in the main index (which is a list of lists as described above).
5. Then we build the index for this document (note that the terms are not the stemmed versions for demonstration. In the actual program a term would be stemmed by Porter Stemmer before being added to the index. 
6. So the word ‘retrieval’ would be added to the index as the term ‘retriev’ after being stemmed): 
```python
{ ‘web’: [1, [0, 2]], ‘retrieval’: [1, [1]], ‘search’: [1, [3]], ‘information’: [1, [4]] } 
```
Then we merge this dictionary with our main dictionary (which is currently empty because this is the first document in the collection). Our main dictionary becomes: 
```python
{ ‘web’: [ [1, [0, 2]] ], ‘retrieval’: [ [1, [1]] ], ‘search’: [ [1, [3]] ], ‘information’: [ [1, [4]] ] } 
```
7. The index is stored as text in the following format: term|docID1:pos1,pos2;docID2:pos3,pos4,pos5;… Every line of the file contains a separate term. The line starts with a term, and then the character ‘|’ is used to separate the term from its postings list. The postings list of a term has the following form. First document ID containing the term, followed by a colon, followed by the positions of the term in that document with commas in between, semicolon, second document ID containing the term, colon, comma delimited positions, and it goes on like this. Using the above example, the term – postings list pair ‘web’: [ [1, [0, 2]], [2, [2]] ] would be saved as: web|1:0,2;2:2 

##### The above part corresponding to the step 1- 5 
 
#### B. Query Index 
##### 1) Query Types
* Let’s first remember the query types. Our search engine is going to answer 3 types of queries that we generally use while searching. 
    1) One Word Queries (OWQ): OWQ consist of only a single word. Such as computer, or university. The matching documents are the ones containing the single query term. 
    2) Free Text Queries (FTQ): FTQ contain sequence of words separated by space like an actual sentence. Such as computer science, or Brown University. The matching documents are the ones that contain any of the query terms. 
    3) Phrase Queries (PQ): PQ also contain sequence of words just like FTQ, but they are typed within double quotes. The meaning is, we want to see all query terms in the matching documents, and exactly in the order specified. Such as “Turing Award”, or “information retrieval and web search”. 
* The transformations performed on words of the collection, such as stemming, lowercasing, removing stopwords, and eliminating non-alphanumeric characters will be performed on the query as well. So, querying for computer or Computer is basically the same.

##### 2) [Detailed Implement] (http://www.ardendertat.com/2011/05/31/how-to-implement-a-search-engine-part-2-query-index/)
###### Phrase Queries
An example will make everything clear. Let’s say we search for “computer science department”. We first get the document list of all query terms, as we did in FTQ: computer: [1, 2, 3], science: [1, 2, 3], and department: [1, 2]. Then we intersect all these lists to get the documents that contain all query terms, which is [1, 2]. Next, we should check whether the order is correct or not. First, we get the postings list of the query terms for document 1. Which is computer: [1, [2, 5]], science: [1, [3]], and department: [1, [4, 6]. Then, we extract the positions of each query term, and put them in separate lists, resulting in [ [2, 5], [3], [4, 6] ]. Each list corresponds to the positional information of a query term. We don’t touch the first list, but subtract i-1 from the elements in the ith list, resulting in [ [2, 5], [2], [2, 4] ]. Finally, we take the intersection of the lists, which is [2]. Since the intersection is not empty, we conclude that document 1 is a matching document. Next, we check document 2. Get the positions of query terms and put them to separate lists as before: [ [1, 7], [2, 5], [0, 6] ]. Perform the subtractions: [ [1, 7], [1, 4], [-2, 4] ]. And take the intersection: []. The result of the intersection is empty, meaning the query terms don’t appear in the correct order, so this is not a matching document. There is no more document that contains all query terms. So, the result of the phrase query is document 1 only: [1].

#### C. [Ranking](http://www.ardendertat.com/2011/07/17/how-to-implement-a-search-engine-part-3-ranking-tf-idf/)


#### 注意的细节
1. 在create index的时候，我们对于用户输入的query要处理，将大写变为小写，处理特殊字符，去掉'a','the'等词语，用Porter Stemmer处理，保证fisher, fishes, fished, 都为fish
2. The Porter stemming algorithm (or ‘Porter stemmer’) is a process for removing the commoner morphological and inflexional endings from words in English.
3. 要注意在用directory储存时，value不仅储存document number，还要储存单词在文件中相对的位置


#### Reference:
* [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/~backrub/google.html#data)
* [How to implement google search](http://programmers.stackexchange.com/questions/38324/interview-question-how-would-you-implement-google-search)
* [Good implement for google search](http://www.ardendertat.com/2011/05/31/how-to-implement-a-search-engine-part-2-query-index/)
* [Page Rank](http://en.wikipedia.org/wiki/PageRank)
* [Internet Robot](http://en.wikipedia.org/wiki/Internet_bot)



#### 笔记
* Caching in web search systems
      * Benefits:
      * performance! a few machines do work of 100s or 1000s
      * much lower query latency on hits
         * queries that hit in cache tend to be both popular and expensive, expensive means like "single word search", which returns a lot of the documents or higher rankings 
      * Beware: big latency spike/capacity drop when index updated or cache flushed, need to flushed aviod high speed 
