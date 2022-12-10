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
     * @return Integer
     */

    function max_height($root){
        $left = 0;
        $right = 0;

        if($root->left != null){
            $left = 1+max_height($root->left);
        }
        if($root->right != null){
            $right = 1+max_height($root->right);
        }
        if($root->left == null && $root->right == null){
            return 0;
        }

        return max($left, $right);
    }

    function maxDepth($root) {

        if($root==null){
            return 0;
        }
        return $this->max_height($root) + 1;
    }
}

?>