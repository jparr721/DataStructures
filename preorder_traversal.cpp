/** 
	This is a hackerrank problem
	**/

struct node {
	int data ;
	node* left;
	node* right;
};

void preOrder(node *root){
	if (root == NULL)
		return;

	cout << root->data << " " << flush;
	preOrder(root->left);
	preOrder(root->right);
}

// fucking magic

