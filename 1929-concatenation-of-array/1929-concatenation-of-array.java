class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length*2];
        int counter = 0;
        for(int i=0;i<nums.length;i++){
            ans[counter] = nums[i];
            counter++;
        }
        
        for(int i=0;i<nums.length;i++){
            ans[counter] = nums[i];
            counter++;
        }
        
        return ans;
        
    }
}