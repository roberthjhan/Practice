'''
Given the root node of a binary search tree (BST) and a
value to be inserted into the tree, insert the value into
the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the
original BST.

Note that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can
return any of them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val) # Empty tree

        if val > root.val: # Value is greater than the root
            if root.right:  # Child already exists move to next level
                self.insertIntoBST(root.right, val)
            else:  # Child does not exist
                root.right = TreeNode(val)

        else: # Value is less than the root
            if root.left:  # Child already exists move to next level
                self.insertIntoBST(root.left, val)
            else:  # Child does not exist
                root.left = TreeNode(val)

        return root