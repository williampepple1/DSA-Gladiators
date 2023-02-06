"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true


Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

1. The number of nodes in the tree is in the range [1, 104].
2. -231 <= Node.val <= 231 - 1

Link: https://leetcode.com/problems/validate-binary-search-tree/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return root

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, low, high = stack.pop()

            if low >= node.val or node.val >= high:
                return False

            if node.left:
                stack.append((node.left, low, node.val))
            if node.right:
                stack.append((node.right, node.val, high))

        return True