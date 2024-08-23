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
    
    //we start off with the Depth first search solution 
    public Node cloneGraph(Node node) {
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