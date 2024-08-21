class Solution {
    public boolean[][] pBool;
    public boolean[][] aBool;
    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;
        this.pBool = new boolean[rows][cols];
        this.aBool = new boolean[rows][cols];
        
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                pBool[i][j] = false;
                aBool[i][j] = false;
            }
        }
        //1. Horizontal Stuff
        for(int h = 0;h<cols;h++){
            this.DFSFunction(heights, 0, h, true);
            this.DFSFunction(heights, rows-1, h, false);
     
        }
        //2. Vertical Stuff
        for(int v=0;v<rows;v++){
            this.DFSFunction(heights, v, 0, true);
            this.DFSFunction(heights, v, cols-1, false);
            
        }
        //3. DFS/BFS Stuff when needed
        List<List<Integer>> output = new ArrayList<>();
        
        //4. Grid loop and find all the overlap of oceans
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                if((pBool[i][j] == true) && (aBool[i][j]== true)){
                    output.add(Arrays.asList(i,j));
                }
            }
        }
        return output;
        
        
    }
    
    public void DFSFunction(int[][] heights, int r, int c, boolean oceanFlag ){
        //Boolean flag thing
        boolean[][] bBool;
        if (oceanFlag == true){
            bBool = pBool;
        }else{
            bBool = aBool;
        }
        
        //1. Check all necessary conditions
        if((r<0) || (c<0) || (r>=heights.length) ||(c>=heights[0].length)){
            return;
        }
  
        if(bBool[r][c] == true){
            return;
        }
        //2. Process the cell
        bBool[r][c] = true;
        
        //3. Call DFS as needed (recursive call)
        if(r+1<heights.length && heights[r+1][c]>=heights[r][c]){
            this.DFSFunction(heights, r+1, c, oceanFlag);
        }
        
        if(r-1>=0 && heights[r-1][c] >=heights[r][c]){
            this.DFSFunction(heights, r-1, c, oceanFlag);
        }
        
        if(c+1<heights[0].length && heights[r][c+1] >= heights[r][c]){
            this.DFSFunction(heights, r, c+1, oceanFlag);
        }
        
        if(c-1>=0 && heights[r][c-1]>=heights[r][c]){
            this.DFSFunction(heights, r, c-1, oceanFlag);
        }
        
    }
}