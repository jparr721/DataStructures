class MyLinkedList<T> {

    protected Node head, last;
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
       last = null;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public int getSize() {
        return size;
    }

    public T getFirst() {
        return head.data;
    }

    public T getLast() {
        return last.data;
    }

    // Insert at the front of the Linked List
    public void addFirst(T data) {
        if (head == null) {
            Node temp = new Node();
            temp.data = data;
            head = temp;
            head.next = null;
            head.prev = null;
            size++;
        } else if (size == 1) {
            Node temp = head;
            Node newHead = new Node();
            newHead.data = data;
            last = head;
            head.next = newHead;
            head = newHead;
            head.prev = temp;
            size++;
        } else {
            Node temp = head;
            Node newHead = new Node();
            newHead.data = data;
            head.next = newHead;
            head = newHead;
            head.prev = temp;
            size++;
        }
    }

    public void addLast(T data) {
        if (head == null) {
            Node temp = new Node();
            temp.data = data;
            head = temp;
        }

        last = new Node(data, last, null);
    }

    public boolean contains(T data) {
        Node temp = last;

        while (temp != null) {
            if (temp.data == data) {
                return true;
            }
            else {
                temp = temp.next;
            }
        }
        return false;
    }

    public void remove() {
        System.out.println("Previous head " + head.data);
        head = head.prev;
        System.out.println("New head " + head.data);
    }

    public void print() {
        Node temp = last;
        while (temp != null) {
            System.out.print(temp.data + "-->");
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        // Initialize an empty linked list
        MyLinkedList<Integer> linkedList = new MyLinkedList<>();
        linkedList.addFirst(1);
        linkedList.addFirst(2);
        linkedList.addLast(3);
        linkedList.addLast(5);
        linkedList.addFirst(7);
        linkedList.addFirst(10);
        System.out.println(linkedList.contains(969));
        System.out.println(linkedList.contains(5));
        System.out.println(linkedList.contains(2));
        System.out.println(linkedList.getFirst());
        System.out.println(linkedList.getLast());
        linkedList.remove();
        System.out.println("The head: " + linkedList.head.data);
        linkedList.print();
    }
}
