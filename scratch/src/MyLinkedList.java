
class MyNode<T> {
    T data;
    MyNode next;
}

public class MyLinkedList<MyNode> {
    private MyNode head;
    private MyNode next;

    public MyLinkedList() { }

    public MyLinkedList(MyNode head, MyNode next) {
       this.head = head;
       this.next = next;
    }

    public void Print(MyNode head) {
        MyNode temp = head;

        while (temp != null) {

        }
    }
}
