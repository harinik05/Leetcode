class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //1. Initilialize the pointers 
        int start = 0;
        int end = people.length-1;
        int counter = 0;
        Arrays.sort(people);
        //2. while loop
        while(start<=end){
            //a. is the limit reached or less
            if(people[start]+people[end]<=limit){
                start++;
                end--;
                
            }
            //b. over exceeded the limit
            else{
                end--;
            }
            counter++;
            
        }
        return counter;
    }
}