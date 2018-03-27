import java.util.*;
/**
 * AnimalShelter leverages a queue to manage adoptions
 * and returns animals based on prefernece or lackthereof.
 */

public class AnimalShelter {
    LinkedList<Boolean> petList;

    public AnimalShelter() {
        petList = new LinkedList<>();
    }

    // Cat = false
    // Dog = true

    public void enqueue(boolean animal) {
        petList.add(animal);
    }

    public boolean dequeueDog() {
        if (petList.removeLastOccurrence(true)){
            System.out.println("Dog adopted");
            return true;
        } else {
            System.out.println("No dogs left to adopt");
            return false;
        }
    }

    public boolean dequeueCat() {
        if (petList.removeLastOccurrence(false)) {
            System.out.println("Cat adopted");
            return true;
        } else {
            System.out.println("No cats left to adopt");
            return false;
        }
    }

    public void dequeueAny() {
       if (petList.removeLast()) {
            System.out.println("Dog removed");
       } else {
            System.out.println("Cat removed");
       }
    }

    public static void main(String[] args) {
        AnimalShelter a = new AnimalShelter();
        a.enqueue(false);
        a.enqueue(false);
        a.enqueue(false);
        a.enqueue(true);
        a.dequeueAny();
        a.dequeueAny();
        a.dequeueDog();
    }
}
