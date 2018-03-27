import java.util.*;
import java.io.*;

public class Plates {
    int size = 0;
    int[] plate;
    ArrayList<int[]> setOfStacks = new ArrayList<>();
    int capacity = 0;

    public Plates() {
        capacity = 3;
        size = 0;
        plate = new int[capacity];
    }

    public void push(int data) {
        if (size < capacity) {
            plate[size] = data;
            size++;
        } else {
            setOfStacks.add(plate);
            size = 0;
            plate = new int[capacity];
            plate[size] = data;
            size++;
        }
    }

    public int[] pop() {
        int[] poppedVal = setOfStacks.get(0);
        setOfStacks.remove(0);

        return poppedVal;
    }

    public int[] popAt(int index) {
        int[] value;
        if (setOfStacks.contains(setOfStacks.get(index))) {
            value = pop();
        } else {
            throw new IndexOutOfBoundsException("This value does not exist on the stack set!");
        }
        return value;
    }

    public static void main(String[] args) {
        Plates p = new Plates();
        p.push(1);
        p.push(2);
        p.push(3);
        System.out.println(p.size);
        for (int i = 0; i < p.size; i++) {
            System.out.print(p.plate[i] + ", ");
        }
        p.push(3);
        System.out.println("\n" + p.size);
        for (int i = 0; i < p.size; i++) {
            System.out.print(p.plate[i] + ", ");
        }
        p.pop();
        for (int[] array : p.setOfStacks) {
            for (int number : array) {
                System.out.print(number);
            }
        }
    }
}
