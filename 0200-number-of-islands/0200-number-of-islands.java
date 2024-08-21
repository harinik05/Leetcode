class Solution {
    public Queue<int[]> queue = new LinkedList<>();
    public int[][] directions = new int[][]{{1,0}, {0,1}, {-1,0}, {0,-1}};
    
    public int numIslands(char[][] grid){
        //1. Counter
        int counter = 0;
        
        //2. for loop 
        for(int i = 0;i<grid.length;i++){
            for(int j = 0;j<grid[0].length;j++){
                if(grid[i][j] == '1'){
                    this.BFSFunction(grid, i, j);
                    counter++;
                }
                
            }
        }
        return counter;
    }
    
    public void BFSFunction(char[][] grid, int r, int c){
        //1. Put something in the queue 
        //this.queue.clear();

        int[] currentElem = {r,c};
        this.queue.offer(new int[]{r,c});
        grid[r][c] = '0';
        
        //2. While in the queue, pop for gettting current 
        while(!queue.isEmpty()){
            int[] popped = this.queue.poll();
            
            //3. For loop of directions
            for(int[] arr: this.directions){
                int newRow = popped[0] + arr[0];
                int newCol = popped[1] + arr[1];
                //4. check conditions and append to the queue if it works 
                if((newRow>=0) && (newRow<grid.length) && (newCol>=0) && (newCol<grid[0].length) && (grid[newRow][newCol] == '1')){
                    this.queue.offer(new int[]{newRow, newCol});
                    grid[newRow][newCol] = '0';
                    
                }
            }
        }
        
        
        
    }
    public int numIslandsDFS(char[][] grid) {
        int numOfIslands = 0;
        
        if((grid==null) || (grid.length== 0)){
            return 0;
        }
        for(int i = 0;i<grid.length;i++){
            for(int j = 0;j<grid[0].length;j++){
                if(grid[i][j] == '1'){
                    DFSFunction(grid, i, j);
                    numOfIslands++;
                }
                
            }
        }
        
        return numOfIslands;
        
    }
    
    public void DFSFunction(char[][] grid, int r, int c){
        //1. Check all necessary conditions
        if((r<0)||(r>=grid.length)||(c<0)||(c>=grid[0].length)){
            return;
        }
        if(grid[r][c] == '0'){
            return;
        }
        
        //2. Process the cell
        grid[r][c] = '0';
        
        //3. Call DFS as needed (recursion)
        this.DFSFunction(grid, r+1, c);
        this.DFSFunction(grid, r-1, c);
        this.DFSFunction(grid, r, c+1);
        this.DFSFunction(grid, r, c-1);
    }
    
    
}