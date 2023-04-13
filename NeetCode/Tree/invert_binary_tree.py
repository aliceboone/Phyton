'''226. Invert Binary Tree - Easy

Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
'''

from typing import List


# Depth first search
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root:TreeNode) -> List[int]:
    if root is None:
        return None

    # swap the childrem
    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root



# Define a sample binary tree
def treeToList(root: TreeNode) -> List[int]:
    if root is None:
        return []
    left_list = treeToList(root.left)
    right_list = treeToList(root.right)
    root.left, root.right = right_list, left_list
    return [root.val] + right_list + left_list


# Example 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_root = invertTree(root)
print(inverted_root)
inverted_list1 = treeToList(inverted_root)
print(inverted_list1)  # prints [4,7,2,9,6,3,1]
print(invertTree(root))

# Example 2
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
inverted_root2 = invertTree(root2)
inverted_list2 = treeToList(inverted_root2)
print(inverted_list2)  # prints [2,3,1]

# Example 3
root3 = None
print(invertTree(root3))  # prints []
