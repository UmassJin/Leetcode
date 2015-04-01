The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, 
it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

# Solution 1 
class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        index = 0
        
        while True:
            buf4 = [""]*4
            oneread = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue),n-index)
            for i in xrange(curr):
                buf[index] = self.queue.pop(0)
                index += 1
            if curr == 0: break
        return index   
        

# Why TLE for this one ? Last executed input:	"", [read(1)]
# Explain the wrong answer 
    def read(self, buf, n):
        index = 0
        
        while True:
            buf4 = [""]*4
            oneread = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue),n-index)
            for i in xrange(curr):
                ele = self.queue.pop(0) # Error is here, see the below explaination 
                if ele:
                    buf[index] = ele
                    index += 1
                else: break
            if curr == 0: break
        return index 
        
# This solution is wrong, since for the self.queue, it always extend buf4, which means it always add the 4 length when read, 
# Let's say, for the file 'ab', read(1), read(2), after the read1, the self.queue is ['b', '', '', '', '', '', ''] 
# (pop() 'a' already, so we need to use the n-index == 0 to get out of the while True loop. 
# for the read(2), queue: ['b', '', '', '', '', '', '', '', '', '', ''], curr = n-index = 2-0 = 2, first we add ''b', get 
# index = 1, then we add '', index = 2, so the curr == n-index = 0, out of the while True loop, otherwise, the index will never
# read 2 and curr never reach 0. 

# Solution 2 
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
    
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i
        
class Solution:
    def __init__(self):
        self.buffer_size, self.offset = 0, 0
        self.buffer = [None for _ in xrange(4)]
    
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        read_bytes = 0
        eof = False
        while not eof and read_bytes < n:
            if self.buffer_size == 0:
                size = read4(self.buffer)
            else:
                size = self.buffer_size
            if self.buffer_size == 0 and size < 4:
                eof = True   
            bytes = min(n - read_bytes, size)
            for i in xrange(bytes):
                buf[read_bytes + i] = self.buffer[self.offset + i]
            self.offset = (self.offset + bytes) % 4
            self.buffer_size = size - bytes
            read_bytes += bytes
        return read_bytes

if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in xrange(100)]
    file_content = "ab"
    print buf[:sol.read(buf, 1)]
    print buf[:sol.read(buf, 2)]    

Reference: http://www.danielbit.com/blog/puzzle/leetcode/leetcode-read-n-characters-given-read4-ii
https://github.com/kamyu104/LeetCode/blob/master/Python/read-n-characters-given-read4-ii-call-multiple-times.py
