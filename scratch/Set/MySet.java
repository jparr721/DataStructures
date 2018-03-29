import java.util.*;

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

    public void clear() {
        setList.clear();
    }
}
