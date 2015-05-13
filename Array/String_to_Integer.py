Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
spoilers alert... click to show requirements for atoi.
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus 
or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()   # Note: here use the str.strip() to strip the whitespace in the leading and tailing    
        length = len(str)
        if length == 0: return 0
        sign = 1
        res = 0
        imin, imax = -1<<31, (1<<31)-1 # Note: use this method to get the max/mix value 
        
        for i, bit in enumerate(str): # Note: use enumerate 
            if i == 0 and (bit in ['+','-']): # Note: use the bit in [] to judge and check i == 0 !! test case:'+-2' ==> 0
                if bit == '-':
                    sign = -1
            
            elif bit.isdigit(): # Note 3) 
                res = res*10 + int(bit)
                if res*sign >= imax:  # Note 5) 
                    return imax 
                if res*sign <= imin:
                    return imin
            else:                     # Note 4) 
                break
        return sign*res 

# immediatly return the imax or the imin, since if we assign the imin to res, then sign*res, will return the wrong answer .
# Some corner case: 
# 1) how to handle the white space before and after the string. 
# 2) when starting the first character, need to consider the minus or plus sign.  
# 3) The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function. 
# 4) If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed. 
# 5) If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned. 

