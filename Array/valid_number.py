'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your 
function signature accepts a const char * argument, please click the reload button  
to reset your code definition.
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        if not s: return True
        has_e = False
        has_dot = False
        has_number = False
        has_numaftere = False
        
        s = s.strip()
        for i, char in enumerate(s):
            if char.isdigit():
                has_number = True
                has_numaftere = True
            elif char == 'e':
                if has_e or not has_number:
                    return False
                has_e = True
                has_numaftere = False
            elif char == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif (char == '+') or (char == '-'):
                if i != 0 and s[i-1] != 'e':
                    return False
            else:
                return False
        
        return (has_numaftere and has_number)

# Reference: 
# 状态方程：http://blog.csdn.net/kenden23/article/details/18696083
# 参考图示：http://www.cnblogs.com/zuoyuan/p/3703075.html
# Java Solution: https://leetcode.com/discuss/26682/clear-java-solution-with-ifs
# 有'e'之后不能有'.', '.'必须在e前面
# 'e'之后可以有'+/-', 之前必须有数字，之后必须有数字, 已经出现过'e'也不行
# '.'之前不必有数字，但是不能有'e',不能有一个'.'
