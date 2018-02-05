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

    public static void insert(int data) {
        Node temp = root;
        Queue<Node> q = new LinkedList<Node>();
        q.add(root);
        System.out.println(q.peek());
    }

    public static void main(String[] args) {
        BinaryTree b = new BinaryTree();
        b.root = new Node(10);
        b.insert(1);
    }
}
