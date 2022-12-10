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
     * @return Boolean
     */
    function isSymmetric($root) {
        
        if($root == null) return true;
        
        $parents = [$root];
        while($parents != null){
            $children = [];
            $test = [];

            foreach($parents as $node){
                if($node != null){
                    array_push($children, $node->left, $node->right);
                }
            }

            foreach ($children as $c) {
                if($c != null){
                    array_push($test, $c->val);
                }
                else{
                    array_push($test, " ");
                }
            }

            print_r($test);

            if($test != array_reverse($test)){
                return false;
            }


            $parents = $children;

        }
        return true;
    }
}

?>