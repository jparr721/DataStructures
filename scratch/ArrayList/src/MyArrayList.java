public class MyArrayList<E> {
    private E[] theArray;
    private int theJuice = 0;
    public MyArrayList() {
        theArray = (E[])new Object[0];
    }

    public E increaseSize() {
    }

    // Returns the value at a given index
    public E get(int index) {
        return theArray[index];
    }
}
