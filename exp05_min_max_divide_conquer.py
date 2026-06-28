"""
Experiment 5: Find Min-Max Value by Applying Divide and Conquer Technique

Algorithm Description:
    The Divide and Conquer approach simultaneously finds minimum and maximum
    elements with optimal number of comparisons: 3n/2 - 2
    
    Compare naive approach (2n - 2 comparisons) with D&C approach.
    The D&C method achieves 25% reduction in comparisons.

Time Complexity: O(n)
Space Complexity: O(log n) for recursion stack

Comparison Formula:
    - Naive: 2(n-1) comparisons
    - D&C: 3n/2 - 2 comparisons (approximately 1.5n)
    - Theoretical improvement: 25% reduction

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import random


# Global counter for comparisons (for demonstration)
comparison_count = 0


def min_max_dc(arr, low, high):
    """
    Find Min and Max using Divide and Conquer
    
    Args:
        arr: List of integers
        low: Starting index
        high: Ending index
        
    Returns:
        tuple: (minimum, maximum)
    
    Time Complexity: O(n)
    Space Complexity: O(log n) for recursion
    
    Comparison Count: Exactly 3n/2 - 2 comparisons
    """
    global comparison_count
    
    # Base case: single element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: two elements (1 comparison)
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
    
    # Divide: split array in half
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    
    # Conquer: combine results with 2 comparisons
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    
    return overall_min, overall_max


def min_max_naive(arr):
    """
    Find Min and Max using Naive Approach
    
    Args:
        arr: List of integers
        
    Returns:
        tuple: (minimum, maximum, comparison count)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Comparison Count: 2(n-1) comparisons
    """
    mn, mx = arr[0], arr[0]
    comps = 0
    
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        
        comps += 1
        if x > mx:
            mx = x
    
    return mn, mx, comps


def demonstrate_on_small_array():
    """Demonstrate both approaches on a small array."""
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
    
    global comparison_count
    comparison_count = 0
    
    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc_comps = comparison_count
    
    _, _, naive_comps = min_max_naive(arr)
    
    print(f"Array: {arr}")
    print(f"Min: {mn}, Max: {mx}")
    print()
    print(f"{'Approach':<20} {'Comparisons':>15} {'Formula':>20}")
    print('-' * 60)
    print(f"{'D&C':20} {dc_comps:>15} {'3n/2 - 2':>20}")
    print(f"{'Naive':20} {naive_comps:>15} {'2(n-1)':>20}")
    print()
    reduction = ((naive_comps - dc_comps) / naive_comps) * 100
    print(f"Improvement: {reduction:.1f}%")


def performance_analysis():
    """Analyze performance across different array sizes."""
    print()
    print("=" * 70)
    print("PERFORMANCE ANALYSIS")
    print("=" * 70)
    print()
    
    print(f"{'Size':>8} {'DC Comps':>12} {'Naive Comps':>14} {'Formula 3n/2-2':>16} {'Actual':>10}")
    print('-' * 70)
    
    for size in [10, 100, 1000, 10000]:
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        # D&C approach
        global comparison_count
        comparison_count = 0
        mn, mx = min_max_dc(arr, 0, len(arr) - 1)
        dc = comparison_count
        
        # Naive approach
        _, _, naive = min_max_naive(arr)
        
        # Theoretical formula
        formula = 3 * size // 2 - 2
        
        print(f"{size:>8} {dc:>12} {naive:>14} {formula:>16} {dc==formula:>10}")


def verify_correctness():
    """Verify correctness of both algorithms."""
    print()
    print("=" * 70)
    print("CORRECTNESS VERIFICATION")
    print("=" * 70)
    print()
    
    test_cases = [
        [5],
        [5, 3],
        [3, 5],
        [3, 1, 4, 1, 5, 9, 2, 6],
        list(range(1, 11)),
        list(range(10, 0, -1))
    ]
    
    for arr in test_cases:
        global comparison_count
        comparison_count = 0
        
        dc_min, dc_max = min_max_dc(arr, 0, len(arr) - 1)
        naive_min, naive_max, _ = min_max_naive(arr)
        built_min, built_max = min(arr), max(arr)
        
        dc_correct = (dc_min == built_min and dc_max == built_max)
        naive_correct = (naive_min == built_min and naive_max == built_max)
        
        print(f"Array: {arr}")
        print(f"  D&C:    min={dc_min}, max={dc_max} {'✓' if dc_correct else '✗'}")
        print(f"  Naive:  min={naive_min}, max={naive_max} {'✓' if naive_correct else '✗'}")
        print()


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 5: MIN-MAX USING DIVIDE AND CONQUER")
    print("=" * 70)
    print()
    
    demonstrate_on_small_array()
    verify_correctness()
    performance_analysis()
    
    print()
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("D&C reduces comparisons from 2(n-1) to 3n/2 - 2 (25% improvement)")
    print("Theoretically optimal for simultaneous min-max finding")
    print("Critical in parallel processors where comparison cost is high")
    print("=" * 70)


if __name__ == "__main__":
    main()
