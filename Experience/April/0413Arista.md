#####Give a Linked list and given value, delete all the nodes which have the same value, Use C
Similar questions: [G4G](http://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/)

Given a Singly Linked List, write a function to delete the node which has given value. Your function must follow following constraints:
1) It must accept pointer to the start node as first parameter and node to be deleted as second parameter i.e., pointer to head node is not global.
2) It should not return pointer to the head node.
3) It should not accept pointer to pointer to head node.

You may assume that the Linked List never becomes empty.

```c
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

void deleteNode(struct node *head, int n)
{   
    while (head->data == n)
    {
        if (head->next == NULL)
        {
            printf("there is only one node!");
            return;
        }
        head->data = head->next->data;
        struct node *tmp = head->next;
        head->next = head->next->next;
        free(tmp);
    }

    struct node *prev = head;
    while (prev != NULL)
    {
        while(prev->next != NULL && prev->next->data != n)
        {
            prev = prev->next;
        }
        if (prev->next == NULL)
        {
            printf("Given value does not exist!");
            return;
        }
        struct node *tmp = prev->next;
        prev->next =  prev->next->next;
        free(tmp);
    }
}

/* Utility function to print a linked list */
void printList(struct node *head)
{
    while(head!=NULL)
    {
        printf("%d ",head->data);
        head=head->next;
    }
    printf("\n");
}

/* Driver program to test above functions */
int main()
{
    struct node *head = NULL;

    /* Create following linked list
      12->15->10->11->5->6->2->3 */
    push(&head,3);
    push(&head,2);
    push(&head,6);
    push(&head,5);
    push(&head,2);
    push(&head,10);
    push(&head,12);
    push(&head,12);

    printf("Given Linked List: ");
    printList(head);

    /* Let us delete the node with value 10 */
    printf("\nDeleting node 2 ");
    deleteNode(head, 2);

    printf("\nModified Linked List: ");
    printList(head);

```

* Note:今天面试Arista彻底的被虐了...只要求用c做了一道题...没有做好...:( 加油！再接再厉！！
