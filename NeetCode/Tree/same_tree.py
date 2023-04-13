'''100. Same Tree - Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

    # # create tree 1
    # p = TreeNode(1)
    # p.left = TreeNode(2)
    # p.right = TreeNode(3)
    #
    # # create tree 2
    # q = TreeNode(1)
    # q.left = TreeNode(2)
    # q.right = TreeNode(3)
    #
    # # check if the trees are the same
    # print(isSameTree(p, q))
    #
    # p1 = TreeNode(1)
    # p1.left = TreeNode(2)
    #
    # # create tree 2
    # q1 = TreeNode(1)
    # q1.right = TreeNode(2)
    #
    # print(isSameTree(p1, q1))
    #
    # p2 = TreeNode(1)
    # p2.left = TreeNode(2)
    # p2.right = TreeNode(1)
    #
    # # create tree 2
    # q2 = TreeNode(1)
    # q2.left = TreeNode(1)
    # q2.right = TreeNode(2)

    print(isSameTree(p2, q2))

    p = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(19)))
    q = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(19)))
    print(isSameTree(p, 1))
