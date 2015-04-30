```
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
```

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        result = []
        for i in xrange(2**n):
            result.append(i>>1 ^ i)
        return result 
        
def graycode( n):
    return [ (i >> 1 ^ i )for i in xrange(1<<n)]
print graycode(3)

        
#Conver from Gray Code to Normal Code:
def graycode(num):
    result = []
    for number in num:
        mask = number >> 1
        while mask != 0:
            number = number ^ mask
            mask = mask >> 1
        result.append(number)
    return result

print graycode([0, 1, 3, 2, 6, 7, 5, 4])

#Reference: http://en.wikipedia.org/wiki/Gray_code        
