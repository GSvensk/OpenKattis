package problems;

public class EmergencyContestRunning {

	public static void main(String[] args) {
		
		long path = 0, optimalJumpDistance;
		
		//Custom OpenKattis scanner
		Kettio ka = new Kettio(System.in);
		
		//number of nodes
		long nodes = (ka.getLong()-1);
		
		//key is the magic number that connects two nodes as long as they are multiples
		long key = ka.getLong();
		
		//key can only get us somewhere if it's less than or half of the number of nodes, otherwise we have to walk the whole distance
		if(key <= (nodes/2)) {
			
			//floored division using long type to calculate optimalJumpDistance, the (integer) number of nodes we can jump using the key
			optimalJumpDistance = (key*(nodes/key));
			
			//First we have to go to node key, jump which takes 1 step and then cover the remaining distance between the node we land in and home
			path = key + 1 + (nodes-optimalJumpDistance);
			System.out.println(path);
		} else {
			System.out.println(nodes);
		}
		//close scanner
		ka.close();
	}
}
