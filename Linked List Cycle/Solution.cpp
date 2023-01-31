/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(!head || !head->next || !head->next->next){
            return false;
        }
        auto walker = head, runner = head;

        while(walker->next && runner->next && runner->next->next){
            walker = walker->next;
            runner = runner->next->next;
            if(walker == runner) return true;
        }

        return false;
    }
};