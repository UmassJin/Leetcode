[G4G] (http://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/#comment-5369)

Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.

Example:

Consider the following SpecialStack
```
16  --> TOP
15
29
19
18
```

When getMin() is called it should return 15, which is the minimum 
element in the current stack. 

If we do pop two times on stack, the stack becomes
```
29  --> TOP
19
18
```
When getMin() is called, it should return 18 which is the minimum 
in the current stack.

```python
# Min Stack 
class MinStack():
    def __init__(self, size):
        self.data_stack = []
        self.min_stack = []
        self.size = size

    def is_full(self):
        return len(self.data_stack) == self.size

    def is_empty(self):
        return not self.data_stack
        
    def push(self, data):
        if self.is_full():
            return False
        self.data_stack.append(data)
        if not self.min_stack or self.min_stack[-1] >= data:
            self.min_stack.append(data)

    def pop(self):
        if self.is_empty():
            return False
        data = self.data_stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def get_min(self):
       if self.min_stack:
           return self.min_stack[-1]

test = MinStack(3)
test.push(5)
test.push(3)
test.push(9)
print test.get_min()
print test.pop()
test.push(1)
print test.get_min()
print test.pop()


```
