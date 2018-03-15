import java.util.*;

/**
  * This code determines if two nodes in two
  * linked lists intersect at a point. There
  * are more efficient ways to do this, but 
  * this is what I came up with with O(t1 + t2) 
  * time and O(t1 + t2) space. So it's not bad.
  */
public class Intersect {

    public class Node {
        int data;
        Node next;
    }

    public boolean intersection(Node r1, Node r2) {
        Node t1 = r1;
        Node t2 = r2;
        HashMap<Node, Integer> nodeMap = new HashMap<>();

        while(t1 != null) {
            int count = nodeMap.containsKey(t1) ? nodeMap.get(t1) : 0;
            nodeMap.put(t1, count + 1);
            t1 = t1.next;
        }
        while(t2 != null) {
            int count = nodeMap.containsKey(t2) ? nodeMap.get(t2) : 0;
            nodeMap.put(t2, count + 1);
            t2 = t2.next;
        }
        int intersections = 0;
        for (int i : nodeMap.values()) {
            if (i > 1)
                intersections++;
            else
                continue;
        }

        return intersections != 0;
    }
}
