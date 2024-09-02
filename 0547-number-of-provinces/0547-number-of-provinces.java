class Solution {
    //constructor
    public boolean[] visited;
    public Queue<Integer> queue = new LinkedList<>();
    public Solution(){
        
        //ArrayList<Boolean> visited = new ArrayList<>();
        //Queue<Integer> queue = new Queue<>();
        
    }
    
    public int findCircleNum(int [][] isConnected){
        int m = isConnected.length;
        this.visited = new boolean[m];
        int counter = 0;
        for(int i = 0;i<m;i++){
            if(this.visited[i] == false){
                counter++;
                this.bfs(i, isConnected);
                
            }
        }
        
        return counter;
        
    }
    
    public void bfs(int i, int[][] isConnected){
        //1. Put the first element in the queue 
        this.queue.offer(i);
        this.visited[i] = true;
        
        //2. If the queue is still containing stuff
        while(!this.queue.isEmpty()){
            //a. Pop the first element 
            int firstElem = this.queue.poll();
            
            //b. Loop rhrough the neighbots 
            for(int j = 0;j<isConnected[firstElem].length;j++){
                //1. check if theres connction and its not visited 
                if((isConnected[firstElem][j] == 1) &&(this.visited[j] == false)){
                    this.queue.add(j);
                    this.visited[j] = true;
                }
            }
        }
        
    }
    
    public int findCircleNumDFS(int[][] isConnected) {
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