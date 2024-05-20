# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memoTable = {}
    def helperBST(self, start, end):
        resultArr = []
        #base case if start > end
        if start>end:
            return [None]
        if (start,end) in self.memoTable.keys():
            return self.memoTable[(start,end)]
        
        # for i 
        for i in range(start, end+1,1):
            leftTrees = self.helperBST(start,i-1)
            rightTrees = self.helperBST(i+1,end)
            
            # loop through left and right
            for l in leftTrees:
                for r in rightTrees:
                    rootNode = TreeNode(i,l,r)
                    resultArr.append(rootNode)
        self.memoTable[(start,end)] = resultArr
        return resultArr
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helperBST(1,n)
        
        