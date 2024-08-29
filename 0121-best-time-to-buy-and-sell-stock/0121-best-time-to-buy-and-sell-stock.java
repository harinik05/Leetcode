class Solution {
    public int maxProfit(int[] prices) {
        //1. Initialize the variables (current and max)
        int currentMin = Integer.MAX_VALUE;
        int maxProfit = 0;
        
        //2. for prices 
        for(int price:prices){
            //a. process the current value 
            currentMin = Math.min(currentMin, price);
            
            //b. current profit 
            int profit = price-currentMin;
            
            //c. Max profit 
            maxProfit = Math.max(profit, maxProfit);
        }
        
        return maxProfit;
    }
}