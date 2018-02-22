import java.util.*;

class Duplicate {
	public boolean isUnique(String str) {
		Set<Character> values = new HashSet<>();
		boolean dupFound = false;
		for (int i = 0; i < str.length(); i++) {
			if (values.add(str.charAt(i))) {
				continue;
			} else {
				dupFound = true;
				break;
			}
		}

		return dupFound;
	}

	public static void main(String[] args) {
		Duplicate d = new Duplicate();
		System.out.println(d.isUnique("abracadabra"));
		System.out.println(d.isUnique("Orange"));
	}
}
