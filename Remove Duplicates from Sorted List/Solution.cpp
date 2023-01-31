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
    ListNode* deleteDuplicates(ListNode* head) {
        set<int> items = {};
        ListNode* prev_item = new ListNode();
        ListNode* new_head = prev_item;

        while(head != nullptr){
            if(items.count(head->val) == 0){
                items.insert(head->val);
                prev_item->next = new ListNode(head->val);
                prev_item = prev_item->next;
            }

            head = head->next;
        }

        return new_head->next;
    }
};