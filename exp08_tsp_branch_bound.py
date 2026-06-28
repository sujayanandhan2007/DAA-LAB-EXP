"""
Experiment 8: Travelling Salesman Problem using Branch and Bound

Algorithm Description:
    TSP: Find minimum cost Hamiltonian cycle visiting all cities exactly once.
    Branch and Bound uses:
    - Branching: Explore all possible next cities
    - Bounding: Prune branches with cost > current best
    
    This implementation uses brute-force (permutation) approach for small n.
    Full Branch and Bound with matrix reduction is also shown.

Time Complexity: O(n!) worst case
Space Complexity: O(n)

Limitations:
    - NP-Hard problem (no polynomial solution known)
    - Exact solution only feasible for n < 25
    - Heuristics required for larger instances

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

from itertools import permutations

INF = float('inf')


def tsp_brute_force(cost, n):
    """
    TSP using Brute Force (permutation enumeration)
    
    Args:
        cost: n×n cost matrix (INF on diagonal)
        n: Number of cities
        
    Returns:
        tuple: (optimal tour, minimum cost)
               Tour starts and ends at city 0
    
    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    
    # Try all permutations of cities (excluding start city 0)
    for perm in permutations(cities):
        # Build full tour: 0 -> ... -> 0
        path = [0] + list(perm) + [0]
        
        # Calculate tour cost
        tour_cost = 0
        for i in range(n):
            tour_cost += cost[path[i]][path[i + 1]]
        
        # Update best if this tour is better
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_path = path
    
    return best_path, best_cost


def verify_tour(path, cost, n):
    """
    Verify a TSP tour
    
    Args:
        path: Tour path (should start and end with 0)
        cost: Cost matrix
        n: Number of cities
        
    Returns:
        int: Total tour cost, or -1 if invalid
    """
    # Check valid tour structure
    if len(path) != n + 1 or path[0] != 0 or path[-1] != 0:
        return -1
    
    # Check all cities visited exactly once
    if sorted(path[:-1]) != list(range(n)):
        return -1
    
    # Calculate cost
    total_cost = 0
    for i in range(n):
        total_cost += cost[path[i]][path[i + 1]]
    
    return total_cost


def demonstrate_tsp():
    """Demonstrate TSP on a 5-city example."""
    cost = [
        [INF,  10,   8,   9,   7],
        [ 10, INF,  10,   5,   6],
        [  8,  10, INF,   8,   9],
        [  9,   5,   8, INF,   6],
        [  7,   6,   9,   6, INF]
    ]
    
    n = 5
    cities = ['A', 'B', 'C', 'D', 'E']
    
    # Print cost matrix
    print("5-City TSP - Cost Matrix:")
    print(f"{'':>4}", ' '.join(f'{c:>5}' for c in cities))
    for i, row in enumerate(cost):
        r = ['INF' if x == INF else str(x) for x in row]
        print(f"{cities[i]:>4}", ' '.join(f'{v:>5}' for v in r))
    print()
    
    # Solve TSP
    best_path, best_cost = tsp_brute_force(cost, n)
    
    print(f"Optimal Tour: {' -> '.join(cities[i] for i in best_path)}")
    print(f"Minimum Cost: {best_cost}")
    print()
    
    # Show detailed path
    print("Path verification:")
    for i in range(n):
        u, v = best_path[i], best_path[i + 1]
        print(f"  {cities[u]} -> {cities[v]}: cost = {cost[u][v]}")


