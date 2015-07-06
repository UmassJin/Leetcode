#### Introduction
Given an array, write a program to generate a random permutation of array elements. 
This question is also asked as “shuffle a deck of cards” or “randomize a given array”.

```
To shuffle an array a of n elements (indices 0..n-1):
  for i from n - 1 downto 1 do
       j = random integer with 0 <= j <= i
       exchange a[j] and a[i]
```       

#### prove 
* for each element in the array, the possibility of choosen is O(1/n)
* for the kth element, it choosen at ith time is:
* (1-1/i) * 1/(i-1) = 1/i
* each element, last time did not get choosen, the probability is 1 - 1/i
* each element, this time get choosen, the probability is 1/(i-1)
* so the total probability is 1/i

#### Implement 
```python
import random

def shuffle(array):
    n = len(array)
    for i in xrange(n-1, -1, -1):
        index = random.randrange(i+1)
        print
        array[i], array[index] = array[index], array[i]
    print array
    
test = [1,2,3,4,5,6]
shuffle(test)
```


#### Reference:
* [wiki](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm)
* [G4G Shuffle a given array](http://www.geeksforgeeks.org/shuffle-a-given-array/)
