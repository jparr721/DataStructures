import java.util.*;

class Compress {
	
	public String compressString(String str) {
		StringBuilder sb = new StringBuilder();
		int count = 0;
		
		if (str.length() == 0) {
			return str;
		}

		for (int i = 0; i < str.length(); i++) {
			count++;
			if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i+1)) {
				sb.append(str.charAt(i));
				sb.append(count);
				count = 0;
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		Compress C = new Compress();
		System.out.println(C.compressString("aaabbbc"));
	}
}
