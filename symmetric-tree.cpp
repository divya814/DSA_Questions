// https://leetcode.com/problems/symmetric-tree

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
    
    bool identical(TreeNode * p , TreeNode *q){
        if (p==nullptr || q==nullptr){
            return p==q;
        }
        bool cond1=p->val==q->val;
        bool cond2=identical(p->left,q->right);
        bool cond3=identical(p->right,q->left);
        if(cond1 && cond2 && cond3){
            return true;
        }
        return false;
    }
    
    bool isSymmetric(TreeNode* root) {
        return identical(root->left,root->right);
        
    }
};
