//package shortestpath1;

public class Edge {
	
	public final double weight;
	public final Node endNode;
	
	public Edge(Node endNode, double weight) {
		this.endNode = endNode;
		this.weight = weight;
	}
}
