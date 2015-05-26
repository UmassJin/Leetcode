'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
'''
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        alpha = [chr(i) for i in xrange(65,91)]
        res = []
        while n > 0:
            t = n % 26
            res.append(alpha[t-1])
            n = n / 26
            if t == 0:
                n -= 1 # test case: n = 26, need to return 'Z'
        return ''.join(res[::-1])
