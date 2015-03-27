Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

    # 1. isalnum()
    # 2. lower()
    # 3. no need to check len at the begining

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome_1(self, s):
        if len(s) == 0:
            return True 
        characters = 'abcdefghijklmnopqrstuvwxyz1234567890'    
        left = 0; right = len(s)-1
        
        s = s.lower()
        #while left < len(s)-1 and right >-1 and left <= right:
        while left < right:
            if s[left] not in characters:
                left += 1
            elif s[right] not in characters:
                right -=1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                return False 
        return True         
        
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
      
