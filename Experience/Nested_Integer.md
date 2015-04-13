#####[转]From NC QQ group and mitbbs, Linkedin Second round phone interview

This is the interface that represents nested lists.
You should not implement it, or speculate about its implementation.

```
public interface NestedInteger
{
    /** @return true if this NestedInteger holds a single integer, rather than a nested list */
    boolean isInteger();

    /** @return the single integer that this NestedInteger holds, if it holds a single integer
     * Return null if this NestedInteger holds a nested list */
    Integer getInteger();

    /** @return the nested list that this NestedInteger holds, if it holds a nested list
     * Return null if this NestedInteger holds a single integer */
    List<NestedInteger> getList();
}


/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
 * For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
 * Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
 */

// null || empty: 0
//  1*2
//
public int depthSum (List<NestedInteger> input)

```

```python
def depthSum(input):
    if isInteger(input):
        return getInteger(input)
    return get_depth_recur(input, 1) # Note: the first level is 1 !!!
    
def get_depth_recur(input, depth):
    if isInteger(input):
        return getInteger(input)*depth
    nested_list = getList(input)
    
    sum = 0
    for element in nested_list:
        sum += get_depth_recur(element, depth+1)
    return sum
```    
