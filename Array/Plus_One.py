Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits)-1
        carry = 1
        
        while i >= 0 and carry == 1:   # Note: details ! 
            number = digits[i] + 1
            digit = number % 10
            carry = number/10
            digits[i] = digit
            i-=1
        
        if carry == 1:
            digits.insert(0,1)
        return digits
          
