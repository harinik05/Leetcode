class Solution(object):
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i!=j and i<j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
    def reverse(self, matrix):
        for i in range(len(matrix)):
            matrix[i].reverse()
    
    #2. Reverse the rows 
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        self.transpose(matrix)
        self.reverse(matrix)
        
        
        
        