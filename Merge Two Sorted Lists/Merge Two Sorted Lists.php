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
     * @param ListNode $list1
     * @param ListNode $list2
     * @return ListNode
     */
    function mergeTwoLists($list1, $list2) {

        if($list1==null){
            return $list2;
        }
        else if($list2==null){
            return $list1;
        }
        
        $list3 = $head = new ListNode();

        while($list1 != null && $list2 != null){
            if($list1->val<$list2->val){
                $list3->next = new ListNode($list1->val);
                $list1 = $list1->next;
            }
            else{
                $list3->next = new ListNode($list2->val);
                $list2 = $list2->next;
            }
            $list3 = $list3->next;
        }
            
        while($list1 != null){
            $list3->next = new ListNode($list1->val);
            $list1 = $list1->next;
            $list3 = $list3->next;
        }    
        while($list2 != null){
            $list3->next = new ListNode($list2->val);
            $list2 = $list2->next;
            $list3 = $list3->next;
        }
        return $head->next;
    }
}


?>