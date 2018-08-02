import java.util.*;
/**
  * This class returns the k-to-last element
  * in a linked list.
  * Example: k = 4
  * 5-->5-->9-->10-->7-->4-->1-->END   
  * Output = 9
  */

public class KtoLast {
	public Node head;

	public class Node {
		int data;
		Node next;

		public Node(int nodeData){
			data = nodeData;
		}
	}
	public void insert(int data) {
		if (head == null) {
			head = new Node(data);
		} else {
			Node temp = new Node(data);
			temp.next = head;
			head = temp;
		}
	}

	public Node kToLast(Node head, int k) {
		Node p1 = head;
		Node p2 = head;

		for (int i = 0; i < k; i++) {
			if (p1 == null) {
				return null;
			}
			p1 = p1.next;
		}

		while (p1.next != null) {
			p1 = p1.next;
			p2 = p2.next;
		}

		return p2;
	}

	public static void main(String[] args) {
		KtoLast kt = new KtoLast();
		kt.insert(1);
		kt.insert(4);
		kt.insert(7);
		kt.insert(10);
		kt.insert(9);
		kt.insert(5);
		kt.insert(5);
		Node kToLast = kt.kToLast(kt.head, 2);
		System.out.println("Kth to last element: " + kToLast.data);
	}
}
