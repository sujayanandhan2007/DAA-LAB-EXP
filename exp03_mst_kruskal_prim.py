"""
Experiment 3: Implementation of Kruskal's and Prim's Algorithms for MST

Algorithm Description:
    Two classical algorithms for finding Minimum Spanning Tree:
    1. Kruskal's: Sort edges globally, use Union-Find to detect cycles
    2. Prim's: Grow tree greedily from start vertex using priority queue

Time Complexity:
    - Kruskal's: O(E log E) with sorting, O(E α(V)) union-find
    - Prim's: O(E log V) with min-heap, O(V^2) with array

Space Complexity: O(V + E)

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import heapq


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure
    
    Used in Kruskal's algorithm to detect cycles efficiently.
    Features path compression and union by rank for O(α(n)) amortized time.
    """
    
    def __init__(self, n):
        """
        Initialize Union-Find structure for n elements
        
        Args:
            n: Number of elements (vertices)
        """
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """
        Find the root of element x with path compression
        
        Args:
            x: Element to find root of
            
        Returns:
            int: Root of element x
            
        Time Complexity: O(α(n)) amortized
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union two sets containing x and y
        
        Args:
            x: Element in first set
            y: Element in second set
            
        Returns:
            bool: True if union succeeded, False if already in same set
            
        Time Complexity: O(α(n)) amortized
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        return True


def kruskal(n, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree
    
    Args:
        n: Number of vertices
        edges: List of (weight, u, v) tuples
        
    Returns:
        tuple: (list of MST edges, total cost)
        
    Time Complexity: O(E log E)
    Space Complexity: O(V + E)
    """
    edges.sort()  # O(E log E)
    uf = UnionFind(n)
    mst = []
    cost = 0
    
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == n - 1:
                break
    
    return mst, cost


def prim(n, adj, start=0):
    """
    Prim's Algorithm for Minimum Spanning Tree
    
    Args:
        n: Number of vertices
        adj: Adjacency list {u: [(v, w), ...]}
        start: Starting vertex (default 0)
        
    Returns:
        tuple: (list of MST edges, total cost)
        
    Time Complexity: O(E log V)
    Space Complexity: O(V + E)
    """
    INF = float('inf')
    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n
    key[start] = 0
    pq = [(0, start)]
    mst = []
    cost = 0
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        
        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w
        
        # Explore neighbors
        for v, wt in adj.get(u, []):
            if not in_mst[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))
    
    return mst, cost


def build_adjacency_list(n, edges):
    """
    Build adjacency list from edge list
    
    Args:
        n: Number of vertices
        edges: List of (weight, u, v) tuples
        
    Returns:
        dict: Adjacency list {u: [(v, w), ...]}
    """
    adj = {}
    for w, u, v in edges:
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    
    return adj


def demonstrate_mst():
    """Demonstrate MST algorithms on a sample graph."""
    n = 7
    edges = [
        (7, 0, 1), (5, 0, 3), (8, 1, 2), (9, 1, 3),
        (7, 1, 4), (5, 2, 4), (15, 3, 4), (6, 3, 5),
        (8, 4, 5), (9, 4, 6), (11, 5, 6)
    ]
    
    # Build adjacency list for Prim's
    adj = build_adjacency_list(n, edges)
    
    # Run both algorithms
    k_mst, k_cost = kruskal(n, edges[:])  # Copy edges
    p_mst, p_cost = prim(n, adj)
    
    print(f"{'Vertex Count':>20}: {n}")
    print(f"{'Edge Count':>20}: {len(edges)}")
    print()
    
    print("=" * 50)
    print("KRUSKAL'S ALGORITHM")
    print("=" * 50)
    for u, v, w in k_mst:
        print(f"  Edge ({u} - {v})  Weight: {w}")
    print(f"  Total MST Cost: {k_cost}")
    print()
    
    print("=" * 50)
    print("PRIM'S ALGORITHM")
    print("=" * 50)
    for u, v, w in p_mst:
        print(f"  Edge ({u} - {v})  Weight: {w}")
    print(f"  Total MST Cost: {p_cost}")
    print()
    
    print(f"Both algorithms produced same MST cost: {k_cost == p_cost}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 3: MINIMUM SPANNING TREE")
    print("=" * 70)
    print()
    
    demonstrate_mst()
    
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("Kruskal's is efficient for sparse graphs (E log E)")
    print("Prim's is efficient for dense graphs (E log V)")
    print("Both guarantee optimal MST for undirected graphs.")
    print("=" * 70)


if __name__ == "__main__":
    main()
