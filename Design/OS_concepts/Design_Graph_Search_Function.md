## Facebook Graph Search 
### Challenge
#### Graph Search Scale
* More than 1 billion people use Facebook each month, they have shared more than 240 billion photos on the site, and formed more that 1 trillion connections of thousands of different types

#### Usage convenient 
* We wanted people to be able to construct their own views of the particular Facebook content they were interested in.

#### Privacy 
* This, of course, is why Graph Search is such a powerful experience: a lot of what you will find is content that is not public, but content that someone has shared with a limited audience that happens to include you.

#### Future
* Today's Graph Search beta is just the beginning. We're starting with a focus on people, photos, places and interests, but are looking forward to incorporating posts and Open Graph actions, as well as making Graph Search available on mobile and in every language

### [Build out the Infrastructure for Graph Search](https://www.facebook.com/note.php?note_id=10151347573598920)
* Typeahead: 
    * a new search product
    * deliver search result as the searcher typed, or "prefix matching"

* Facebook Graph: entries are the nodes and the relationships are the edges
    * Nodes in the graph are identified by a unique number called the fbid.
    * The kinds of entities searched are users, pages, places, groups, applications
    * The goal of Graph Search was to extend this capability to also search based on the relationship between entities--meaning we are also searching over the edges between the corresponding nodes.
  
* An inverted-index system called Unicorn
    * The main components of Unicorn 
      * The index -- a many-to-many mapping from attributes (strings) to entities (fbids)
      * A framework to build the index from other persistent data and incremental updates
      * A framework to retrieve entities from the index based on various constraints on attributes

* Building an Index for Facebook
    * Unicorn is not only the software that holds our index, but the system that builds the index and the system that retrieves from the index.

### [Indexing and ranking in Graph Search](https://www.facebook.com/notes/facebook-engineering/under-the-hood-indexing-and-ranking-in-graph-search/10151361720763920)
*  Graph Search takes place in two distinct phases – the query suggestion phase, and the search phase.
      * Query Suggestion Phase
         * a Natural Language Processing (NLP) module attempts to parse it based on a grammar.
         * The NLP module parses the query, and identifies portions to search in Unicorn. Steps 2 through 9 are then performed simultaneously for each of these search requests.
         * The Top Aggregator receives the request and fans it out for each vertical. Steps 3 through 8 are performed simultaneously for each vertical.
         * The Top Aggregator rewrites the query for the vertical. Each vertical has different query rewriting requirements. Rewritten queries are typically augmented with additional searcher context.
         * The Top Aggregator sends the rewritten query to the vertical – first to the Vertical Aggregator, which passes it on to each of the Index Servers.
         * Each Index Server retrieves a specified number of entities from the index.
         * Each of these retrieved entities is scored and the top results are returned from the Index Server to the Vertical Aggregator.
         * The Vertical Aggregator combines the results from all Index Servers and sends them back to the Top Aggregator.
         * The Top Aggregator performs result set scoring on the returned results separately for each vertical.
         * The Top Aggregator runs the blending algorithm to combine the results from each vertical and returns this combined result set to the NLP module.
         * Once the results for all the search requests are back at the NLP module, it constructs all possible parse trees with this information, assigns a score to each parse tree and shows the top parse trees as suggestions to the searcher.\
      
      * Search Phase 

## Graph Search 
#### 1. Requirement 
*  cost-effective
*  highly available
*  low latency (fast retrieval).

#### 2. Functionality 
* Upload image 
* Query image 






