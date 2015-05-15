'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        
        while left <= right: # <=, test case: [1], 1
            mid = (left + right) /2
            if target == A[mid]:
                return mid
            if A[mid] >= A[left]: # Note: here should be >=, test case: [3,1], 0; [1],0
                if target < A[mid] and target >= A[left]:
                    right = mid -1
                else:
                    left = mid+1
            elif A[mid] < A[right]: # Note: here should be < or <=
                if target > A[mid] and target <= A[right]:
                    left = mid+1
                else:
                    right = mid -1
        return -1            
                   
'''                    
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
Analysis:http://chaoren.is-programmer.com/posts/44555.html
'''

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    # 70ms
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        return self.inter_search(A, left, right, target)
        
    def inter_search(self,A, left, right,target):    
        while left <= right:
            mid = (left + right) /2
            if target == A[mid]:
                return True
            if A[mid] > A[left]:
                if target < A[mid] and target >= A[left]:
                    right = mid -1
                else:
                    left = mid+1
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid+1
                else:
                    right = mid -1
            elif A[mid] == A[left] or A[mid] == A[right]:
                 return (self.inter_search(A, left, mid-1, target) or self.inter_search(A, mid+1, right, target))
        return False   
    
    # 57ms
    def search(self,A,target):
        left, right = 0, len(A)-1
        
        while left <= right:
            mid = (left+right)/2
            if A[mid]==target: return True
            if A[mid] > A[left]:
                if A[left]<=target < A[mid]:
                    right = mid -1
                else:
                    left = mid +1
            elif A[mid] < A[left]: 
                # test case: A[mid] < A[right]: [3,1,1], 3; A[mid] <= A[right]:[1,1,3,1], 3
                # A[mid] <= A[left]: [3,1], 1
                if A[mid]<target <= A[right]:  # Here we should check A[right], not the A[left]
                    left= mid +1
                else:
                    right = mid -1
            else:
                left +=1
        return False 
