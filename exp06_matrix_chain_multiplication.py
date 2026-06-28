"""
Experiment 6: Optimal Cost Computation in Matrix Chain Multiplication using DP

Algorithm Description:
    Matrix Chain Multiplication finds the optimal way to parenthesize
    a sequence of matrix multiplications to minimize scalar multiplications.
    
    For matrices A1(p0×p1), A2(p1×p2), ..., An(pn-1×pn), find optimal order.
    Example: A1(10×30) × A2(30×5) × A3(5×60) × A4(60×10)

Time Complexity: O(n³)
Space Complexity: O(n²)

Dynamic Programming Approach:
    - m[i][j]: minimum multiplications for matrices i to j
    - s[i][j]: split point k that gives optimal solution
    - Build solution bottom-up by increasing chain length

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""


def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming
    
    Args:
        dims: List of dimensions where matrix i has dims[i-1] × dims[i]
        
    Returns:
        tuple: (m array, s array)
               m[i][j] = minimum multiplications for matrices i to j
               s[i][j] = split point k for optimal solution
    
    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    n = len(dims) - 1  # Number of matrices
    
    # m[i][j] = minimum multiplications for matrices i to j
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # s[i][j] = split point for optimal solution
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    # l is chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            
            # Try all split points k
            for k in range(i, j):
                # Cost = cost of left chain + cost of right chain + 
                #        cost of multiplying result matrices
                cost = m[i][k] + m[k+1][j] + dims[i-1] * dims[k] * dims[j]
                
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    
    return m, s


def print_optimal_parens(s, i, j):
    """
    Recursively print optimal parenthesization
    
    Args:
        s: Split point array from matrix_chain_order
        i: Start matrix index
        j: End matrix index
        
    Returns:
        str: Optimal parenthesization string
    """
    if i == j:
        return f'A{i}'
    
    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)
    
    return f'({left} x {right})'


def print_dp_table(m, n):
    """
    Pretty print the DP cost table
    
    Args:
        m: DP cost table
        n: Number of matrices
    """
    print('\nDP Cost Table m[i][j]:')
    print(f"{'':>6}", end='')
    for j in range(1, n + 1):
        print(f'A{j:>8}', end='')
    print()
    
    for i in range(1, n + 1):
        print(f'A{i:<5}', end='')
        for j in range(1, n + 1):
            if j < i:
                print(f'{"---":>9}', end='')
            else:
                print(f'{m[i][j]:>9.0f}', end='')
        print()


def demonstrate_matrix_chain():
    """Demonstrate matrix chain multiplication with a 4-matrix example."""
    # Matrices: A1(10×30), A2(30×5), A3(5×60), A4(60×10)
    dims = [10, 30, 5, 60, 10]
    n = len(dims) - 1
    
    print("Matrix Dimensions:")
    for i in range(n):
        print(f"  A{i+1}: {dims[i]} x {dims[i+1]}")
    print()
    
    # Compute optimal solution
    m, s = matrix_chain_order(dims)
    
    print(f"Minimum scalar multiplications: {m[1][n]:.0f}")
    print(f"Optimal parenthesization: {print_optimal_parens(s, 1, n)}")
    
    print_dp_table(m, n)


def trace_computation():
    """Trace through computation step by step."""
    print()
    print("=" * 70)
    print("DETAILED COMPUTATION TRACE")
    print("=" * 70)
    print()
    
    dims = [10, 30, 5, 60, 10]
    n = len(dims) - 1
    
    print("Chain length 2 (adjacent pairs):")
    print(f"  m[1][2] = 10 × 30 × 5 = {10*30*5}")
    print(f"  m[2][3] = 30 × 5 × 60 = {30*5*60}")
    print(f"  m[3][4] = 5 × 60 × 10 = {5*60*10}")
    print()
    
    print("Chain length 3:")
    print(f"  m[1][3]: Best split at k=1: m[1][1] + m[2][3] + 10×30×60")
    print(f"           = 0 + {30*5*60} + {10*30*60} = {30*5*60 + 10*30*60}")
    print(f"           OR split at k=2: m[1][2] + m[3][3] + 10×5×60")
    print(f"           = {10*30*5} + 0 + {10*5*60} = {10*30*5 + 10*5*60}")
    print()
    
    print(f"  m[2][4]: Best split at k=2: m[2][2] + m[3][4] + 30×5×10")
    print(f"           = 0 + {5*60*10} + {30*5*10} = {5*60*10 + 30*5*10}")
    print(f"           OR split at k=3: m[2][3] + m[4][4] + 30×60×10")
    print(f"           = {30*5*60} + 0 + {30*60*10} = {30*5*60 + 30*60*10}")


def test_different_sizes():
    """Test with different number of matrices."""
    print()
    print("=" * 70)
    print("TESTING WITH DIFFERENT MATRIX CHAIN LENGTHS")
    print("=" * 70)
    print()
    
    test_cases = [
        [2, 3, 4],                    # 2 matrices
        [3, 4, 5, 6],                 # 3 matrices
        [5, 10, 3, 12, 5, 50, 6],    # 6 matrices
    ]
    
    for dims in test_cases:
        m, s = matrix_chain_order(dims)
        n = len(dims) - 1
        print(f"Matrices: {n}")
        print(f"  Dimensions: {' × '.join(f'{d}' for d in dims)}")
        print(f"  Optimal cost: {m[1][n]:.0f}")
        print(f"  Parenthesization: {print_optimal_parens(s, 1, n)}")
        print()


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 6: MATRIX CHAIN MULTIPLICATION")
    print("=" * 70)
    print()
    
    demonstrate_matrix_chain()
    trace_computation()
    test_different_sizes()
    
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("DP solves MCM in O(n³) vs exponential brute force")
    print("Critical for scientific computing and compiler optimization")
    print("Optimal parenthesization dramatically reduces computation time")
    print("=" * 70)


if __name__ == "__main__":
    main()
