class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //1. Determine rows and cols count
        int noRows = matrix.length;
        int noCols = matrix[0].length;
        
        //2. Do binary search 
        int left = 0;
        int right = noRows * noCols -1;
        
        while (left<=right){
            int pivotIndex = (int)((left + right)/2);
            int pivotElement = matrix[(int)(pivotIndex/noCols)][pivotIndex%noCols];
            
            if(target == pivotElement){
                return true;
            }else{
                if (target<pivotElement){
                    right = pivotIndex-1;
                }else{
                    left = pivotIndex +1;
                }
            }
        }
        
        return false;
    }
}