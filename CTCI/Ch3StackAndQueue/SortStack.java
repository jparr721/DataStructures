import java.util.*;
/**
 * This code is an implementation of the
 * common stack ADT, but it sorts all of 
 * the information as it comes in.
 */

public class SortStack {
    Stack<Integer> sorted;
    Stack<Integer> temporary;

    public SortStack() {
        sorted = new Stack<>();
        temporary = new Stack<>();
    }

    public void push(int data) {
        while (!sorted.isEmpty() && data > sorted.peek()) {
            temporary.push(sorted.pop());
        }
        sorted.push(data);
        while(!temporary.empty()) {
            sorted.push(temporary.pop());
        }
    }

    public int pop() {
        return sorted.pop();
    }

    public int peek() {
        return sorted.peek();
    }

    public boolean isEmpty() {
        return sorted.empty();
    }

    // For testing
    public void print() {
        System.out.println(Arrays.toString(sorted.toArray()));
    }

    public static void main(String[] args) {
        SortStack ss = new SortStack();
        System.out.println(ss.isEmpty());
        ss.push(10);
        ss.push(100);
        ss.push(15);
        ss.push(18);
        ss.print();
    }
}
