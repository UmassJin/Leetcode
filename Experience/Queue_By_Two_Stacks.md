Implement a Queue by using two stacks. Support O(1) push, pop, top

```python
class Queue():
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, number):
        self.inbox.append(number)

    def pop():
        if not self.outbox:
            while len(self.indox) > 0:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def get_top():
        if not self.outbox:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]

```
