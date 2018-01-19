class MyLinkedList<T> {

    Node head;

    class Node {
        T data;
        Node next;

        public Node(T d) {
           data = d;
           next = null;
        }
    }

    public MyLinkedList() {
       head = null;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void insertAtHead(T data) {
       if (head != null) {
           Node newNode = new Node(data);
           newNode.next = head;
           head = newNode;
       } else {
           // If head null, then set head equal to a new node with data
           head = new Node(data);
       }
    }

    public void insertAtTail(T data) {
        if (head != null) {
            Node temp = head;

            while (temp.next != null) {
                temp = temp.next;
            }

            Node newNode = new Node(data);
            newNode.next = temp;
        }
    }
}
