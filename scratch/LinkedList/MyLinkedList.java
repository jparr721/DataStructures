class MyLinkedList<T> {

    protected Node head, previous, next;
    int size;

    class Node {
        T data;
        Node next;
        Node prev;

        public Node() {
            data = null;
            next = null;
            prev = null;
        }

        public Node(T d, Node n, Node p) {
           data = d;
           next = n;
           prev = p;
        }
    }

    public MyLinkedList() {
       head = null;
       size = 0;
       previous = null;
       next = null;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public int getSize() {
        return size;
    }

    public Node getFirst() {
        return head;
    }

    public Node getLast() {
        Node temp = head;
        while (temp.next != null) {
            // Iterate to the end of the list
            temp = temp.next;
        }
        return temp;
    }

    // Insert at the front of the Linked List
    public void addFirst(T data) {
        if (head == null) {
            Node temp = new Node();
            temp.data = data;
            head = temp;
        }

        Node newHead = new Node(data, null, head.prev);
        head.next = newHead;
        head = newHead;
        size++;
    }

    public void addLast(T data) {
        if (head == null) {
            Node temp = new Node();
            temp.data = data;
            head = temp;
        }

        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        Node newTail = new Node(data, temp, null);
        newTail.next = temp;
        size++;
    }

    public boolean contains(T data) {
        Node temp = head;

        while (temp != null) {
            if (temp.data == data)
                break;
            else
                temp = temp.next;
            return true;
        }
        return false;
    }
}
