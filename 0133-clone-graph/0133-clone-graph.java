/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    
    public Map<Node, Node> hashmap = new HashMap<>();
    public Queue<Node> queue = new LinkedList<>();
    
    //We'll then do the breath first search solution 
    public Node cloneGraph(Node node){
        if(node == null){
            return null;
        }
        return this.BFSFunction(node);
    }
    
    public Node BFSFunction(Node node){
        //1. Put something in the queue 
        this.queue.add(node);
        Node duplicateNode = new Node(node.val);
        this.hashmap.put(node, duplicateNode );
        
        //2. While the queue is not emoty 
        while(!this.queue.isEmpty()){
            //3. Current 
            Node current = this.queue.poll();
            
            //4. Go through the neighbors 
            for(Node neighbors: current.neighbors){
                //check the condition 
                if(!this.hashmap.containsKey(neighbors)){
                    Node nDuplicate = new Node(neighbors.val);
                    this.hashmap.put(neighbors, nDuplicate);
                    this.queue.add(neighbors);
                    
                }
                //you have to add things to the hashmap neighbors no matter what 
                this.hashmap.get(current).neighbors.add(this.hashmap.get(neighbors));
            }
            
        }
        return this.hashmap.get(node);
        
    }
    //we start off with the Depth first search solution 
    public Node cloneGraphDFS(Node node) {
        if(node == null){
            return null;
        }
        return this.DFSFunction(node);
    }
    
    public Node DFSFunction(Node node){
       //1. Check the necessary conditions 
        if(this.hashmap.containsKey(node)){
            return this.hashmap.get(node);
        }
        
        //2. Process the cell 
        Node clonedNode = new Node(node.val);
        this.hashmap.put(node,clonedNode );
        
        //3. Recusrive DFS Calls 
        for(Node neighbors: node.neighbors){
            clonedNode.neighbors.add(this.DFSFunction(neighbors));
            //this.hashmap.put(node, this.DFSFunction(neighbors));
        }
        
        return clonedNode;
    }
}