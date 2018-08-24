import java.util.*;

/**
  * This code checks if two strings are permutations of one another
  * and returns true if they are, and false otherwise.
  * Example: "abc", "cab" --> true
  * Example: "bucket", "flower" --> false
  */

class Permutation {
	public boolean isPermutation(String s1, String s2) {
		if (s1.length() != s2.length()) {
			return false;
		}

		char temp1[] = s1.toCharArray();
		char temp2[] = s2.toCharArray();
		Arrays.sort(temp1);
		Arrays.sort(temp2);
		String nS1 = new String(temp1);
		String nS2 = new String(temp2);

		return nS1.equals(nS2);
	}

	public static void main(String[] args) {
		Permutation p = new Permutation();
		System.out.println(p.isPermutation("dog", "god"));
		System.out.println(p.isPermutation("bucket", "flower"));
	}
}
