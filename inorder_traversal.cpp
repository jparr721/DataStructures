struct node {
	    int data;
	    node* left;
	    node* right;
};

void inOrder(node *root) {
	    if (root == NULL) 
				return;
			    
			inOrder(root->left);
			cout << root->data << " " << flush;
		  inOrder(root->right);
}
