//package shortestpath1;

import java.util.PriorityQueue;

public class Shortestpath {
	
	public static void search(Node start) {
		
		PriorityQueue<Node> Q = new PriorityQueue<Node>();
		Q.add(start);
		
		while (!Q.isEmpty()) {
			
			Node head = Q.poll();
			
			for (Edge e : head.neighbours) {
				Node u = e.endNode;
				double alt = head.distance + e.weight;
				if (alt < u.distance) {
					u.distance = alt;
					Q.add(u);
				}
			}
		}		
	}

	public static void main(String args[]) {

		Kattio io = new Kattio(System.in);
		int n = io.getInt();
		int edges = io.getInt();
		int queries = io.getInt();
		int start = io.getInt();

		Node[] nodes;
		
		while (n != 0) {
			nodes = new Node[n];

			for (int i = 0; i < n; i++) {
				nodes[i] = new Node(i);
			}

			nodes[start].distance = 0;

			for (int i = 0; i < edges; i++) {
				int u = io.getInt();
				int v = io.getInt();
				double w = io.getDouble();
				nodes[u].neighbours.add(new Edge(nodes[v], w));
			}

			search(nodes[start]);
			
			for (int i = 0; i < queries; i++) {
				int query = io.getInt();
				if (nodes[query].distance == Double.POSITIVE_INFINITY) {
					System.out.println("Impossible");
				} else {
					System.out.println((int)(nodes[query].distance));
				}
			}
			System.out.println();
			n = io.getInt();
			edges = io.getInt();
			queries = io.getInt();
			start = io.getInt();
		}
	}
}
