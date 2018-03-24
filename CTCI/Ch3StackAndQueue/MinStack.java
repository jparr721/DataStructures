import java.util.*;

/**
* This is a stack implementation that returns
* the miniumum value in O(1) time.
*
* Ex:
* TOP: 11, 13, 4, 5, 8, 9 --> min = 4
*/
public class MinStack {
    ArrayList<Integer> stack = new ArrayList<>();
    ArrayList<Integer> minStack = new ArrayList<>();
    int min = Integer.MAX_VALUE;

    public void push(int data) {
        if (data < min) {
            min = data;
            minStack.add(data);
        }
        stack.add(data);
    }

    public int peek() {
        return stack.get(stack.size() - 1);
    }

    public int pop() {
        int poppedVal = stack.get(stack.size() - 1);
        stack.remove(stack.size() - 1);
        if (poppedVal == min) {
            minStack.remove(minStack.size() - 1);
            min = minStack.size() - 1; // Assign the next in line for min value
        }
        return poppedVal;
    }

    public int min() {
        return min;
    }

    public static void main(String[] args) {
        MinStack ms = new MinStack();
        ms.push(10);
        ms.push(4);
        ms.push(19);
        ms.push(1);
        ms.push(11);
        System.out.println(ms.peek());
        System.out.println(ms.min());
    }
}
