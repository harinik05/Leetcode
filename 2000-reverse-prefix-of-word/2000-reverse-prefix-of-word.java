public class Solution {
    public String reversePrefix(String word, char ch) {
        
        
        
        //1. Determine the index of the particular array
        int index = word.indexOf(ch);
        if(index == -1){
            return word;
        }
        
        //2. stringbuildef
        StringBuilder resultSB = new StringBuilder();
        
        for(int i = 0;i<word.length();i++){
            if(i<=index){
                resultSB.append(word.charAt(i));
                if(i == index){
                    resultSB.reverse();
                }
            }
            else{
                resultSB.append(word.charAt(i));
            }
        }
        
        //3. return the answer
        return resultSB.toString();
        
    }
}