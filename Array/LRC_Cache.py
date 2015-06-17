'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class ListNode:
    def __init__(self, key=None, value = None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # self.hash used to save the parent node
        # self.tail point to the tail of linkedlist
        # self.head point to the head of linkedlist
        # self.tail save the latest used node
        self.hash = {}
        self.head = ListNode()
        self.tail = self.head 
        self.capacity = capacity
    
    def push_back(self, newnode):
        self.hash[newnode.key] = self.tail
        self.tail.next = newnode
        self.tail = self.tail.next 

    def popfront(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        if self.head.next:
            self.hash[self.head.next.key] = self.head

    def kick(self, pre):
        node = pre.next 
        if node == self.tail:
            return
        pre.next = node.next
        if node.next != None:
            self.hash[node.next.key] = pre
            node.next = None
        self.push_back(node)
        
    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.hash:
            newnode = ListNode(key, value)
            self.push_back(newnode)
            if len(self.hash) > self.capacity:
                self.popfront()
        else:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        
