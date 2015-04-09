##### [转]Interview With Cyan

Shortest Path

Consecutive Subarray

Prob 2:
[1, 4, 20, 10, 3, 5, 9] # (20, 10, 3) Sum=33 Also the subarray must be consecutive Note: 
All elements are positive integers exception: array can include 0 Note: You cannot sort the array 1 4 20

```python
# O(n^2)
def find_consecutive(num, sum):
    length = len(num)
    for i in xrange(length-1):
        cur_sum = 0
        for j in xrange(i, length):
            cur_sum += num[j]  # Note: here we should add the cur_sum
            if cur_sum == sum:
                return num[i:j+1]
            if cur_sum > sum: # Note: break here!
                break
    return -1

# O(n)
def find_consecutive_best(num, sum):
    length = len(num)
    i = 0
    j = 0
    cur_sum = 0
    while j < length:
        if cur_sum + num[j] == sum:
            return num[i:j+1]  # Note: return j+1
        elif cur_sum + num[j] < sum:
            cur_sum += num[j]
            j += 1
        else:
            cur_sum -= num[i]
            i += 1
    return -1
 
num = [9, 1, 4, 20, 10, 3, 5]
sum = 33
print find_consecutive(num, sum)
print find_consecutive_best(num, sum)

```
