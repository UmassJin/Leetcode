Onsite interview with Facebook for finding rotated mirrow number like 808 which is less than N.

思路：
1) Find the maximum length of the candidate number 
2) Add the number in front of and back 
3) Check if this number is in the range

``` python
def rotated_mirror_number(n):
    length = 0
    while n - 10**length > 0:
        length += 1
    ret = []
    rotated_helper(n, length, [], ret)
    return ret

def rotated_helper(n, length, res, ret):
    num = convert_to_num(res)
    if num > n or len(res) > length:
        return
    if len(res) > 0 and res[0] != 0:  # Note: need to exclude the 0 start number !!
        ret.append(num)
        print "ret: ", ret
    if len(res) == 0:
        for i in range(10):
            res.append(i)
            print "first, res: ", res
            rotated_helper(n, length, res, ret)  # Note: this is used to handle 1, 2, 3...single number!
            res.pop()

    for i in range(10):
        res.append(i)
        res.insert(0,i)
        print "res: ", res
        rotated_helper(n, length, res, ret)
        res.pop() # Note: need to pop the number !
        res.pop(0)

def convert_to_num(int_list):
    res = 0
    for digit in int_list:
        res = res*10 + digit
    return res

print rotated_mirror_number(150)
```
