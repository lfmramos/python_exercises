"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
"""
### Definition for a binary tree node.
### class TreeNode:
###     def __init__(self, val=0, left=None, right=None):
###         self.val = val
###         self.left = left
###         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Dictionary to store the subtrees and their frequencies
        subtrees = {}
        
        # List to store the duplicate subtrees
        duplicates = []
        
        # Helper function to serialize the subtrees
        def serialize(node):
            if not node:
                return '#'
            
            # Serialize the left and right subtrees
            left = serialize(node.left)
            right = serialize(node.right)
            
            # Serialize the current node
            subtree = f'{node.val},{left},{right}'
            
            # Add the subtree to the dictionary
            subtrees[subtree] = subtrees.get(subtree, 0) + 1
            
            # Add the duplicate subtrees to the list
            if subtrees[subtree] == 2:
                duplicates.append(node)
            
            return subtree
        
        # Serialize the root node
        serialize(root)
        
        return duplicates
