import java.util.*;
/**
  * This code checks to see if a Linked List
  * of characters contains a palindrome 
  * (a word that is the same front to back)
  * Example:
  * m-->o-->m true
  * m-->o-->k false
  */

public class Palindrome {

	protected Node head;
	
	public class Node {
		char data;
		Node next;

		public Node() {
			next = null;
		}

		public Node(char newData) {
			data = newData;
		}
	}

	public void insert(char data) {
		if (head == null) {
			head = new Node(data);
		} else {
			Node newVal = new Node(data);
			newVal.next = head;
			head = newVal;
		}
	}

	public void print(Node head) {
		Node temp = head;
		while (temp != null) {
			System.out.print(temp.data + "-->");
			temp = temp.next;
		}
	}

	public boolean isPalindrome(Node root) {
		Node temp = root;
		HashMap<Character, Integer> charMap = new HashMap<>();
		while (temp != null) {
			int count = charMap.containsKey(temp.data) ? charMap.get(temp.data) : 0;
			charMap.put(temp.data, count + 1);
			temp = temp.next;
		}

		int differences = 0;
		for (int vals : charMap.values()) {
			if (vals %2 == 0) {
				continue;
			} else {
				differences++;
			}
		}
		return differences <= 1;
	}

	public static void main(String[] args) {
		Palindrome p = new Palindrome();
		p.insert('m');
		p.insert('o');
		p.insert('k');
		System.out.println(p.isPalindrome(p.head));
	}
}
