import java.util.*;

class Compress {
	
	public String compressString(String str) {
		if (str.length() == 0) {
			return str;
		}

		HashMap<Character, Integer> dict = new HashMap<>();
		char current;

		for (int i = 0; i < str.length() - 1; i++) {
			current = str.charAt(0); 
			int count = 1;
			if (str.charAt(i++) == (current)) {
				count++;
			} else {
				if (dict.containsKey(current)) {
					dict.put(current, count);
				} else {
					dict.put(current, count);
				}
				current = str.charAt(i++);
				count = 1;
			}
		}
		return dict.toString();
	}

	public static void main(String[] args) {
		Compress C = new Compress();
		System.out.println(C.compressString("aaabbbc"));
	}
}
