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
        

Why TLE for this one ? Last executed input:	"", [read(1)]
    def read(self, buf, n):
        index = 0
        
        while True:
            buf4 = [""]*4
            oneread = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue),n-index)
            for i in xrange(curr):
                ele = self.queue.pop(0)
                if ele:
                    buf[index] = ele
                    index += 1
                else: break
            if curr == 0: break
        return index 
