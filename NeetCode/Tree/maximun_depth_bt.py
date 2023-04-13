'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    print(left_depth)
    right_depth = max_depth(root.right)
    print(right_depth)
    return max(left_depth, right_depth) + 1


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(19)))
# tree = TreeNode(3)
# tree.left = TreeNode(9)
# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)
print(max_depth(tree))
