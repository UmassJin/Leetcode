Given a linked list where every node represents a linked list and contains two pointers of its type: 

(i) Pointer to next node in the main list (we call it ‘right’ pointer in below code) 

(ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code). 
All linked lists are sorted. See the following example

``` 
       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
```

```python
class Node():
    def __init__(self, data):                
        self.right = None                    
        self.down = None                            
        self.data = data

def merge(node1, node2):
    if not node1 and node2:
        return node2
    if not node2 and node1:
        return node1
    
    if node1.data < node2.data:
        head = node1
        head.down = merge(node1.down, node2) # use the merge here
    
    else:
        head = node2
        head.down = merge(node1, node2.down)
    return head
    
def flatten(root):    
    if not root or not root.right:
        return root
    flatten(root, flatten(root.right))
    # flatten from the tail of the list 


```
