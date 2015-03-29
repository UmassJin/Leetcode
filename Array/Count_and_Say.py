The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

# How to prove the count should less than 10
# https://leetcode.com/discuss/6762/how-to-proof-the-count-is-always-less-than-10

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in xrange(1,n):  # Note: here start from 1 
            s = self.count(s)
        return s 
    
    def count(self,s):
        amount = 1
        curr = '#'
        result = ''
        for char in s:
            if char != curr:
                if curr != '#':
                    result += str(amount) + curr  # Note: here we should use result += str(amount) + curr
                curr = char
                amount = 1
            else:
                amount +=1
        result += str(amount) + curr
        return result 

