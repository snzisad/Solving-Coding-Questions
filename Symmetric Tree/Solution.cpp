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

#include <algorithm>


class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        vector<TreeNode*> parents = {root};
        vector<TreeNode*> childs = {};
        vector<int> test = {};
        vector<int> original_test = {};

        while(!parents.empty()){
            childs.clear();
            test.clear();

            for(int i=0; i<parents.size(); i++){
                if(parents[i]){
                    childs.push_back(parents[i]->left);
                    childs.push_back(parents[i]->right);
                }
            }

            for(int i=0; i<childs.size(); i++){
                if(childs[i]){
                    test.push_back(childs[i]->val);
                }
                else{
                    test.push_back(-101);
                }
            }
            original_test = test;
            reverse(test.begin(),test.end());
            if(test != original_test){
                return false;
            }

            parents = childs;
        }

        return true;
    }
};