class Solution {
    public boolean[][] pBool;
    public boolean[][] aBool;
    public int[][] directions = new int[][]{{-1,0},{1,0},{0,1},{0,-1}};
    public Queue<int[]> pQueue = new LinkedList<>();
    public Queue<int[]> aQueue = new LinkedList<>();
    
    public List<List<Integer>> pacificAtlantic(int[][] heights){
        //1. Intialize the variables 
        int rows = heights.length;
        int cols = heights[0].length;
        
        this.pBool = new boolean[rows][cols];
        this.aBool = new boolean[rows][cols];
        
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                this.pBool[i][j]=false;
                this.aBool[i][j]= false;
            }
        }
        //2. horizontal stuff
        for(int h = 0;h<cols;h++){
            this.BFSFunction(heights, 0, h, true);
            this.BFSFunction(heights, rows-1, h, false);
        }
        
        //3. vertical stuff
        for(int v = 0;v<rows;v++){
            this.BFSFunction(heights, v, 0, true);
            this.BFSFunction(heights, v, cols-1, false);
        }
        
        
        
        //4. Find the overlaps 
        List<List<Integer>> output = new ArrayList<>();
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                if(pBool[i][j] == true && aBool[i][j] == true){
                    output.add(Arrays.asList(i,j));
                }
            }
        }
        
        return output;
    
    }
    
    public void BFSFunction(int[][] heights, int r, int c, boolean oceanFlag){
        //1. Initialize the queue 
        Queue<int[]> queue;
        boolean[][] bArr;
        if (oceanFlag == true){
            queue = pQueue;
            bArr = pBool;
            
        }else{
            queue = aQueue;
            bArr = aBool;
        }
        
        queue.offer(new int[]{r,c});
        bArr[r][c] = true;
        //2. While the queue is not empty (current is popped off)
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            for(int[] direction: this.directions){
                int newRow = current[0]+ direction[0];
                int newCol = current[1]+ direction[1];
                
                if((newRow>=0) &&(newRow<heights.length)&&(newCol>=0) &&(newCol<heights[0].length) &&(heights[current[0]][current[1]]<=heights[newRow][newCol]) &&(bArr[newRow][newCol] == false)){
                    queue.offer(new int[]{newRow,newCol});
                    bArr[newRow][newCol]=true;
                }
            }
        }
        
        //3. Loop through all the directions and check the conditions and add to the queue accoridngly
    }
    public List<List<Integer>> pacificAtlanticBFS(int[][] heights) {
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