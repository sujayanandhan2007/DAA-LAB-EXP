"""
Experiment 10: Improving Quick Sort Efficiency using Randomized Algorithm

Algorithm Description:
    Compares two Quick Sort variants:
    1. Deterministic Quick Sort: Always uses last element as pivot
       - Can degrade to O(n²) on sorted/reverse-sorted arrays
    
    2. Randomized Quick Sort: Randomly selects pivot
       - Guarantees expected O(n log n) regardless of input
       - Avoids adversarial cases through randomization

Time Complexity:
    - Deterministic: O(n²) worst case, O(n log n) average
    - Randomized: O(n log n) expected, O(n²) worst case with negligible probability

Space Complexity: O(log n) for recursion stack (average)

Key Insight: Randomization trades determinism for robustness against
             worst-case inputs. Practical sorting algorithms use this.

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import random
import time
import sys

# Increase recursion limit for large arrays
sys.setrecursionlimit(20000)

# Global counter for comparisons
comparisons = 0


def partition(arr, low, high):
    """
    Partition array using last element as pivot
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index
        
    Returns:
        int: Partition index
    
    Time Complexity: O(n)
    """
    global comparisons
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low, high):
    """
    Standard Quick Sort with last element as pivot
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    
    Time Complexity: O(n²) worst case, O(n log n) average
    Space Complexity: O(log n) recursion
    """
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


def randomized_quicksort(arr, low, high):
    """
    Quick Sort with random pivot selection
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    
    Time Complexity: O(n log n) expected, O(n²) worst case
    Space Complexity: O(log n) recursion
    
    Randomization Strategy:
        Randomly select pivot from low to high, swap with last element
    """
    if low < high:
        # Randomize pivot by swapping random element to end
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        
        pi = partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def run_test(sort_fn, arr):
    """
    Run sorting test and collect metrics
    
    Args:
        sort_fn: Sorting function
        arr: Array to sort
        
    Returns:
        tuple: (comparisons, time in milliseconds)
    """
    global comparisons
    a = arr[:]
    comparisons = 0
    
    start = time.perf_counter()
    sort_fn(a, 0, len(a) - 1)
    elapsed = (time.perf_counter() - start) * 1000
    
    # Verify sorting
    assert a == sorted(a), "Array not sorted correctly!"
    
    return comparisons, elapsed


def generate_test_cases(n):
    """
    Generate different types of test arrays
    
    Args:
        n: Array size
        
    Returns:
        dict: Test cases with labels
    """
    test_cases = {}
    
    # Random array
    test_cases['Random'] = [random.randint(1, 100000) for _ in range(n)]
    
    # Already sorted
    test_cases['Sorted'] = list(range(n))
    
    # Reverse sorted
    test_cases['Reverse'] = list(range(n, 0, -1))
    
    # Nearly sorted (slightly shuffled)
    nearly_sorted = list(range(n))
    for _ in range(n // 20):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
    test_cases['Nearly Sorted'] = nearly_sorted
    
    return test_cases


def demonstrate_worst_case():
    """Show deterministic QS worst case behavior."""
    print("=" * 70)
    print("WORST CASE DEMONSTRATION")
    print("=" * 70)
    print()
    
    print("Deterministic Quick Sort (pivot = last element) worst case:")
    print("  - Sorted array: Each pivot splits at edge (n, 1) -> O(n²)")
    print("  - Reverse sorted: Same problem")
    print()
    
    n = 1000
    sorted_arr = list(range(n))
    
    global comparisons
    comparisons = 0
    dqs_copy = sorted_arr[:]
    deterministic_quicksort(dqs_copy, 0, n - 1)
    dqs_comps = comparisons
    
    comparisons = 0
    rqs_copy = sorted_arr[:]
    randomized_quicksort(rqs_copy, 0, n - 1)
    rqs_comps = comparisons
    
    print(f"Array: Already sorted, n={n}")
    print(f"  Deterministic QS: {dqs_comps:,} comparisons")
    print(f"  Randomized QS:    {rqs_comps:,} comparisons")
    print()
    ratio = dqs_comps / rqs_comps if rqs_comps > 0 else float('inf')
    print(f"Deterministic QS is {ratio:.1f}x slower!")
    print()


def performance_comparison():
    """Compare performance across different input types."""
    print()
    print("=" * 70)
    print("PERFORMANCE COMPARISON (N=5000)")
    print("=" * 70)
    print()
    
    n = 5000
    test_cases = generate_test_cases(n)
    
    print(f"{'Input Type':<16} {'DQS Comps':>12} {'DQS Time(ms)':>14} "
          f"{'RQS Comps':>12} {'RQS Time(ms)':>14}")
    print('-' * 72)
    
    for case, arr in test_cases.items():
        d_comps, d_time = run_test(deterministic_quicksort, arr)
        r_comps, r_time = run_test(randomized_quicksort, arr)
        
        print(f"{case:<16} {d_comps:>12} {d_time:>14.2f} "
              f"{r_comps:>12} {r_time:>14.2f}")


def scaling_analysis():
    """Analyze scaling behavior as array size increases."""
    print()
    print()
    print("=" * 70)
    print("SCALING ANALYSIS (Random Input)")
    print("=" * 70)
    print()
    
    print(f"{'Size':>8} {'DQS Time(ms)':>14} {'RQS Time(ms)':>14} {'Ratio':>10}")
    print('-' * 50)
    
    for n in [1000, 2000, 5000, 10000]:
        arr = [random.randint(1, 100000) for _ in range(n)]
        
        _, d_time = run_test(deterministic_quicksort, arr)
        _, r_time = run_test(randomized_quicksort, arr)
        
        ratio = d_time / r_time if r_time > 0 else 0
        print(f"{n:>8} {d_time:>14.2f} {r_time:>14.2f} {ratio:>10.2f}x")


def verify_stability():
    """Verify algorithm correctness across multiple runs."""
    print()
    print()
    print("=" * 70)
    print("STABILITY TEST (10 Random Runs, N=1000)")
    print("=" * 70)
    print()
    
    n = 1000
    
    print(f"{'Run':>3} {'Array Type':<15} {'DQS OK':>8} {'RQS OK':>8}")
    print('-' * 40)
    
    for run in range(10):
        arr_type = random.choice(['Random', 'Sorted', 'Reverse'])
        
        if arr_type == 'Random':
            arr = [random.randint(1, 10000) for _ in range(n)]
        elif arr_type == 'Sorted':
            arr = list(range(n))
        else:
            arr = list(range(n, 0, -1))
        
        # Test DQS
        dqs_arr = arr[:]
        try:
            deterministic_quicksort(dqs_arr, 0, n - 1)
            dqs_ok = dqs_arr == sorted(arr)
        except:
            dqs_ok = False
        
        # Test RQS
        rqs_arr = arr[:]
        try:
            randomized_quicksort(rqs_arr, 0, n - 1)
            rqs_ok = rqs_arr == sorted(arr)
        except:
            rqs_ok = False
        
        print(f"{run+1:>3} {arr_type:<15} {'✓' if dqs_ok else '✗':>8} "
              f"{'✓' if rqs_ok else '✗':>8}")


def comparison_analysis():
    """Theoretical comparison of algorithms."""
    print()
    print()
    print("=" * 70)
    print("THEORETICAL COMPARISON")
    print("=" * 70)
    print()
    
    print("Deterministic Quick Sort:")
    print("  ✓ Predictable (same execution each run)")
    print("  ✗ Vulnerable to adversarial inputs (sorted arrays)")
    print("  - Worst case: O(n²) [Very unlikely with random data]")
    print("  - Average: O(n log n)")
    print()
    
    print("Randomized Quick Sort:")
    print("  ✓ Robust against adversarial inputs")
    print("  ✓ Expected O(n log n) regardless of input")
    print("  - Theoretical worst case: O(n²) [Negligible probability]")
    print("  - Average: O(n log n)")
    print()
    
    print("Practical Implications:")
    print("  - Real sorting libraries (Python, C++, Java) use randomization")
    print("  - Python's Timsort: Uses randomization + mergesort hybrid")
    print("  - C++ std::sort: Introsort (QS + Heapsort fallback)")
    print("  - Java Arrays.sort: DualPivotQuicksort with randomization")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 10: RANDOMIZED QUICK SORT")
    print("=" * 70)
    print()
    
    demonstrate_worst_case()
    performance_comparison()
    scaling_analysis()
    verify_stability()
    comparison_analysis()
    
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("Randomized Quick Sort avoids O(n²) worst case through randomization")
    print("Achieves expected O(n log n) on ANY input distribution")
    print("Trades determinism for robustness - practical sorting standard")
    print("Demonstrates power of randomized algorithms in algorithm design")
    print("=" * 70)


if __name__ == "__main__":
    main()
