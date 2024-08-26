class Solution {
    public int maxArea(int[] height) {
        //use binary search to do this
        
        int maxOutput = 0;
        
        //1. Initialize the pointers
        int leftPointer = 0;
        int rightPointer = height.length-1;
        
        //2. While loop 
        while(leftPointer<=rightPointer){
            //3. Intialize the max area stuff
            int maxArea = Math.min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer);
            maxOutput = Math.max(maxArea, maxOutput);
            
            if(height[leftPointer] < height[rightPointer]){
                leftPointer++;
            }else{
                rightPointer--;
            }
        }
        
        return maxOutput;
    }
}