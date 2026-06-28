"""
Experiment 4: Implementation of Single Source Shortest Path (Dijkstra's)

Algorithm Description:
    Dijkstra's algorithm finds the shortest path from a source vertex
    to all other vertices in a weighted directed graph with non-negative
    edge weights. Uses a greedy approach with a priority queue.

Time Complexity: O((V + E) log V) with min-heap
Space Complexity: O(V + E)

Limitations: Does not work with negative edge weights (use Bellman-Ford)

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap Priority Queue
    
    Args:
        graph: Adjacency list {u: [(v, weight), ...]}
        source: Source vertex index
        
    Returns:
        tuple: (distance array, predecessor array)
        
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, vertex)
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Skip if already visited
        if u in visited:
            continue
        
        visited.add(u)
        
        # Relax edges
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return dist, prev


def reconstruct_path(prev, source, target):
    """
    Reconstruct shortest path from source to target
    
    Args:
        prev: Predecessor array from Dijkstra
        source: Source vertex
        target: Target vertex
        
    Returns:
        list: Path from source to target, or empty list if no path
    """
    path = []
    node = target
    
    while node is not None:
        path.append(node)
        node = prev[node]
    
    path.reverse()
    
    # Verify path starts from source
    if path and path[0] == source:
        return path
    
    return []


def demonstrate_dijkstra():
    """Demonstrate Dijkstra's algorithm on a sample graph."""
    # Graph represented as adjacency list
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }
    
    source = 0
    dist, prev = dijkstra(graph, source)
    
    print(f"Shortest paths from vertex {source}:")
    print()
    print(f"{'Vertex':>8} {'Distance':>10} {'Path':>35}")
    print('-' * 60)
    
    for v in range(len(graph)):
        path = reconstruct_path(prev, source, v)
        path_str = ' -> '.join(map(str, path)) if path else 'No path'
        d = dist[v] if dist[v] != float('inf') else 'INF'
        print(f"{v:>8} {str(d):>10} {path_str:>35}")


def example_with_path_details():
    """Show detailed path information for each destination."""
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }
    
    source = 0
    dist, prev = dijkstra(graph, source)
    
    print()
    print("=" * 60)
    print("DETAILED PATH INFORMATION")
    print("=" * 60)
    
    for target in range(len(graph)):
        path = reconstruct_path(prev, source, target)
        if path:
            print(f"\nPath to vertex {target}:")
            print(f"  Sequence: {' -> '.join(map(str, path))}")
            print(f"  Distance: {dist[target]}")
            
            # Show edge weights along path
            if len(path) > 1:
                print("  Edges:")
                for i in range(len(path) - 1):
                    u, v = path[i], path[i + 1]
                    # Find edge weight
                    for neighbor, weight in graph[u]:
                        if neighbor == v:
                            print(f"    {u} -> {v}: {weight}")
                            break


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 4: DIJKSTRA'S SHORTEST PATH ALGORITHM")
    print("=" * 70)
    print()
    
    demonstrate_dijkstra()
    example_with_path_details()
    
    print()
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("Dijkstra's algorithm guarantees optimal shortest paths")
    print("for non-negative edge weights using greedy approach.")
    print("Essential for GPS navigation, network routing (OSPF).")
    print("=" * 70)


if __name__ == "__main__":
    main()
