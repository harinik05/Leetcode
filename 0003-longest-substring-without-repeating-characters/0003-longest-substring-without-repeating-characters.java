class Solution {
    public int lengthOfLongestSubstring(String s) {
        //1. Output variables
        Set<Character> seen = new HashSet<>();
        int outputResult = 0;
        
        //2. Pointers
        int left = 0;
        int right = 0;
        
        //3. While loop as long as right<length
        while(right<s.length()){
            //a. is it in the seen 
            if (seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left+=1;
                
            }else{
                seen.add(s.charAt(right));
                right+=1;
                outputResult = Math.max(outputResult, right-left);
            }
        }
        return outputResult;
        
    }
}