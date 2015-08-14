#### Problem
Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. 
It is given that ll array elements are distinct.

#### Implement 
```python
import random

def KthSmallest(array, l, r, k):
    if (k > 0 and (k <= (r-l+1))):
        pos = randomPartition(array, l, r)
        if pos - l == k -1:
            return array[pos]
        elif pos - l > k - 1:
            return KthSmallest(array, l, pos-1, k)
        else:
            return KthSmallest(array, pos+1, r, k-(pos-l+1))
    return -1

def randomPartition(array, l, r):
    pivot_index = random.randint(l, r)
    print "pivot", array[pivot_index]
    array[pivot_index], array[r] = array[r], array[pivot_index]
    i = l
    pivot = array[r]
    for j in xrange(l, r):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[r] = array[r], array[i]
    print "array: ", array
    return i


array = [12, 3, 5, 7, 4, 19, 26]
print KthSmallest(array, 0, len(array)-1, 3)
```

time complexity:
The worst case time complexity of the above solution is still O(n2). In worst case, the randomized function may always pick a corner element. The expected time complexity of above randomized QuickSelect is Θ(n)

#### Reference
* [G4G set1](http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/)
* [G4G set2](http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/)
* [Wiki QuickSelect](https://en.wikipedia.org/wiki/Quickselect)
* [Wiki Median of Median](https://en.wikipedia.org/wiki/Median_of_medians)
