# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# Input: list1 = [], list2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:

    merged_list = ListNode()
    current = merged_list

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    return merged_list.next


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_two_list(l1, l2)

while merged_list:
    print(merged_list.val, end='->')
    merged_list = merged_list.next
