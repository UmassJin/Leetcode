####[G4G](http://geeksquiz.com/quick-sort/)
##### The Best Case:
The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case.
```T(n) = 2T(n/2) + O(n)```

##### The Worst Case:
The worst case occurs when the partition process always picks greatest or smallest element as pivot. 
If we consider above partition strategy where last element is always picked as pivot, 
the worst case would occur when the array is already sorted in increasing or decreasing order. 
Following is recurrence for worst case.
```
T(n) = T(0) + T(n-1) + O(n)
which is equivalent to  
 T(n) = T(n-1) + O(n)
```

#####Code:
```python
def quick_sort(array):
    if not array: return array
    sort_help(array, 0, len(array)-1)
    return array

def sort_help(array, left, right):
    if left < right:
        pivot, start, end = array[left], left, right
        while start <= end:
            while array[start] < pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            if start <= end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
        print "array: ", array
        print "left %d, right: %d, start: %d, end: %d" %(left, right, start, end)
        sort_help(array, left, end)
        sort_help(array, start, right)
            
test = [6,8,5,9,3,2,2,1,4,7]
print quick_sort(test)

```
