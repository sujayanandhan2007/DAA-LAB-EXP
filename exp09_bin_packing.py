"""
Experiment 9: Efficient Bin Packing using Approximation Algorithms

Algorithm Description:
    Three approximation algorithms for bin packing problem:
    1. First Fit (FF): Place item in first bin with enough space
    2. First Fit Decreasing (FFD): Sort items descending, then FF
    3. Best Fit Decreasing (BFD): Sort descending, place in best-fit bin

Problem: Pack items into minimum number of bins of fixed capacity.

Approximation Ratios:
    - FF: 17/10 * OPT + 6/10
    - FFD: 11/9 * OPT + 6/9 (much better in practice)
    - BFD: Similar to FFD

Time Complexity: O(n²) for FFD/BFD
Space Complexity: O(n)

Key Insight: FFD achieves near-optimal results in practice despite being
             heuristic (greedy). Sorting is the key improvement.

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""


def first_fit(items, capacity=1.0):
    """
    First Fit Algorithm
    
    Args:
        items: List of item sizes
        capacity: Bin capacity
        
    Returns:
        list: Packing solution (bins with items)
    
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    bins = []  # Remaining space in each bin
    bin_contents = []  # Items in each bin
    
    for item in items:
        placed = False
        
        # Try to place in first bin with enough space
        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break
        
        # If not placed, open new bin
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])
    
    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    """
    First Fit Decreasing Algorithm
    
    Sort items in decreasing order, then apply First Fit.
    Usually achieves better results than plain First Fit.
    
    Args:
        items: List of item sizes
        capacity: Bin capacity
        
    Returns:
        list: Packing solution (bins with items)
    
    Time Complexity: O(n log n) for sort + O(n²) for FF = O(n²)
    Space Complexity: O(n)
    """
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    """
    Best Fit Decreasing Algorithm
    
    Sort items in decreasing order, place each in bin with minimum
    remaining space that can fit it (best fit).
    
    Args:
        items: List of item sizes
        capacity: Bin capacity
        
    Returns:
        list: Packing solution (bins with items)
    
    Time Complexity: O(n²) for placement
    Space Complexity: O(n)
    """
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        
        # Find bin with minimum remaining space that fits item
        for i, space in enumerate(bins):
            if space >= item and space - item < best_space:
                best_space = space - item
                best_idx = i
        
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            # Open new bin
            bins.append(capacity - item)
            bin_contents.append([item])
    
    return bin_contents


def next_fit(items, capacity=1.0):
    """
    Next Fit Algorithm (for comparison)
    
    Only try to place item in current bin, move to next if full.
    Simplest but worst approximation.
    
    Args:
        items: List of item sizes
        capacity: Bin capacity
        
    Returns:
        list: Packing solution
    
    Time Complexity: O(n)
    """
    bins = []
    bin_contents = []
    current_space = 0
    
    for item in items:
        if current_space >= item:
            bins[-1] -= item
            bin_contents[-1].append(item)
            current_space -= item
        else:
            bins.append(capacity - item)
            bin_contents.append([item])
            current_space = capacity - item
    
    return bin_contents


def display_bins(label, bins, capacity=1.0):
    """
    Display bin packing solution with visualization
    
    Args:
        label: Algorithm name
        bins: Packing solution
        capacity: Bin capacity
    """
    total_used = sum(sum(b) for b in bins)
    
    print(f"\n{label}: {len(bins)} bins used")
    for i, b in enumerate(bins, 1):
        used = sum(b)
        percentage = (used / capacity) * 100
        bar_length = int(used * 20)
        bar = '#' * bar_length
        items_str = ', '.join(f'{x:.1f}' for x in b)
        print(f"  Bin {i}: [{items_str}]")
        print(f"          Used: {used:.1f}/{capacity} ({percentage:.0f}%) "
              f"[{bar:<20}]")


