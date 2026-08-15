# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(p,q):
            if not p and not q:
                return True

            if (p and not q) or (not p and q):
                return False
            
            if p.val != q.val:
                return False
            
            return sametree(p.left, q.left) and sametree(p.right, q.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if sametree(root, subRoot):
                return True
            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)
        
        
        

            
    
        
        

            