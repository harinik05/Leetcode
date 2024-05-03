class Solution {
    public int compareVersion(String version1, String version2) {
        //1. Split the array
        String[] firstArr = version1.split("\\.");
        String[] secondArr = version2.split("\\.");
        
        //2. Find the max length
        int maxLength = Math.max(firstArr.length, secondArr.length);
        
        for(int i =0;i<maxLength;i++){
            //a. Determine the strings
            String firstNum = (i<firstArr.length)?firstArr[i]:"0";
            String secondNum = (i<secondArr.length)?secondArr[i]:"0";
            
            //b. Determine the integers (string-> int type)
            int num1 = Integer.valueOf(firstNum);
            int num2 = Integer.valueOf(secondNum);
            
            //c. if num1<num2
            if (num1<num2){
                return -1;
            }
            if (num1>num2){
                return 1;
            }
        }
        return 0;
    }
}