def demonstrate_bin_packing():
    """Demonstrate bin packing algorithms."""
    items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
    capacity = 1.0
    
    # Calculate lower bound
    lower_bound = -(-sum(items) // capacity)  # Ceiling division
    
    print("Items:", items)
    print(f"Capacity: {capacity}")
    print(f"Sum of items: {sum(items):.1f}")
    print(f"Theoretical lower bound on bins: {int(lower_bound)}")
    print()
    
    # Apply algorithms
    ff_bins = first_fit(items)
    ffd_bins = first_fit_decreasing(items)
    bfd_bins = best_fit_decreasing(items)
    nf_bins = next_fit(items)
    
    display_bins("First Fit (FF)", ff_bins)
    display_bins("Next Fit (NF)", nf_bins)
    display_bins("First Fit Decreasing (FFD)", ffd_bins)
    display_bins("Best Fit Decreasing (BFD)", bfd_bins)
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Lower Bound: {int(lower_bound)}")
    print(f"Next Fit:    {len(nf_bins)} bins")
    print(f"First Fit:   {len(ff_bins)} bins")
    print(f"FFD:         {len(ffd_bins)} bins")
    print(f"BFD:         {len(bfd_bins)} bins")


def performance_analysis():
    """Analyze performance across different scenarios."""
    print()
    print()
    print("=" * 70)
    print("PERFORMANCE ANALYSIS")
    print("=" * 70)
    print()
    
    import random
    
    print(f"{'Items':>6} {'Lower Bound':>12} {'NF':>5} {'FF':>5} {'FFD':>5} {'BFD':>5}")
    print('-' * 50)
    
    for num_items in [10, 20, 50, 100]:
        # Generate random items
        items = [round(random.uniform(0.1, 0.9), 1) for _ in range(num_items)]
        capacity = 1.0
        
        lower_bound = int(-(-sum(items) // capacity))
        nf_bins = len(next_fit(items))
        ff_bins = len(first_fit(items))
        ffd_bins = len(first_fit_decreasing(items))
        bfd_bins = len(best_fit_decreasing(items))
        
        print(f"{num_items:>6} {lower_bound:>12} {nf_bins:>5} {ff_bins:>5} "
              f"{ffd_bins:>5} {bfd_bins:>5}")


def approximation_ratios():
    """Demonstrate approximation ratios."""
    print()
    print()
    print("=" * 70)
    print("APPROXIMATION RATIO ANALYSIS")
    print("=" * 70)
    print()
    
    import random
    
    print("Theoretical bounds:")
    print("  Next Fit (NF): 2 * OPT")
    print("  First Fit (FF): 17/10 * OPT + 6/10")
    print("  FFD/BFD: 11/9 * OPT + 6/9")
    print()
    
    # Run multiple trials
    trials = 20
    results = {'NF': [], 'FF': [], 'FFD': [], 'BFD': []}
    
    for _ in range(trials):
        items = [round(random.uniform(0.1, 0.9), 1) for _ in range(50)]
        capacity = 1.0
        
        lb = int(-(-sum(items) // capacity))
        
        if lb > 0:
            nf = len(next_fit(items)) / lb
            ff = len(first_fit(items)) / lb
            ffd = len(first_fit_decreasing(items)) / lb
            bfd = len(best_fit_decreasing(items)) / lb
            
            results['NF'].append(nf)
            results['FF'].append(ff)
            results['FFD'].append(ffd)
            results['BFD'].append(bfd)
    
    print(f"{'Algorithm':<10} {'Avg Ratio':>12} {'Min':>10} {'Max':>10}")
    print('-' * 45)
    for algo in ['NF', 'FF', 'FFD', 'BFD']:
        if results[algo]:
            avg = sum(results[algo]) / len(results[algo])
            print(f"{algo:<10} {avg:>12.3f} {min(results[algo]):>10.3f} "
                  f"{max(results[algo]):>10.3f}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 9: BIN PACKING USING APPROXIMATION ALGORITHMS")
    print("=" * 70)
    print()
    
    demonstrate_bin_packing()
    performance_analysis()
    approximation_ratios()
    
    print()
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("FFD/BFD achieve near-optimal results despite being greedy")
    print("Sorting is crucial - FFD much better than plain FF")
    print("O(n log n) time makes FFD practical for real-world applications")
    print("Applications: Cloud resource allocation, truck loading,")
    print("memory management, multi-processor scheduling")
    print("=" * 70)


if __name__ == "__main__":
    main()
