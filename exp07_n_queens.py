"""
Experiment 7: Solving N-Queens Problem using Backtracking

Algorithm Description:
    Place N queens on an N×N chessboard such that no two queens attack each other.
    Uses backtracking to explore and prune the search space.
    
    Constraints:
    - No two queens in same row (ensured by placement order)
    - No two queens in same column
    - No two queens in same diagonal (checked by is_safe)

Time Complexity: O(N!)
Space Complexity: O(N) for recursion stack

Key Insight:
    Backtracking reduces search space from N^N to N! by exploring only
    valid placements. For N=8, only 92 valid solutions exist out of
    4,426,165,368 brute-force possibilities.

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""


def is_safe(board, row, col):
    """
    Check if placing queen at (row, col) is safe
    
    Args:
        board: Array where board[i] = column of queen in row i, -1 if empty
        row: Current row
        col: Current column to check
        
    Returns:
        bool: True if safe to place queen, False otherwise
    
    Time Complexity: O(N)
    """
    # Check previously placed queens (all in rows < row)
    for prev_row in range(row):
        placed = board[prev_row]
        
        # Same column
        if placed == col:
            return False
        
        # Same diagonal (difference of coordinates is equal)
        if abs(prev_row - row) == abs(placed - col):
            return False
    
    return True


def solve_n_queens(n):
    """
    Solve N-Queens problem using backtracking
    
    Args:
        n: Board size (number of queens)
        
    Returns:
        tuple: (list of solutions, backtrack count)
               Each solution is a list where solution[i] = column of queen in row i
    
    Time Complexity: O(N!)
    Space Complexity: O(N)
    """
    board = [-1] * n
    solutions = []
    backtrack_count = [0]  # Use list to allow modification in nested function
    
    def backtrack(row):
        """
        Recursive backtracking function
        
        Args:
            row: Current row to place queen
        """
        if row == n:
            # All queens placed successfully
            solutions.append(board[:])
            return
        
        # Try placing queen in each column of current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo (backtrack)
                backtrack_count[0] += 1
    
    backtrack(0)
    return solutions, backtrack_count[0]


def display_board(solution, n):
    """
    Display N-Queens solution as ASCII board
    
    Args:
        solution: Solution array (column for each row)
        n: Board size
    """
    print('  +' + '---+' * n)
    for row in range(n):
        print('  |', end='')
        for col in range(n):
            if solution[row] == col:
                print(' Q |', end='')
            else:
                print(' . |', end='')
        print()
        print('  +' + '---+' * n)


def demonstrate_n_queens():
    """Demonstrate N-Queens for small board sizes."""
    for n in [4, 6, 8]:
        solutions, backtracks = solve_n_queens(n)
        print(f"N={n}: {len(solutions)} solutions, {backtracks} backtracks")
        
        if n == 4:
            print(f'\n  All solutions for {n}-Queens:')
            for i, sol in enumerate(solutions, 1):
                print(f'\n  Solution {i}: {sol}')
                display_board(sol, n)
        print()


def analyze_solution_properties():
    """Analyze properties of solutions."""
    print()
    print("=" * 70)
    print("SOLUTION ANALYSIS")
    print("=" * 70)
    print()
    
    for n in range(1, 9):
        solutions, backtracks = solve_n_queens(n)
        print(f"N={n:2}: Solutions={len(solutions):4} "
              f"Backtracks={backtracks:6} "
              f"Branching~{backtracks/(len(solutions)+1):.1f}")


def verify_solution(solution, n):
    """
    Verify that a solution is valid
    
    Args:
        solution: Solution array
        n: Board size
        
    Returns:
        bool: True if valid solution, False otherwise
    """
    # Check all pairs of queens
    for i in range(n):
        for j in range(i + 1, n):
            # Queens at (i, solution[i]) and (j, solution[j])
            
            # Same column
            if solution[i] == solution[j]:
                return False
            
            # Same diagonal
            if abs(i - j) == abs(solution[i] - solution[j]):
                return False
    
    return True


def solution_verification():
    """Verify all solutions are valid."""
    print()
    print("=" * 70)
    print("SOLUTION VERIFICATION")
    print("=" * 70)
    print()
    
    for n in [4, 5, 6]:
        solutions, _ = solve_n_queens(n)
        all_valid = all(verify_solution(sol, n) for sol in solutions)
        print(f"N={n}: {len(solutions)} solutions, All valid: {all_valid}")


def comparison_with_brute_force():
    """Compare backtracking with brute force search space."""
    print()
    print("=" * 70)
    print("SEARCH SPACE REDUCTION")
    print("=" * 70)
    print()
    
    print(f"{'N':>2} {'N-Queens':>10} {'N^N':>15} {'N!':>15} {'Reduction':>12}")
    print('-' * 60)
    
    import math
    for n in range(1, 9):
        solutions, _ = solve_n_queens(n)
        nn = n ** n
        nfact = math.factorial(n)
        reduction = (1 - len(solutions) / nn) * 100
        print(f"{n:2} {len(solutions):10} {nn:15} {nfact:15} {reduction:11.2f}%")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 7: N-QUEENS PROBLEM USING BACKTRACKING")
    print("=" * 70)
    print()
    
    demonstrate_n_queens()
    analyze_solution_properties()
    solution_verification()
    comparison_with_brute_force()
    
    print()
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("Backtracking efficiently prunes invalid search branches")
    print("Reduces search space from N^N to N! valid configurations")
    print("For N=8: only 92 solutions vs 16,777,216 brute-force attempts")
    print("Essential for constraint satisfaction, scheduling, graph coloring")
    print("=" * 70)


if __name__ == "__main__":
    main()
