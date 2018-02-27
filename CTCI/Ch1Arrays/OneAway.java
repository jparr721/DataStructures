import java.util.*;
import java.lang.Math;
/**
  * Checks between two strings to see if they have only
  * one difference (one-char removal, one-char addition, one-char change)
  * Examples:
  * peak, peak --> True
  * park, dark --> True
  * dinoasaur, skeletor --> False
  */

class OneAway {
	public boolean oneAway(String s1, String s2) {
		HashMap<Character, Integer> map = new HashMap<>();

		if (Math.abs(s1.length() - s2.length()) > 2) {
			return false;
		}

		if (s1.equals(s2)) {
			return true;
		}

		for(int i = 0; i < s1.length(); i++) {
			int count = map.containsKey(s1.charAt(i)) ? map.get(s1.charAt(i)) : 0;
			if (map.containsKey(s1.charAt(i))) {
				map.put(s1.charAt(i), count + 1);
			} else {
				map.put(s1.charAt(i), count + 1);
			}
		}

		int diffCount = 0;
		for (int i = 0; i < s2.length(); i++) {
			int count = map.containsKey(s2.charAt(i)) ? map.get(s2.charAt(i)) : 0;
			if (map.containsKey(s2.charAt(i))) {
				map.put(s2.charAt(i), count - 1);
			} else {
				map.put(s2.charAt(i), count + 1);
			}
		}

		for (int value : map.values()) {
			if (value > 0) {
				diffCount++;
			}
		}

		return diffCount > 2 ? false : true;
	}

	public static void main(String[] args) {
		OneAway o = new OneAway();
		System.out.println(o.oneAway("peak", "peak"));
		System.out.println(o.oneAway("park", "dark"));
		System.out.println(o.oneAway("oblongo", "obongo"));
		System.out.println(o.oneAway("dinosaur", "skeletor"));
	}
}
