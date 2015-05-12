Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

# Couple of details need to note in this solution 

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        A = len(a)
        B = len(b)
        i = 1
        result = []
        carry = 0
        
        while i <= max(A,B):  # we need to choose the maximum length of A and B, not the minimum, and here is <= 
            sum = carry 
            if i <= A:  # Here we need to use <=, since a[-lena] is the first char
                sum += int(a[-i]) 
            if i <= B:
                sum += int(b[-i])
            bit = sum % 2
            carry = sum / 2
            i += 1
            result.insert(0,str(bit)) # When insert the bit, we need to transfer to the string, since ''.join(result)
        if carry > 0 :
            result.insert(0,'1') # Detail:  we need to add the string here 
        return ''.join(result)
