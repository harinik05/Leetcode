/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        //1. Setup a hashmap to get the nodes in 
        Map<Node, Node> hashmap = new HashMap<>();
        
        //2. Loop through the whole thing and setup the nodes first
        Node current = head;
        while(current!=null){
            Node nodePlaceholder = new Node(current.val);
            hashmap.put(current, nodePlaceholder);
            current = current.next;
        }
        
        //3. Set up those connections for the copy 
        Node currentSecond = head;
        while(currentSecond!=null){
            Node copy = hashmap.get(currentSecond);
            copy.next = hashmap.get(currentSecond.next);
            copy.random = hashmap.get(currentSecond.random);
            currentSecond = currentSecond.next;
        }
        return hashmap.get(head);
        
    }
}