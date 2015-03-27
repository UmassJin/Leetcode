Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

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
        
        while i <= max(A,B):
            sum = carry 
            if i <= A:
                sum += int(a[-i]) 
            if i <= B:
                sum += int(b[-i])
            bit = sum % 2
            carry = sum / 2
            i += 1
            result.insert(0,str(bit))
        if carry > 0 :
            result.insert(0,'1')
        return ''.join(result)
