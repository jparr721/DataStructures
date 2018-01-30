import java.util.LinkedList;

public class MyStack<E> {

    // Declare empty linked list
    LinkedList<E> ll;

    public MyStack() {
        ll = new LinkedList<>();
    }

    public boolean empty() {
        return ll.isEmpty();
    }

    public E peek() {
        return ll.peek();
    }

    public void pop() {
        ll.pop();
    }

    public void push(E data) {
        ll.push(data);
    }

    public void printStack() {
        for (E val : ll) {
            System.out.println(val);
        }
    }

    public int search(E data) {
        int dataLocation = 0;
        if (ll.contains(data)) {
            for(E val : ll) {
              if(ll.get(dataLocation) == data) {
                  break;
              } else {
                  dataLocation++;
              }
            }
        } else {
            dataLocation = -1;
        }
        return dataLocation;
    }

    public static void main(String[] args) {
        MyStack<Integer> stack = new MyStack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        stack.push(6);
        stack.pop();
        stack.printStack();
        System.out.println(stack.search(10));
    }
 }
