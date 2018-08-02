import java.util.*;

/**
  * This code determines if the linked list
  * contains a loop. This algorithm detects
  * the first occurance of the duplicate
  * node and returns it in O(n) time and space.
  * I could have used the runner technique to 
  * decrease space complexity, but I do these
  * solutions as if I were in an interview.
  *
  * This code assumes the linked list is always circular.
  */

public class Loop {
    public class Node {
        int data;
        Node next;
    }

    public int isLoop(Node root) {
        Set<Node> loopSet = new HashSet<>();
        Node temp = root;
        int output = -1; 

        while (temp != null) {
            if (loopSet.add(temp)) {
                temp = temp.next;
            } else {
                output = temp.data;
                break;
            }
        }
        return output;
    }
}
