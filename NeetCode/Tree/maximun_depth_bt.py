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


class Solution(object):
    def max_depth(self, root:TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(19)))

solution = Solution()
print(solution.max_depth(root))
