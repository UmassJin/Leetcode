##### [Find k closest elements to a given value] (http://www.geeksforgeeks.org/find-k-closest-elements-given-value/)

Given a sorted array arr[] and a value X, find the k closest elements to X in arr[]. 
Examples:
```
Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
```
Note that if the element is present in array, then it should not be in output, only the other closest elements are required.

In the following solutions, it is assumed that all elements of array are distinct.

def find_k_closet_elements(arr, k, x):
    if not arr: return None
    length = len(arr)
    index = find_point(arr, 0, length-1, x)
    count = 0
    result = []
    r = index + 1
    if arr[index] == x:
        l = index -  1
    else:
        l = index

    while r < length and l >= 0 and count < k:
        if abs(arr[r]-x) > abs(arr[l]-x):
            result.append(arr[l])
            l -= 1

        else:
            result.append(arr[r])
            r += 1
        count += 1

    while count < k and l >= 0:
        result.append(arr[l])
        l -= 1
        count += 1

    while count < k and r < n:
        result.append(arr[r])
        r += 1
        count ++ 1
    return result

def find_point(arr, start, end, x):
    if x < arr[start]:
        return start
    elif x > arr[end]:
        return end

    mid = (start + end)/2
    # Note: here we check whether the arr[mid] <= x!!!
    if arr[mid] <= x and arr[mid+1] > x:
        return mid
    elif arr[mid] < x:
        return find_point(arr, mid+1, end, x)
    else:
        return find_point(arr, start, mid-1, x)

print find_k_closet_elements([12, 16, 22, 30, 35, 39, 42,45, 48, 50, 53, 55, 56],4,35)
                                                                             50,8          Bot

