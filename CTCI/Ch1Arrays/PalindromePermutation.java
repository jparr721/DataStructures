import java.util.*;
  /* This code will check if a string is a permutation
   * of a palindrome. 
   * Example: "Tact coa" --> True (Permutation: Taco cat)
   * Example: "Oblong mongoose" --> False
   */
class PalindromePermutation {
	public boolean palindromePermutation(String s) {
		HashMap<Character, Integer> repeatedVals = new HashMap<Character, Integer>();
		int oddcount = 0;
		s = s.toLowerCase();
		for (int i = 0; i < s.length(); i++) {
			int count = repeatedVals.containsKey(s.charAt(i)) ? repeatedVals.get(s.charAt(i)) : 0;
			if (s.charAt(i) != ' '){
				if (repeatedVals.containsKey(s.charAt(i))) {
					repeatedVals.put(s.charAt(i), count + 1);
				} else {
					repeatedVals.put(s.charAt(i), count + 1);
				}
			} else {
				continue;
			}
		}

		for (int value : repeatedVals.values()) {
			if (value %2 != 0) {
				oddcount++;
			}
		}
		return oddcount < 2;
	}

	public static void main(String[] args) {
		PalindromePermutation p = new PalindromePermutation();
		System.out.println(p.palindromePermutation("Tact coa"));
		System.out.println(p.palindromePermutation("Oblong mongoose"));
	}
}