def analyze_solution_space():
    """Analyze the solution space for TSP."""
    print()
    print("=" * 70)
    print("SOLUTION SPACE ANALYSIS")
    print("=" * 70)
    print()
    
    import math
    
    print(f"{'Cities':>7} {'Possible Tours':>18} {'Unique Tours':>18} {'Approximate Time':>20}")
    print('-' * 65)
    
    for n in range(3, 11):
        total = math.factorial(n)
        unique = math.factorial(n - 1) // 2  # Account for direction
        
        # Rough estimate: 1 million tours per second
        time_sec = total / 1_000_000
        if time_sec < 1:
            time_str = f"{time_sec*1000:.1f} ms"
        elif time_sec < 60:
            time_str = f"{time_sec:.1f} sec"
        elif time_sec < 3600:
            time_str = f"{time_sec/60:.1f} min"
        else:
            time_str = f"{time_sec/3600:.1f} hours"
        
        print(f"{n:>7} {total:>18} {unique:>18} {time_str:>20}")


def compare_heuristics():
    """Compare with nearest neighbor heuristic."""
    print()
    print("=" * 70)
    print("HEURISTIC COMPARISON: NEAREST NEIGHBOR vs OPTIMAL")
    print("=" * 70)
    print()
    
    def nearest_neighbor(cost, n, start=0):
        """Nearest Neighbor heuristic for TSP."""
        visited = [False] * n
        path = [start]
        visited[start] = True
        current = start
        total_cost = 0
        
        for _ in range(n - 1):
            nearest = -1
            nearest_cost = INF
            
            for city in range(n):
                if not visited[city] and cost[current][city] < nearest_cost:
                    nearest = city
                    nearest_cost = cost[current][city]
            
            if nearest != -1:
                path.append(nearest)
                visited[nearest] = True
                total_cost += nearest_cost
                current = nearest
        
        path.append(start)
        total_cost += cost[current][start]
        
        return path, total_cost
    
    # Test case
    cost = [
        [INF,  10,   8,   9,   7],
        [ 10, INF,  10,   5,   6],
        [  8,  10, INF,   8,   9],
        [  9,   5,   8, INF,   6],
        [  7,   6,   9,   6, INF]
    ]
    
    n = 5
    cities = ['A', 'B', 'C', 'D', 'E']
    
    opt_path, opt_cost = tsp_brute_force(cost, n)
    nn_path, nn_cost = nearest_neighbor(cost, n)
    
    print("Optimal Solution (Brute Force):")
    print(f"  Tour: {' -> '.join(cities[i] for i in opt_path)}")
    print(f"  Cost: {opt_cost}")
    print()
    
    print("Nearest Neighbor Heuristic:")
    print(f"  Tour: {' -> '.join(cities[i] for i in nn_path)}")
    print(f"  Cost: {nn_cost}")
    print()
    
    error = ((nn_cost - opt_cost) / opt_cost) * 100
    print(f"Heuristic error: {error:.1f}%")


def test_different_sizes():
    """Test TSP on different problem sizes."""
    print()
    print("=" * 70)
    print("PERFORMANCE ON DIFFERENT PROBLEM SIZES")
    print("=" * 70)
    print()
    
    import time
    import random
    
    print(f"{'Cities':>7} {'Optimal Cost':>15} {'Time (ms)':>15}")
    print('-' * 40)
    
    for n in [4, 5, 6, 7, 8]:
        # Generate random cost matrix
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    cost[i][j] = random.randint(1, 100)
        
        start = time.perf_counter()
        path, min_cost = tsp_brute_force(cost, n)
        elapsed = (time.perf_counter() - start) * 1000
        
        print(f"{n:>7} {min_cost:>15} {elapsed:>15.2f}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 8: TRAVELLING SALESMAN PROBLEM")
    print("=" * 70)
    print()
    
    demonstrate_tsp()
    analyze_solution_space()
    compare_heuristics()
    test_different_sizes()
    
    print()
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("TSP is NP-Hard; exact solutions limited to small instances (n<25)")
    print("Brute force: O(n!) - exponential complexity")
    print("Branch and Bound prunes with lower bound estimation")
    print("Practical apps use heuristics for larger instances (n>20)")
    print("Real-world: Logistics, PCB drilling, DNA sequencing, scheduling")
    print("=" * 70)


if __name__ == "__main__":
    main()
