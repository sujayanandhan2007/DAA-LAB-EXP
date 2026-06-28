"""
Experiment 1: Implementation and Performance Analysis of Interpolation Search

Algorithm Description:
    Interpolation Search estimates the position of a target element in a sorted
    array using the interpolation formula, similar to how we search in a phone
    book. It works best on uniformly distributed sorted data.

Time Complexity: O(log log n) average case, O(n) worst case
Space Complexity: O(1)

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import time
import random


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    
    Args:
        arr: Sorted list of integers
        target: Element to search for
        
    Returns:
        tuple: (index of target, number of comparisons)
               (-1, comparisons) if not found
    
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        
        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons
        
        # Interpolation formula to estimate probe position
        pos = low + int(((target - arr[low]) * (high - low)) /
                        (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm (for comparison)
    
    Args:
        arr: Sorted list of integers
        target: Element to search for
        
    Returns:
        tuple: (index of target, number of comparisons)
               (-1, comparisons) if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons


def demonstrate_search():
    """Demonstrate interpolation search on a small example."""
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35
    
    idx, comps = interpolation_search(arr, target)
    
    print(f"Array: {arr}")
    print(f"Searching for: {target}")
    print(f"Found at index: {idx}, Comparisons: {comps}")
    print()


def performance_analysis():
    """Analyze performance of Interpolation Search vs Binary Search."""
    sizes = [1000, 5000, 10000, 50000, 100000]
    
    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
          f"{'IS Comps':>12} {'BS Comps':>12}")
    print('-' * 70)
    
    for size in sizes:
        # Generate sorted uniformly distributed array
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]
        
        # Interpolation Search timing
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000
        
        # Binary Search timing
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000
        
        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} "
              f"{comp_is:>12} {comp_bs:>12}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 1: INTERPOLATION SEARCH")
    print("=" * 70)
    print()
    
    demonstrate_search()
    performance_analysis()
    
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("Interpolation Search outperforms Binary Search on uniformly")
    print("distributed sorted data with O(log log n) complexity.")
    print("=" * 70)


if __name__ == "__main__":
    main()
