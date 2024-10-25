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
    void reorderList(ListNode* head) {
        //1. Get the middle of the linked list 
        ListNode* slow = head;
        ListNode* fast = head;

        //2. Loop through the whole thing 
        while((fast!=nullptr) &&(fast->next!=nullptr)){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* secondHalf = slow;
        ListNode* prev = nullptr;
        //3. Get the reversed version of the second half 
        while(secondHalf!=nullptr){
            ListNode* buffer = secondHalf->next;
            secondHalf->next = prev;
            prev = secondHalf;
            secondHalf = buffer;
        }
        ListNode* reversedSecondHalf = prev;

        //4. Add stuff
        int counter = 1;
        ListNode* original = head;
        ListNode* resultNode = new ListNode(-1);
        ListNode* returnResult = resultNode;

        while((original!=nullptr) && (reversedSecondHalf!=nullptr)){
            if(counter%2==0){
                returnResult->next = reversedSecondHalf;
                reversedSecondHalf = reversedSecondHalf->next;
            }else{
                returnResult->next = original;
                original = original->next;
            }
            counter+=1;
            returnResult = returnResult->next;

        }

        head = resultNode->next;
    }
};