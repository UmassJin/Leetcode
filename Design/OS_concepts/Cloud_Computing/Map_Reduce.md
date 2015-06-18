* Map
    * processes are sequentially and independently 
    * Could run multiple Map process parallelly 
    * called only once for the all input 

![pic](https://cloud.githubusercontent.com/assets/9062406/8224568/acd7638e-153d-11e5-8679-c29ee8b639f8.png)

* Reduce
    * Reduces process batches of values associated with the same key while Maps process keys independently
    * reduce called one time for the one key 

![pic](https://cloud.githubusercontent.com/assets/9062406/8224561/9744f64e-153d-11e5-81ef-fdcab0f66b1a.png)

* Different Product
    * Sort
    * Advantage:
      * A Map can know which contiguous sets of its key-value pairs (sharing the same key) need to be sent to one Reduce
      * A Reduce task can call the Reduce function on a contiguous set of key-value pairs (sharing the same key)
      * Sorting as an application becomes very simple to write

* [Implement](https://github.com/UmassJin/Leetcode/blob/master/Design/OS_concepts/Design_Map_Reduce.py)
