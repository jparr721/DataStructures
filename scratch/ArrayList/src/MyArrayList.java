import java.lang.reflect.Array;
import java.util.Arrays;

public class MyArrayList<E> {
    private Object theArray[];
    private int size = 0;

    public MyArrayList() {
        theArray = new Object[10];
    }

    // Doubles the size of the current array
    public void increaseSize() {
        int newSize = theArray.length * 2;
        theArray = Arrays.copyOf(theArray, newSize);
    }

    public void add(E data) {
        if (theArray.length - size <= 5) {
            increaseSize();
        }

        theArray[size++] = data;
    }

    public void delete(int index) {
        if (index >= size || theArray[index] == null || index < 0) {
            throw new ArrayIndexOutOfBoundsException();
        } else {
            for (int i = index; i < size - 1; i++) {
                theArray[i] = theArray[i + 1];
            }
            size--;
        }
    }

    // Returns the value at a given index
    @SuppressWarnings("unchecked")
    public void get(int index) {
        if (index >= size || theArray[index] == null || index < 0) {
            throw new ArrayIndexOutOfBoundsException();
        } else {
            System.out.println((E) theArray[index]);
        }
    }

    public void removeValue(E value) {
        for (int i = 0; i < size; i++) {
            if (theArray[i] == value) {
                delete(i);
            } else {
                break;
            }
        }
    }

    public void printValues() {
        for(int i = 0; i < size; i++) {
            System.out.print(theArray[i] + ", ");
        }
    }

    public static void main(String[] args) {
        MyArrayList al = new MyArrayList<Integer>();
        al.add(1);
        al.add(2);
        al.add(3);
        al.add(4);
        al.add(7);
        al.add(8);
        al.add(9);
        al.add(0);
        al.printValues();
        al.removeValue(1);
        System.out.println("\n");
        al.printValues();
        al.delete(3);
        System.out.println("\n");
        al.printValues();
        System.out.println("\n");
        al.get(2);
    }
}
