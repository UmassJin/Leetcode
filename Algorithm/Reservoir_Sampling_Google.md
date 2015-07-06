#### Introduction
Reservoir sampling is a family of randomized algorithms for randomly choosing a sample of k items from a list S containing n items, 
where n is either a very large or unknown number. Typically n is large enough that the list doesn't fit into main memory.

#### Time Complexity
O(n)

#### Probability
when the algorithm has finished executing, each item in S has equal probability 
(i.e. k/length(S)) of being chosen for the reservoir. 

#### Prove
1. For all i, the ith element of S is chosen to be included in the reservoir with probability k/i.
2. At each iteration the jth element of the reservoir array is chosen to be replaced with probability 1/k * k/i
    * 这里是指之后每个i+1被选中在reservoir里面，而且取代之前的那个i的概率是1/k * k/i ＝ 1/i
3. 所以第i个element最终留在array里面的概率是 
![pic](https://cloud.githubusercontent.com/assets/9062406/8529243/91d4a65c-23cd-11e5-9adf-f9fe3500bda9.png)

#### Implement 
```python
import random

def selectKitems(array, k):
    n = len(array)
    # copy the first k element
    reservoir = array[:k]
    for i in xrange(k, n):
        # pick random index from 0 to i (include)
        index = random.randint(0,i)
        print "index: ", index
        if index < k:

            reservoir[index] = array[i]
    print reservoir[:3]


test = [1,2,3,4,5,6,7,8,9,10]
selectKitems(test, 3)
```


#### Reference
* [G4G](http://www.geeksforgeeks.org/reservoir-sampling/)
* [wiki](https://en.wikipedia.org/wiki/Reservoir_sampling)
* [中文版本](http://web.eecs.utk.edu/~sli22/resources/Reservoir_Sampling.pdf)
