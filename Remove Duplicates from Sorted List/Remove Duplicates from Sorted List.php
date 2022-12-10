<?php

//  Definition for a singly-linked list.
class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function deleteDuplicates($head) {
        $items = [];
        $new_head = $prev_item = new ListNode();

        while($head != null){
            if(count($items) == 0 || !in_array($head->val, $items)){
                array_push($items, $head->val);
                $prev_item->next = new ListNode($head->val);
                $prev_item = $prev_item->next;
            }
            $head = $head->next;
        }
        return $new_head->next;
    }
}

?>