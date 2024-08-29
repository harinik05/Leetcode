//Kadane's Algorithm - Optimal Solution
class Solution {
    public int maxSubArray(int[] nums) {
        //1. Initialize the counter variables 
        int maxCounter = Integer.MIN_VALUE;
        int sumCounter = 0;
        
        //2. For loop through nums array 
        for(int number: nums){
            //a. Increment to the sum 
            sumCounter+=number;
            
            //b. maxCounter update its value 
            maxCounter = Math.max(sumCounter, maxCounter);
            
            //c. negative value edge case 
            if (sumCounter<0){
                sumCounter = 0;
            }
        }
        
        return maxCounter;
    }
}