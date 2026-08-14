# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None: #to check if both root are null, both none
                return True
            elif p is None or q is None: # one of them is none
                return False

            if p.val != q.val: # value of p and q root
                return False
            
            left_tree = self.isSameTree(p.left, q.left) #recursive call to left tree
            right_tree = self.isSameTree(p.right, q.right) #recursive call to right 

            if left_tree is True and right_tree and True: 
                return True
            else:
                return False
            
            #left_tree and right_tree give boolean values true or false

            
            
