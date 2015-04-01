The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there 
is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
Note:
The read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        buf4 = [""]*4
        index = 0
        
        while True:
            curr = min(read4(buf4),n-index)
            for i in xrange(curr):
                buf[index] = buf4[i]
                index += 1
            if index == n or curr < 4:
                return index     

# 注意这道题目1与2的区别，对于1来说，因为只读一次，例如有文件has 20 chars, but read(buf, 10), the maximum is 10, 
# so we will return 9 here, 0 based
# But if the read function called for mutiple times, such as file: 'abcd', read(1),read(2),read(3)
# If we still use this function, after read(1), we only read 1 char, but we lose the 'bcd'. Because 
# read4(buf4) already read 4 but since n = 1, we only read out 1.
