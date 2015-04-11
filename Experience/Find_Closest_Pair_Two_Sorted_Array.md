[Find the closest pair from two sorted arrays] (http://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/)

Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

We are given two arrays ```ar1[0…m-1] and ar2[0..n-1]``` and a number ```x```, 
we need to find the pair ```ar1[i] + ar2[j]``` such that absolute value of ```(ar1[i] + ar2[j] – x)``` is minimum.

Example:

``` python
Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
```

```python

def find_closet_pair_two_sorted_arr(A, B, target):
    result = []
    diff = 1<<32-1
    l = 0; r = len(B) - 1
    result = [l, r]
    while l < len(A) and r >= 0:
        if abs(A[l] + B[r] - target) < diff:
            diff = abs(A[l] + B[r] - target)
            result[0] = A[l]
            result[1] = B[r]
        if A[l] + B[r] > target:
            r -= 1
        else:
            l += 1
    return result

```


