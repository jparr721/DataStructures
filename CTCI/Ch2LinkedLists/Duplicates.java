import java.util.*;
/**
  * This class removes the duplicates from a 
  * Linked List
  * Examples:
  * 3-->3-->4-->5-->1-->END => 4-->5-->1-->END
  */

public class Duplicates {
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
	public Duplicates() {
		head = null;
	}

	public void addFirst(int data) {
		if (head == null) {
			head = new Node(data);
		} else {
			Node temp = new Node(data);
			temp.next = head;
			head = temp;
		}
	}

	public void print(Node head) {
		Node temp = head;
		while (temp.next != null) {
			System.out.print(temp.data + "-->");
			temp = temp.next;
		}
	}

	public void removeDuplicates(Node head) {
		Set<Integer> set = new HashSet<Integer>();
		Node temp = head;
		while(temp.next != null) {
			set.add(temp.data);
			temp = temp.next;
		}
		Iterator iter = set.iterator();
		while(iter.hasNext()) {
			System.out.print(iter.next() + "-->");
		}
	}

	public static void main(String[] args) {
		Duplicates d = new Duplicates();
		d.addFirst(1);
		d.addFirst(3);
		d.addFirst(3);
		d.addFirst(5);
		d.addFirst(6);
		d.addFirst(7);
		d.addFirst(5);
		System.out.println("List before dup removal");
		d.print(d.head);
		System.out.println("\nList after dup removal");
		d.removeDuplicates(d.head);
	}
}
