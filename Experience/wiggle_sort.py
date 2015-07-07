'''
Given a sorted array, and re-arrange it to wiggle style in one pass.
i.e. [1] A0 >= A1 <= A2 >= A3 .... .... An.
     [2] A0 <= A1 >= A2 <= A3 .... .... An.
'''     
     
def wiggle_sort(arr):
    if not arr or len(arr) == 1: return arr
    lens = len(arr)
    
    flag = False   
    cur = arr[0]
    for i in xrange(lens-1):
        if (flag and cur < arr[i+1]) or (not flag and cur > arr[i+1]):
            arr[i] = arr[i+1]
        else:
            arr[i] = cur
            cur = arr[i+1]
        flag = not flag

    arr[lens-1] = cur
    return arr

# flag = True means  arr[i-1] <= arr[i] >= arr[i+1]
# flag = Flase means arr[i-1] >= arr[i] <= arr[i+1]

arr = [1,2,3,4,5,6]
print wiggle_sort(arr)
arr1 = [1,3]
print wiggle_sort(arr1)
arr2 = [3,1]
print wiggle_sort(arr2)
arr3 = [5,5,6,6,7,8]
print wiggle_sort(arr3)

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python wiggle_sort.py
[1, 3, 2, 5, 4, 6]
[1, 3]
[1, 3]
[5, 6, 5, 7, 6, 8]
