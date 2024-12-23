# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Base cases
        
        if p==None and q==None:
            return True 
        elif p == None or q==None:
            return False 
        elif p.val != q.val:
            return False 
        
        #check the left and right 
        leftProposition = self.isSameTree(p.left, q.left)
        rightProposition = self.isSameTree(p.right, q.right)
        
        return leftProposition and rightProposition
        
        