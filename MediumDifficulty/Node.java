//package shortestpath1;

import java.util.ArrayList;

public class Node implements Comparable<Node> {

	public final int number;
	public double distance = Double.POSITIVE_INFINITY;
	ArrayList<Edge> neighbours;

	public Node(int number) {
		this.number = number;
		this.neighbours = new ArrayList<Edge>();
	}
	
	@Override
	public int compareTo(Node other) {

		if (distance < other.distance) {
			return -1;
		}
		if (distance > other.distance) {
			return 1;
		}
		return 0;
	}
}
