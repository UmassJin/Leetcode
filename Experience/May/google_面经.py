http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=135449&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311

两个链表 求最大的公共后缀

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_max_postfix(head1, head2):
    if not head1 or not head2: return None
    head1 = reverse_linkedlist(head1)
    head2 = reverse_linkedlist(head2)
    dummy = ListNode(0)
    result = dummy

    while head1 and head2:
        if head1.value == head2.value:
            tmp = head1.next  # Note bug here, we need to save the tmp, otherwise, head1.next will become None ! 
            result.next = head1
            result = result.next
            result.next = None 
            
            head1 = tmp
            head2 = head2.next
        else:
            break
    
    return dummy.next
    
def reverse_linkedlist(head1):
    pre = None
    cur = head1
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur 
        cur = next
    return pre

def print_list(head):
    while head:
        print "head.val: ", head.value
        head = head.next 

