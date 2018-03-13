import java.util.*;
import java.lang.*;
/**
  * This program takes two linked lists and 
  * sums their total values in reverse and normal
  * order.
  * Example:
  * 6-->1-->7 + 7-->1-->9 = 1336 (reversed)
  * 7-->1-->6 + 9-->1-->7 = 1336 (non-reversed)
  */

public class SumLists {

	protected Node head;

	public class Node {
		int data;
		Node next;

		public Node() {
			next = null;
		}

		public Node(int nodeData) {
			data = nodeData;
		}
	}

	public void insert(int data) {
		if (head == null) {
			Node newNode = new Node(data);
			head = newNode;
		} else {
			Node newNode = new Node(data);
			newNode.next = head;
			head = newNode;
		}
	}

	public void print(Node head) {
		Node temp = head;
		while (temp != null) {
			System.out.print(temp.data + "-->");
			temp = temp.next;
		}
		System.out.println("\n");
	}
	
	public int sumLists(Node root1, Node root2, boolean reverse) {
		StringBuilder final1 = new StringBuilder();
		StringBuilder final2 = new StringBuilder();
		Node temp1 = root1;
		Node temp2 = root2;

		while(temp1 != null) {
			final1.append(temp1.data);
			temp1 = temp1.next;
		}

		while(temp2 != null) {
			final2.append(temp2.data);
			temp2 = temp2.next;
		}

		if (reverse) {
			final1 = final1.reverse();
			final2 = final2.reverse();
			return Integer.parseInt(final1.toString()) + Integer.parseInt(final2.toString());
		}
		else {
			return Integer.parseInt(final1.toString()) + Integer.parseInt(final2.toString());
		}
	}

	public static void main(String[] args) {
		SumLists s1 = new SumLists();
		s1.insert(6);
		s1.insert(1);
		s1.insert(7);
		SumLists s2 = new SumLists();
		s2.insert(7);
		s2.insert(1);
		s2.insert(9);
		SumLists s3 = new SumLists();
		s3.insert(7);
		s3.insert(1);
		s3.insert(6);
		SumLists s4 = new SumLists();
		s4.insert(9);
		s4.insert(1);
		s4.insert(7);
		SumLists s = new SumLists();
		System.out.println(s.sumLists(s1.head, s2.head, true));
		System.out.println(s.sumLists(s3.head, s4.head, false));
	}
}
