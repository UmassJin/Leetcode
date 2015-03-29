Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        str_ver1 = version1.split('.')
        str_ver2 = version2.split('.')
        
        for i in xrange(min(len(str_ver1),len(str_ver2))):
            if int(str_ver1[i]) > int(str_ver2[i]):
                return 1
            elif int(str_ver1[i]) < int(str_ver2[i]):
                return -1
        
        if len(str_ver1) > len(str_ver2):
            if all(int(num) == 0 for num in str_ver1[i+1:]):   # Note: here we should use i+1 instead of i
                return 0
            else:
                return 1
                
        if len(str_ver1) < len(str_ver2):
            if all( int(num) == 0 for num in str_ver2[i+1:]):  # Note: here we should use i+1 instead of i 
                return 0
            else:
                return -1
        
        if len(str_ver1) == len(str_ver2): return 0
        
# Note: in-build function all() usage 
