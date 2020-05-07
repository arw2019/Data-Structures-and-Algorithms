/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) {
            TreeNode* tmp = p;
            p = q;
            q = tmp;
        }
        while (root->val < p->val || root->val > q->val){
            cout << root->val << endl;
            while(root->val < p->val) {root=root->right; cout << root->val << endl;}
            while(root->val > q->val) {root=root->left; cout << root->val << endl;}
        }
        return root;
    }
};
