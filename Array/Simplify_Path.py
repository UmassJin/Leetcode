Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = ['/']     # Note: the initialization is ['/']
        path_list = path.strip('/').split('/') # Use the strip and split here
        for char in path_list:
            if char == '.' or char == '':
                continue 
            if char == '..':
                if len(stack)>1: stack.pop()  # Check the len(stack) > 1 not check "if stack:"
            else:
              stack.append(char+'/')
        return ''.join(stack).rstrip('/') if len(stack)> 1 else ''.join(stack)      
        # Note: the last return value
        
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        ilist = path.strip('/').split('/')
        result = []
        i = len(ilist)-1
        jump = 0  
        
        while i >= 0:
            if ilist[i] == '' or ilist[i] == '.':
                i -= 1
                continue
            elif ilist[i] == '..':
                jump += 1
            else:
                if jump > 0:
                    jump -= 1
                else:
                    result.insert(0,ilist[i])
            i -= 1
        
        return '/'+ '/'.join(result)
 
# 注意这里用jump，因为有可能出现以下的情况：             
# Input:	"/a/./b/../../c/"
# Output:	"/a/b/c"
# Expected:	"/c"
                  
              
