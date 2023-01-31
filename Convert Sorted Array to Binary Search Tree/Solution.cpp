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
    TreeNode* sortedArrayToBST(vector<int>& a) {
        return dfs(a.begin(), a.end());
    }
    
    TreeNode* dfs(vector<int>::iterator i, vector<int>::iterator j) {
        if (i == j) return nullptr;
        auto mid = i + (j-i)/2;
        auto r = new TreeNode(*mid);
        r->left = dfs(i, mid), r->right = dfs(mid+1, j);
        return r;
    }
};