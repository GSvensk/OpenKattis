package problems;

import moneyfornothing.Kettio;

public class GuessTheNumber {

	public static void main(String[] args) {

		double lowerLimit = 0, counter = 1;
		double upperLimit = 1000;
		double guess = 500;
		
		//OpenKattis scanner
		Kettio ka = new Kettio(System.in);
		
		//First guess is always 500
		System.out.println(guess);
		ka.flush();
		
		//Answer to previous guess
		String answer = ka.getWord();
		
		//Loop while answer is wrong and there are guesses available
		while ((!answer.equals("correct")) && (counter < 10)) {
			
			//Adjust limits based on previous guess
			if(answer.equals("higher")){
				lowerLimit = guess;
			} else {
				upperLimit = guess;
			}
			
			//New guess is in the middle of the limits
			guess = Math.round(((upperLimit+lowerLimit)/2));
			System.out.println((int) guess);
			
			//flush scanner
			ka.flush();
			//increment
			counter++;
			//save answer for the next guess
			answer = ka.getWord();
		}
		ka.close();
	}
}
