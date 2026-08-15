# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if node is None:
                return True

            if not low < node.val < high:
                return False

            left = validate(node.left, low, node.val) #in left side low doesnt change only high changes to the previous parent node
            right = validate(node.right, node.val, high) #in right side low changes to the current minimum and max is the root node 
            return left and right
        return validate(root, float("-inf"), float("inf"))
