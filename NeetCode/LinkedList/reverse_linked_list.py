"""206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

 A linked list can be reversed either iteratively or recursively. Could you implement both?"""


# Interative
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iteratively(head: ListNode) -> ListNode:
    prev = None
    current = head

    if not head:
        return None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_list_iteratively(head)

while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next


# # Recursive
def reverse_list_recursive(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    new_head = head
    if head.next:
        new_head = self(head.next)
        head.next.next = head
    head.next = None
    return new_head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_list_recursive(head)

while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
