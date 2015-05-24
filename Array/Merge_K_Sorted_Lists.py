Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists: return None
        dummy = ListNode(0)
        cur = dummy
        heap = []
        heap = [(l.val, l) for l in lists if l]
        # for l in lists:
        #     if l:
        #         heap.append((l.val, l))
        
        heapq.heapify(heap) # min_heap, O(n)
        
        while heap:
            cur.next = heapq.heappop(heap)[1]
            cur = cur.next 
            if cur.next:
                heapq.heappush(heap, (cur.next.val, cur.next)) # 每次插入一个数 O(logn)
        return dummy.next

# Total time complexity:
# Here, the heapiify use O(k), and then insert each number, each one use O(logk), totally use O(nlogk)
# O(k + nlogk)
