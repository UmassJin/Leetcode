'''
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, 
so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be 
found in the code's annotation part.

Example
Given n = 5:

isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
Here we are 100% sure that the 4th version is the first bad version.

Note
Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is VersionControl.isBadVersion(v)

Challenge
You should call isBadVersion as few as possible.
'''


#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        left = 0; right = n
        result = n
        if n == 1 and VersionControl.isBadVersion(n):
            return n 
        
        while left <= right:
            mid = (left + right) / 2
            if VersionControl.isBadVersion(mid):
                if (mid - 1 > 0) and (not VersionControl.isBadVersion(mid-1)):
                    return mid 
                right = mid - 1
                result = mid 
            else:
                left = mid +1 
        
        return result 
