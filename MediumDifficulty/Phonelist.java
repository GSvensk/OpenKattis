package problemos;

import java.util.Arrays;

public class Phonelist {
	
	public static boolean checkList(String[] str) {

		for(int i = 0; i < str.length-1; i++) {
			int k = 0;
			//try {
			while ((k < str[i].length()) && (str[i].charAt(k) == str[i+1].charAt(k))) {
				k++;
			}
			//} catch(StringIndexOutOfBoundsException exception) {
				//return false;
			//}
			if (k == str[i].length()) {
				return false; 
			}
		}
		return true;
	}

	public static void main(String[] args) {
		
		Kattio io = new Kattio(System.in);
		int cases = io.getInt();
		int numbers;
		String[] nrs = null;
		
		for(int i = 0; i < cases; i++) {
			numbers = io.getInt();
			nrs = new String[numbers];
			for(int j = 0; j < numbers; j++) {
				nrs[j] = io.getWord();
			}
			Arrays.sort(nrs);
			
			if (checkList(nrs)) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		}
		io.close();
	}
}
