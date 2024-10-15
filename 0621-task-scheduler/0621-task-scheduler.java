import java.util.*;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        
        //1. Initialize all the variables 
        Map<Character, Integer> hashmap = new HashMap<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        Queue<int[]> queue = new LinkedList<>();
        int time = 0;
        
        //2. Put everything into the hashmap 
        for(char task: tasks){
            hashmap.put(task,hashmap.getOrDefault(task,0)+1);
        }
        
        //3. Put everything into the maxHeap 
        for(int val: hashmap.values()){
            maxHeap.add(val);
        }
        
        //4. While loop 
        while(!queue.isEmpty() || !maxHeap.isEmpty()){
            //a. Time increment
            time++;
            
            //b. check the heap 
            if(!maxHeap.isEmpty()){
                int largestElement = maxHeap.poll()-1;
                if(largestElement!=0){
                    queue.offer(new int[]{largestElement, time+n});
                }
                
            }
            
            //c. check the queue 
            if(!queue.isEmpty()){
                //int[] queuePopped = queue.poll();
                if(time==queue.peek()[1]){
                    int[] queuePopped = queue.poll();
                    maxHeap.offer(queuePopped[0]);
                }
                
            }
        }
        
        return time;
        
    }      
}
