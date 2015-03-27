Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.

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
