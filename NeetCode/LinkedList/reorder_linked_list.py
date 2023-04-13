'''143. Reorder List - Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3] '''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of the linked list
    prev, curr = None, slow.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    slow.next = None

    # merge the first and second halves of the linked list alternatively
    p1, p2 = head, prev
    while p2:
        temp1 = p1.next
        temp2 = p2.next
        p1.next = p2
        p2.next = temp1
        p1 = temp1
        p2 = temp2


# Test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorderList(head)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next

