/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
#include <unordered_map>
class Solution {
public:
    Node* copyRandomList(Node* head) {
        //1. Create the hashmap 
        std::unordered_map<Node*,Node*> hashmap;
        
        //2. Take care of the mappings to the Node 
        Node* current = head;
        
        while(current!=nullptr){
            Node* placeholderNode = new Node(current->val);
            hashmap[current] = placeholderNode;
            current = current->next;
        }
        //3. Copy initialized to stuff inside the hashmap 
        Node* secondCurrent = head;
        
        while (secondCurrent!=nullptr){
            Node* placeholderNode = hashmap[secondCurrent];
            placeholderNode->next = hashmap[secondCurrent->next];
            placeholderNode->random = hashmap[secondCurrent->random];
            secondCurrent = secondCurrent->next;
        }
        //4. Return the new head 
        return hashmap[head];
    }
};