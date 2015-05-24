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
        
        heapq.heapify(heap) # min_heap
        
        while heap:
            cur.next = heapq.heappop(heap)[1]
            cur = cur.next 
            if cur.next:
                heapq.heappush(heap, (cur.next.val, cur.next))
        return dummy.next
            
