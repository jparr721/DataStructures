import java.util.*;

public class MyQueue {
    Stack<Integer> regStack, queueStack;

    public MyQueue() {
        regStack = new Stack<>();
        queueStack = new Stack<>();
    }

    public void add(int data) {
        regStack.push(data);
    }

    public void transferElements() {
        if (queueStack.isEmpty()) {
            while (!regStack.isEmpty()) {
                queueStack.push(regStack.pop());
            }
        }
    }

    public int remove() {
        transferElements();
        return queueStack.pop();
    }

    public int peek() {
        transferElements();
        return queueStack.peek();
    }
}
