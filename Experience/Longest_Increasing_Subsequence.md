#### [ Longest Increasing Subsequence ] (http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/) 
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given 

sequence such that all elements of the subsequence are sorted in increasing order. 

For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

#####Two solutions:
#####First, DP 
* state: dp[i] means the legnth of the ends with char i 
* initializtion: dp[0,....n] = 1
* function: dp[i] = max(dp[j]+1, dp[i]) if (data[j] < data[i] and list[i] < list[j] + 1  ) for j in xrange(i)
* result: dp[n-1]
* O(n^2)

[G4G solution](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)

```python
# DP (O(n^2))
def LIS(A):
    if not A: return 0
    length = len(A)
    dp = [1 for i in xrange(length)] # Note: the initialization is 1 !!
    max_len = 1
    for i in xrange(1, length):
        for j in xrange(i):
            if A[j] < A[i]:
                dp[i] = max(dp[j] + 1, dp[i])
                max_len = max(max_len, dp[i])
    print "max_len: ", max_len
    
    sequence = []
    for i in reversed(xrange(length)):
        if dp[i] == max_len and (len(sequence)==0 or A[i] < sequence[0]):
            sequence.insert(0, A[i])
            max_len -= 1
    print "sequence: ", sequence

arr = [2,1,5,3,6,4,8,9,7]
LIS(arr)
```

* [Reference analysis] (http://www.felix021.com/blog/read.php?1587)
* [Analysis 2] (http://www.cppblog.com/jaysoon/articles/148382.html)
```python
# More efficient solution O(nlogn)
def BinarySearch(last_min, start, end, val):
    while start <= end:
        mid = (start+end)/2 # Here the value should not add 1 
        if last_min[mid] < val:
            start = mid +1
        elif last_min[mid] > val:
            end = mid - 1
        else:
            return mid 
    return start # Note: here we return start !!!    


def LIS_2(A):
    if not A: return 0
    length = len(A)
    last_min = [0 for i in xrange(length)]
    # last_min[i] is the last minimum element in the LIS of length i 
    max_len = 1
    last_min[1] = A[0]
    
    for i in xrange(1, length):
        if A[i] > last_min[max_len]:
            max_len += 1
            last_min[max_len] = A[i]
        else:
            index = BinarySearch(last_min, 1, max_len, A[i])
            last_min[index] = A[i]

    return max_len



arr = [2,1,5,3,6,4,8,9,7]
print LIS_2(arr)

```
