import java.util.*;
/**
  * This checks if code is a rotation of another
  * piece of code. It's pretty much the same as
  * the permutation. I wanted to try and do it
  * without the "isSubstring()" function the book
  * defined since I doubt I'd get something similar
  * for real.
  *
  * Example:
  * "waterbottle", "erbottlewat" --> True
  * "coat", "moat" --> False
  */

public class Rotation {
	public boolean isRotation(String s1, String s2) {
		if (s1.equals(s2)) {
				return true;
		}

		char[] val1 = s1.toCharArray();
		Arrays.sort(val1);
		char[] val2 = s2.toCharArray();
		Arrays.sort(val2);

		String f1 = new String(val1);
		String f2 = new String(val2);

		return (f1.equals(f2)) ? true: false;
	}

	public static void main(String[] args){
		Rotation r = new Rotation();
		System.out.println(r.isRotation("waterbottle", "erbottlewat"));
		System.out.println(r.isRotation("coat", "moat"));
	}
}
