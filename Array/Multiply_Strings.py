Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.


class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply_1(self, num1, num2):
        result = 0
        for i, bit_i in enumerate(num1[::-1]):
            num_i = int(bit_i) * 10**i
            for j, bit_j in enumerate(num2[::-1]):
                num_j = int(bit_j) * 10**j
                result += num_i*num_j 
        return str(result) 

    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        arr = [0 for i in range(len(num1)+len(num2))]
        result = []
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i])*int(num2[j])
        
        for i in range(len(arr)):
            digit = arr[i]%10
            carry = arr[i]/10
            if i+1 < len(arr):
                arr[i+1] += carry
            result.insert(0,str(digit))
        
        while result[0] == '0' and len(result)>1:
            del result[0]
            
        return ''.join(result)        
