class Solution {
    //a. Some variable initializations here
    public Queue<int[]> queue = new LinkedList<>();
    public int ROWS = 0;
    public int COLS = 0;
    
    public int[][] directions = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
    public void wallsAndGates(int[][] rooms) {
        //1. Initialize the variables 
        this.ROWS = rooms.length;
        this.COLS = rooms[0].length;
        
        //2. For loop 
        for(int r = 0;r<this.ROWS;r++){
            for(int c = 0;c<this.COLS;c++){
                //a. find if its a gate then put in queue
                if(rooms[r][c] == 0){
                    this.queue.offer(new int[]{r,c});
                }
            }
        }
        
        //3. call the bfs function
        this.bfs(rooms);
        
        //4. no return
    }
    
    public void bfs(int[][] rooms){
        //1. Initialize the queue with some stuff (not needed)
        //2. While queue 
        while(!this.queue.isEmpty()){
            //a. Pop the first element 
            
            int[] current= this.queue.poll();
            int dist = rooms[current[0]][current[1]];
            //b. loop through all directions 
            for(int[] direction: this.directions){
                //c. update the values 
                int newR = current[0] + direction[0];
                int newC = current[1]+ direction[1];
                
                //d. check the conditoin 
                if((newR>=0) &&(newR<this.ROWS) &&(newC>=0)&&(newC<this.COLS) && (rooms[newR][newC] == 2147483647)){
                    rooms[newR][newC] = dist+1;
                    this.queue.offer(new int[]{newR, newC});
                    
                    
                }
            }
        }
    }
}