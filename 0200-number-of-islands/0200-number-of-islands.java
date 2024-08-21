//1. Depth First Search Solution
class Solution {
   
    public int numIslands(char[][] grid) {
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