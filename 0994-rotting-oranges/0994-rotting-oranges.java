class Solution {
    public int ROWS = 0;
        public int COLS = 0;
        public int fresh = 0;
        public int[][] directions = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
        public int[][] gridcpy;
        public Queue<int[]> queue = new LinkedList<>();
        public int returnValue = 0;
    public Solution(){
        
        
    }
    public int orangesRotting(int[][] grid) {
        //1. Initialize the grid values 
        this.ROWS = grid.length;
        this.COLS = grid[0].length;
        this.gridcpy = grid;
        //2. For loop 
        for(int r = 0;r<this.ROWS;r++){
            for(int c = 0;c<this.COLS;c++){
                if(grid[r][c] == 2){
                    this.queue.offer(new int[]{r,c});
                }
                else if(grid[r][c]==1){
                    this.fresh++;
                }
            }
        }
        
        //3. Call BFS function 
        this.bfs();
    
        return this.fresh==0?this.returnValue:-1;
        
    }
    
    public void bfs(){
        //1. Initialize values in q = DONE
        //2. 9While queue
        while((!this.queue.isEmpty()) && (this.fresh>0)){
            //loop for the level 
            this.returnValue++;
            int size = this.queue.size();
            for(int i=0;i<size;i++){
                //1. Pop the first element 
                int[] current = this.queue.poll();
                //2. loop throguh the neighbors
                for(int[] arr: this.directions){
                    int newR = current[0] + arr[0];
                    int newC = current[1] + arr[1];
                    
                    //3. check the boundaries 
                    if((newR>=0)&&(newR<this.ROWS)&&(newC>=0)&&(newC<this.COLS)){
                        if(this.gridcpy[newR][newC] == 1){
                            this.gridcpy[newR][newC] = 2;
                            this.queue.offer(new int[]{newR,newC});
                            this.fresh--;
                        }
                    }
                }
            }
        }
    }
    
}