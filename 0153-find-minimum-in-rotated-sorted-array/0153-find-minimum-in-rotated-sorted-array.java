class Solution {
    public int findMin(int[] nums) {
        //1. Initialize the pointers 
        int l = 0;
        int r = nums.length-1;
        
        //2. Handle some basic test cases 
        //a. nums.length = 1
        if(nums.length==1){
            return nums[0];
        }
        //b. case 1 - no rotation nums[r]> nums[l]
        if(nums[r]>nums[l]){
            return nums[l];
        }
        
        //3. binary search for the mid pointer 
        while(l<=r){
            //a. mid pointer 
            int mid = (int)((l+r)/2);
            
            //b. validate if its min (inflection idea)
            if(nums[mid]>nums[mid+1]){
                return nums[mid+1];
            }
            else if(nums[mid-1]>nums[mid]){
                return nums[mid];
            }
            
            //c. adjust the mid pointer 
            if(nums[mid]>nums[0]){
                l = mid+1;
            }else{
                r = mid-1;
            }
        }
        return nums[l];
    }
}