class Solution {
    public int findMaxK(int[] nums) {
        //1. sort the array
        Arrays.sort(nums);
        
        //2. loop through the entire array in backwards order
        for(int i = nums.length-1;i>=0;i--){
            //3. check if the negative version of it is there
            if (nums[i]>0){
                int index = Arrays.binarySearch(nums, nums[i]*-1);
                if (index >=0){
                    return nums[i];
                }
            }else{
                break;
            }
            
        }
        
        return -1;
    }
}