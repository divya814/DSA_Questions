#include <iostream>
using namespace std;

struct Node{
    int data;
    Node *right;
    Node *left;
    Node(int val){
        data=val;
        right=NULL;
        left=NULL;
    }
};
// For subtree
void PrintNodes(Node *root, int k){
    if(root==NULL || k<0){
        return;
    }
    if(k==0){
        cout<<root->data<<" ";
        return;
    }
    PrintNodes(root->left,k-1);
    PrintNodes(root->right,k-1);
}
// for ancestors as well
int findNodesatDist(Node *root, Node * target, int k){
    if(root==NULL){
        return -1;   //we are returning if we found our target node or not
    }
    if(root==target){
        PrintNodes(root,k);
        return 0;
    }
    // Find target node in left subtree of root
    int dleft=findNodesatDist(root->left,target,k);
    // if found
    if(dleft!=-1){
        if (dleft+1==k){
            cout<<root->data<<" ";
        }
        // if key k distance from root is not found in left subtree
        // then root becomes our ancestor
        else{
            PrintNodes(root->right,k-dleft-2);
        }
        return dleft+1;
    }
    
    // Find target node in right subtree of root
    int dright=findNodesatDist(root->right,target,k);
    // if found
    if(dright!=-1){
        if (dright+1==k){
            cout<<root->data<<" ";
        }
        // if key k distance from root is not found in right subtree
        // then root becomes our ancestor
        else{
            PrintNodes(root->left,k-dright-2);
        }
        return dright+1;
    }
    return -1;
}

int main() {
	Node * root=new Node(1);
	root->left=new Node(2);
	root->right=new Node(3);
	root->left->left=new Node(4);
	findNodesatDist(root,root->left,1);
	return 0;
}
