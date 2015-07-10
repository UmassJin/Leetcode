# reference: http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
'''
Similar to balancing BST in Method 2 above, we can use a max heap on left side to represent elements 
that are less than effective median, and a min heap on right side to represent elements that are greater 
than effective median.
'''

import heapq

class MaxHeap:
    def __init__(self):
        self.max_heap_size = 0
        self.maxheap = []

    def insert(self, key):
        self.maxheap.append(key)
        n = len(self.maxheap)
        self.max_heap_size = n
        if n == 1:
            return
        else:
            first = n // 2 - 1
            for i in xrange(first, -1, -1):
                self.heapify(self.maxheap, i, n)

    def heapify(self, array, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child >= end: break
            if child + 1 < end and array[child+1] > array[child]:
                child = child + 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break

    def gettop(self):
        if self.maxheap:
            return self.maxheap[0]
        else:
            return 0
    def poptop(self):
        if self.maxheap:
            value = self.maxheap.pop(0)
            self.max_heap_size -= 1
            if self.max_heap_size > 0:
                self.heapify(self.maxheap, 0, self.max_heap_size)
            return value
class MinHeap:
    def __init__(self):
        self.min_heap_size = 0
        self.minheap = []

    def insert(self, key):
        self.minheap.append(key)
        heapq.heapify(self.minheap)
        self.min_heap_size += 1

    def gettop(self):
        if self.minheap:
            return self.minheap[0]
        else:
            return 0

    def poptop(self):
        if self.minheap:
            value = self.minheap.pop(0)
            self.min_heap_size -= 1
            if self.min_heap_size > 0:
                heapq.heapify(self.minheap)
            return value

class Solution:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def getmedian(self, e, m):
        value = self.min_heap.min_heap_size - self.max_heap.max_heap_size
        if value == 0:
            if e > m:
                self.min_heap.insert(e)
                m = self.min_heap.gettop()
            else:
                self.max_heap.insert(e)
                m = self.max_heap.gettop()


        elif value > 0:
            if e < m:
                self.max_heap.insert(e)
            else:
                value = self.min_heap.poptop()
                self.max_heap.insert(value)
                self.min_heap.insert(e)

            m = (self.min_heap.gettop() + self.max_heap.gettop())/2

        elif value < 0:
            if e > m:
                self.min_heap.insert(e)
            else:
                value = self.max_heap.poptop()
                self.min_heap.insert(value)
                self.max_heap.insert(e)

            m = (self.min_heap.gettop() + self.max_heap.gettop())/2
        return m

if __name__ == "__main__":
    test = Solution()
    arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    m = 0
    for i in xrange(len(arr)):
        m = test.getmedian(arr[i], m)
        print "m: ", m
                     

# Time complexiy: O(nlogn)
