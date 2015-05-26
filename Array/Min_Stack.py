'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.list1 = []
        self.list2 = []
    
    def push(self, x):
        self.list1.append(x)
        if not self.list2 or self.list2[-1] >= x:  # Note, here is >=, test case: push0,push1,push0,getmin,pop,getmin
            self.list2.append(x)
    
    # @return nothing
    def pop(self):
        if self.list1:
            top = self.list1[-1]
            self.list1.pop()
        
            if self.list2 and self.list2[-1] == top: 
                self.list2.pop()

    # @return an integer
    def top(self):
        if self.list1:
            return self.list1[-1]

    # @return an integer
    def getMin(self):
        if self.list2:
            return self.list2[-1]
