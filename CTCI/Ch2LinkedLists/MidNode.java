import java.util.*;
/**
  * This code deletes the "middle" or any
  * other arbitrary element in a linked list
  * when given a reference ONLY to the middle
  * element (so you can't start from root)
  * Example:
  * 1-->2-->4-->7 MID = 4 Output: 1-->2-->7
  */

public class MidNode {

	protected Node head;

	public class Node {
		int data;
		Node next;

		public Node() {
			next = null;
		}

		public Node(int newData) {
			data = newData;
		}
	}

	public void insert(int data) {
		if (head == null) {
			head = new Node(data);
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
		System.out.println("");
	}

	public Node find(Node head, int data) {
		Node temp = head;
		Node foundVal = new Node();
		while (temp != null) {
			if (temp.data == data) {
				foundVal = temp;
				break;
			} else {
				temp = temp.next;
			}
		}
		return foundVal;
	}
	
	public void deleteMiddleNode(Node mid) {
		Node temp = mid.next;
		mid.data = temp.data;
		mid.next = temp.next;
	}

	public static void main(String[] args) {
		MidNode m = new MidNode();
		m.insert(1);
		m.insert(4);
		m.insert(6);
		m.insert(8);
		m.insert(10);
		m.insert(5);
		m.print(m.head);
		Node delete = m.find(m.head, 6);
		m.deleteMiddleNode(delete);
		m.print(m.head);
	}
}
