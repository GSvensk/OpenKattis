import java.util.HashSet;

public class Cd {

	public static void main(String[] args) {

		Kattio katt = new Kattio(System.in);

		//CD:s owned by Jack
		int n = katt.getInt();
		//CD:s owned by Jill
		int m = katt.getInt();

		int answer;

		HashSet<Integer> hs = new HashSet<Integer>(n);

		while (n != 0 && m !=0) {

			//Reset hashset and answer
			hs.clear();
			answer = 0;

			//Fill hashset
			for (int i = 0; i < n; i++) {
				hs.add(katt.getInt());
			}

			//Check if new CD:s already exist, if they do, sell one
			for (int j = 0; j < m; j++) {
				if (hs.contains(katt.getInt())) {
					answer++;
				}
			}

			System.out.println(answer);

			n = katt.getInt();
			m = katt.getInt();
		}
	}
}
