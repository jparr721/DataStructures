struct node {
	int data;
	node* left;
	node* right;
};

void postOrder(node* root) {
	if (root == NULL)
		return;

	postOrder(root->left);
	postOrder(root->right);
	cout << root->data << " " << flush;
}
