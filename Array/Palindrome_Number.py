Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.

# Best answer ! 
# https://leetcode.com/discuss/33500/an-easy-lines-code-only-reversing-till-half-and-then-compare
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): return False # except 10, 100
        sum  = 0
        while x > sum:
            sum = sum * 10 + x % 10
            x = x / 10
        return (x == sum) or (x == sum/10)

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 10
        while x > div:
            div *= 10 
        div /= 10 
        while x > 0:
            if x / div != x % 10:  # compare the first number and last number
                return False
            x = (x % div )/10
            div /= 100
        return True
