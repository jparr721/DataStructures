import java.util.*;

public class BinaryTree {

    private static Node root;
    int size;

    static class Node {
        int data;
        Node left;
        Node right;

        public Node(int data) {
            this.data = data;
            left = null;
            right = null;
        }
    }

    public  BinaryTree() {
        size = 0;
        root = null;
    }

    public static boolean empty() {
        return root == null;
    }

    private static void inorderTraversal(Node root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.data + " ");
            inorderTraversal(root.right);
        }
    }

    private static void postorderTraversal(Node root) {
        if (root != null) {
            postorderTraversal(root.left);
            postorderTraversal(root.right);
            System.out.println(root.data + " ");
        }
    }

    public static void insert(int data) {
        Node temp = root;
        Queue<Node> q = new LinkedList<Node>();
        q.add(root);

        while (!q.isEmpty()) {
            temp = q.peek();
            q.remove();

            if (temp.left == null) {
                temp.left = new Node(data);
                break;
            } else {
                q.add(temp.left);
            }

            if (temp.right == null) {
                temp.right = new Node(data);
                break;
            } else {
                q.add(temp.right);
            }
        }
    }


    public static void main(String[] args) {
        root = new Node(10);
        root.left = new Node(12);
        root.left.left = new Node(8);
        root.right = new Node(13);
        root.right.right = new Node(22);
        root.right.left = new Node(16);

        System.out.println("Before insertion");
        inorderTraversal(root);

        insert(18);
        System.out.println("\nAfter insertion");
        inorderTraversal(root);
    }
}
