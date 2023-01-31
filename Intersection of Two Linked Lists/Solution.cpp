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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        auto head1 = headA, head2 = headB;
        auto shortest = headA, longest = headB;

        while(head1 && head2){
            head1 = head1->next;
            head2 = head2->next;
        }

        if(!head1){
            shortest = headA;
            longest = headB;

            while(head2){
                head2 = head2->next;
                longest = longest->next;
            }
        }
        else if(!head2){
            shortest = headB;
            longest = headA;

            while(head1){
                head1 = head1->next;
                longest = longest->next;
            }
        }


        while(shortest && longest){
            if(shortest == longest) return shortest;

            shortest = shortest->next;
            longest = longest->next;
        }

        return longest;
    }
};