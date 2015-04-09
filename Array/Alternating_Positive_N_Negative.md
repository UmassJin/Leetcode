## // Rearrange Array Alternating Positive Negative Items 

Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed
by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. 
If there are more negative numbers, they too appear in the end of the array.

Example:
Input: arr[] = {1, 2, 3, -4, -1, 4} Output: arr[] = {-4, 1, -1, 2, 3, 4}
Input: arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8} output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
Found online, also NC has marked this to high frequency

[Solution: G4G](http://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/) 
```python
def rearrange_array(A):
    if not A: return None
    i = 0
    while i < len(A):
        if i % 2 == 0 and A[i] > 0:
            start = i + 1
            while start < len(A) and A[start] >= 0:
                start += 1
            if start == len(A):
                break
            tmp = A[start]
            del A[start]
            A.insert(i, tmp)
        elif i % 2 != 0 and A[i] < 0:
            start = i + 1
            while start < len(A) and A[start] < 0:
                start += 1
            if start == len(A):
                break
            tmp = A[start]
            del A[start]
            A.insert(i, tmp)
        i += 1

    return A

print "[1]: ", rearrange_array([1])
print "[-1]: ", rearrange_array([-1])
print "[1, 2, 3, -4, -1, 4]: ", rearrange_array([1, 2, 3, -4, -1, 4])
print "[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]: ", rearrange_array([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])


def rearrange_array_rotate(A):
    if not A: return None
    for i in xrange(len(A)):
        if (i % 2 == 0 and A[i] > 0) or (i % 2 != 0 and A[i] < 0):
            index = find_next(i, A)
            if index == len(A):   
                break
            rotate(i, index, A)
    return A

def find_next(i, A):
    start = i + 1
    if A[i] > 0: is_positive = -1
    if A[i] < 0: is_positive = 1
    while start < len(A) and A[start]*is_positive <= 0 :
        start += 1
    return start

def rotate(i, index, A):
    tmp = A[index]
    j = index
    while j > i:
        A[j] = A[j-1]
        j = j - 1
    A[j] = tmp

print "[1]: ", rearrange_array_rotate([1])
print "[-1]: ", rearrange_array_rotate([-1])
print "[1, 2, 3, -4, -1, 4]: ", rearrange_array_rotate([1, 2, 3, -4, -1, 4])
print "[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]: ", rearrange_array_rotate([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])

```      

