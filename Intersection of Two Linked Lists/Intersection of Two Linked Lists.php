<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */

class Solution {
    /**
     * @param ListNode $headA
     * @param ListNode $headB
     * @return ListNode
     */
    
    function getIntersectionNode($headA, $headB) {
        $head1 = $headA;
        $head2 = $headB;
        $shortest = $headA;
        $longest = $headB;
        
        while($head1 != null && $head2 != null){
            $head1 = $head1->next;
            $head2 = $head2->next;
        }
        if($head1 == null){
            $shortest = $headA;
            $longest = $headB;
            
            while($head2 != null){
                $head2 = $head2->next;
                $longest = $longest->next;
            }
        }
        else if($head2 == null){
            $shortest = $headB;
            $longest = $headA;
            
            while($head1 != null){
                $head1 = $head1->next;
                $longest = $longest->next;
            }
        }
        while($shortest != null && $longest != null){
            if($shortest === $longest){
                return $shortest;
            }
            
            $shortest = $shortest->next;
            $longest = $longest->next;
        }

    }

    
    function getIntersectionNode2($headA, $headB) {        
        if (!$headA->val || !$headB->val) return null;

        $a = $headA;
        $b = $headB;
        while ($a !== $b) {
            $a = $a == null ? $headB : $a->next;
            $b = $b == null ? $headA : $b->next;
        }
        return $a;
    }
}

?>