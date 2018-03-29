import java.util.*;
/**
 * This set implementation just does
 * the more complex functionality since
 * the arrayList does the same crap anyway
 */

public class MySet<T> {
    private ArrayList<T> setList;

    public MySet() {
        setList = new ArrayList<>();
    }

    public boolean add(T data) {
        if (setList.contains(data)) {
            return false;
        } else {
            setList.add(data);
            return true;
        }
    }

    public boolean containsAll(Collection<T> C) {
        int numMatches = 0;
        for (T value : C) {
            if (setList.contains(value)) {
                numMatches++;
            }
        }
        if (setList.size() == numMatches) {
            return true;
        }
        return false;
    } 

    public boolean removeAll(Collection<T> C) {
        int numRemovals = setList.size();
        for (T value : C) {
            if (setList.remove(value)) {
                numRemovals--;
            }
        }
        if (numRemovals == 0) {
            return true;
        } 
        return false;
    }

    public boolean retainAll(Collection<T> C) {
        int matches = 0;
        for (int i = 0; i < setList.size(); i++) {
            if (!C.contains(setList.get(i))) {
                setList.remove(i);
            } else {
                matches++;
            }
        }
        if (matches == C.size()) {
            return true;
        }
        return false;
    }

    public void clear() {
        setList.clear();
    }
}
