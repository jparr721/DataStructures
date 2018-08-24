import java.util.*;

public class Replace {
	public String urlify(String url) {
		StringBuilder sb = new StringBuilder();
		String urlArray[] = url.split(" +");

		for (int i = 0; i < urlArray.length; i++) {
			if(i != urlArray.length - 1) {
				sb.append(urlArray[i]);
				sb.append("%20");
			} else {
				sb.append(urlArray[i]);
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		Replace r = new Replace();
		System.out.println(r.urlify("My name is jonas"));
		System.out.println(r.urlify("I     love fluffy dogs    "));
	}
}
