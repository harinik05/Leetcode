class Solution {
    //constructor
    public boolean[] visited;
    public Solution(){
        
        //ArrayList<Boolean> visited = new ArrayList<>();
        //Queue<Integer> queue = new Queue<>();
        
    }
    public int findCircleNum(int[][] isConnected) {
        //1. Determine the length (number of cities)
        
        int m = isConnected.length;
        this.visited = new boolean[m];
        int counter = 0;
        //2. For 
        for(int i = 0;i<m;i++){
            if(this.visited[i] == false){
                counter++;
                this.dfs(i, isConnected);
                
            }
        }
        
        return counter;
    }
    
    public void dfs(int i, int[][] isConnected){
        
        //1. Check the necessary conditions 
        if (this.visited[i] == true){
            return;
        }
        
        //2. Process the current cell 
        this.visited[i] = true;
        
        //3. Recursive dfs calls
        for(int k = 0;k<isConnected[i].length;k++){
            //check if the connection exists 
            if(isConnected[i][k] == 1){
                this.dfs(k, isConnected);
            }
        }
        
    }
}