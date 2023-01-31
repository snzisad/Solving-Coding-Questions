/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        return maxHeight(root)+1;
    }
    
    int maxHeight(TreeNode* root){
        int left = 0, right = 0;

        if(root->left){
            left = 1+maxHeight(root->left);
        }
        if(root->right){
            right = 1+maxHeight(root->right);
        }
        if(!root->left && !root->right) return 0;

        return max(left, right);
    }
};