# http://www.geeksforgeeks.org/move-zeroes-end-array/

def pushZerosToEnd(arr):
    if not arr: return []
    count = -1
    n = len(arr)
    for i in xrange(n):
        if arr[i] != 0:
            count += 1
            arr[count] = arr[i]
            
    while count + 1 < n:
        count += 1
        arr[count] = 0

    return arr

test = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print pushZerosToEnd(test)
~                              
