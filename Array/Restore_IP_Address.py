Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(s, part, list):
            if part == 4:
                if s == '':
                    list = list[:len(list)-1] # Note: here should be len(list)-1
                    result.append(list)
                return
            else:
                for i in range(1,4): # Note: the range should between (1,4)
                    if i<= len(s) and int(s[:i])<= 255:
                            dfs(s[i:], part+1, list+s[:i]+'.')
                    if i<= len(s) and s[0] == '0': # Note: consider the first letter is '0'
                        break                        
        result = []
        dfs(s, 0, '')
        return result 
            
