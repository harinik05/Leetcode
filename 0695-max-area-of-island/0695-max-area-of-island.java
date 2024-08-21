class Solution {
    public int currentArea = 0;
    Queue<int[]> queue = new LinkedList<>();
    Queue<int[]> DFSqueue = new LinkedList<>();
    public int[][] directions = new int[][]{{1,0},{0,1},{-1,0}, {0,-1}};

    public int DFSArea = 0;
    public int maxAreaOfIsland(int[][] grid){
        int maxArea = 0;
        //1. go through all elements and call BFS
        for(int i = 0;i<grid.length;i++){
            for(int j= 0;j<grid[0].length;j++){
                if(grid[i][j] == 1){
                    this.DFSArea = 0;
                    this.BFSFunction(grid, i, j);
                    maxArea = Math.max(maxArea, this.DFSArea);
                    
                }
            }
        }
        return maxArea;
        
    }
    
    public void BFSFunction(int[][] grid, int r, int c){
        //1. Put some stuff in the queue 
        DFSqueue.offer(new int[]{r,c});
        grid[r][c] = 0;
        this.DFSArea++;
        //2. While queue isnt empty, pop the element 
        while(!this.DFSqueue.isEmpty()){
            int[] current = this.DFSqueue.poll();
            for(int[] direction: this.directions){
                int newR = current[0]+ direction[0];
                int newC = current[1] + direction[1];
                
                if((newR>=0) && (newC>=0) &&(newR<grid.length) &&(newC<grid[0].length)&& (grid[newR][newC] == 1)){
                    this.DFSqueue.offer(new int[]{newR,newC});
                    grid[newR][newC] = 0;
                    this.DFSArea++;
                }
            }
        }
        //3. Loop through all the directions and queue (append if valid )
    }
    public int maxAreaOfIslandDFS(int[][] grid) {
        //1. Initiate the maximum counter 
        int maxOutput = 0;
        for(int i = 0;i<grid.length;i++){
            for(int j = 0;j<grid[0].length;j++){
                if(grid[i][j] == 1){
                    this.currentArea = 0;
                    this.DFSFunction(grid, i, j);
                    maxOutput = Math.max(maxOutput, this.currentArea);
                    
                }
            }
        }
        return maxOutput;
    }
    
    public void DFSFunction(int[][] grid, int r, int c){
        //1. Check all necessary conditions
        if((r<0) || (r>=grid.length) || (c<0) ||(c>=grid[0].length)){
            return;
        }
        if(grid[r][c]==0){
            return;
        }
        //2. Process the cell
        grid[r][c] = 0;
        this.currentArea+=1;
        
        //3. Call the DFS as needed
        this.DFSFunction(grid, r+1, c);
        this.DFSFunction(grid, r-1, c);
        this.DFSFunction(grid, r, c+1);
        this.DFSFunction(grid, r, c-1);
    }
}