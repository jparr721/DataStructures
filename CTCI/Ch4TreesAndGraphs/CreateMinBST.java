import java.util.*;
/*
 * This algorithm makes a minimal Binary Search
 * Tree from a sorted array, which enables us
 * to use a modified binary search algorithm 
 * to get what we need.
 */

public class CreateMinBST {
	
		public class Node {
			int[] data;
			Node left;
			Node right;	
				
			public Node(int arr[]) {
				data = arr;	
			}
		}


		public Node createMinBST(int sortedArr[]) {
			return createMinBST(sortedArr, 0, sortedArr.length - 1);
		}

		public Node createMinBST(int sortedArr[], int start, int end) {
			if (end < start) {
				return null;
			}

			int mid = (start + end) / 2;
			Node n = new Node(sortedArr);
			n.left = createMinBST(sortedArr, start, mid - 1);
			n.right = createMinBST(sortedArr, mid + 1, end);
			return n;
		}
}
