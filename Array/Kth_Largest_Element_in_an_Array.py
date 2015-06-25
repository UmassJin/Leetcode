Find the kth largest element in an unsorted array.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.



class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        self.build_heap(nums, k)
        length = len(nums)
        for p in xrange(k + 1, length):
            if nums[p] > nums[0]:
                nums[p], nums[0] = nums[0], nums[p]
                self.build_heap(nums, k)
        return nums[0]

    def build_heap(self, nums, k):
        n = k
        first = k//2 -1
        for i in xrange(first, -1, -1):
            self.min_heapify(nums, i, n)
        
    def min_heapify(self, nums, start, end):
        root = start 
        while True:
            child = root * 2 + 1
            if child >= end: break
            if child + 1 < end and nums[child] > nums[child+1]:
                child = child + 1
            if nums[root] > nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child 
            else:
                break

# Time Complexity: O(k + (n-k)Logk)            
