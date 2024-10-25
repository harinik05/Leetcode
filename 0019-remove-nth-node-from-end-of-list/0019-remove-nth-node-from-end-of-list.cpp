/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    //function to retrieve the length 
    int getLength(ListNode* head){
        int length = 0;
        ListNode* current= head;
        while (current!= nullptr){
            length+=1;
            current = current->next;
        }
        return length;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        //1. Get the length first
        //2. Establish the counter 

        int totalLength = this->getLength(head);
        int counter = 0;

        //1. Check if there is a head or if n exeeds the length 
        if((head == nullptr) || (totalLength<n)){
            return nullptr;
        }

        //2. Check if the head is the one we need to detele
        if(totalLength == n){
            ListNode* current = head;
            head = current->next;
            return head;
        }

        ListNode* current = head;
        ListNode* previous = nullptr;
        while(current!=nullptr){
            if(totalLength-counter == n){
                previous->next =current->next;
            }
            else{
                previous = current;
                current= current->next;
            }
            counter+=1;
            
        }

        return head;
    }
};