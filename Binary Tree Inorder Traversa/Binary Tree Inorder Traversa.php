<?php

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer[]
     */

    var $result = [];

    function travarse($root){
        if($root != null){
            $this->travarse($root->left);
            array_push($this->result, $root->val);
            $this->travarse($root->right);
        }
    }

    function inorderTraversal($root) {        
        $this->travarse($root);
        return $this->result;
    }

}

?>