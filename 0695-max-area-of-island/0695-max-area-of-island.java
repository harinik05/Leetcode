class Solution {
    public int currentArea = 0;
    public int maxAreaOfIsland(int[][] grid) {
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