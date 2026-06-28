"""
Experiment 2: Comparative Analysis of String Matching Algorithms

Algorithm Description:
    Three classic string matching algorithms are implemented and compared:
    1. Naive Search: Brute force substring matching
    2. KMP (Knuth-Morris-Pratt): Uses a failure function for efficiency
    3. Rabin-Karp: Uses rolling hash for pattern matching

Time Complexity:
    - Naive: O(n*m) worst case
    - KMP: O(n+m)
    - Rabin-Karp: O(n+m) average, O(n*m) worst case

Space Complexity:
    - Naive: O(1)
    - KMP: O(m) for LPS array
    - Rabin-Karp: O(1)

Author: Design and Analysis of Algorithms Lab
Institution: Chennai Institute of Technology
"""

import random
import string


def naive_search(text, pattern):
    """
    Naive String Matching Algorithm
    
    Args:
        text: Text string to search in
        pattern: Pattern string to find
        
    Returns:
        tuple: (list of match positions, number of comparisons)
    
    Time Complexity: O(n*m)
    Space Complexity: O(1)
    """
    n, m = len(text), len(pattern)
    matches, comparisons = [], 0
    
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
    
    return matches, comparisons


def compute_lps(pattern):
    """
    Compute Longest Proper Prefix which is also Suffix array for KMP
    
    Args:
        pattern: Pattern string
        
    Returns:
        list: LPS array for the pattern
    """
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    
    return lps


def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt String Matching Algorithm
    
    Args:
        text: Text string to search in
        pattern: Pattern string to find
        
    Returns:
        tuple: (list of match positions, number of comparisons)
    
    Time Complexity: O(n+m)
    Space Complexity: O(m)
    """
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches, comparisons = [], 0
    i = j = 0
    
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches, comparisons


def rabin_karp(text, pattern, q=101):
    """
    Rabin-Karp Algorithm using rolling hash
    
    Args:
        text: Text string to search in
        pattern: Pattern string to find
        q: Prime number for modulo operation
        
    Returns:
        tuple: (list of match positions, number of comparisons)
    
    Time Complexity: O(n+m) average
    Space Complexity: O(1)
    """
    n, m = len(text), len(pattern)
    d = 256  # Number of characters in alphabet
    h = pow(d, m - 1, q)
    p_hash = t_hash = 0
    matches, comparisons = [], 0
    
    # Calculate hashes of pattern and first window
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    
    # Slide the pattern over text
    for s in range(n - m + 1):
        if p_hash == t_hash:
            # Verify character by character
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)
        
        # Calculate hash of next window
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + 
                     ord(text[s + m])) % q
            if t_hash < 0:
                t_hash += q
    
    return matches, comparisons


def demonstrate_algorithms():
    """Demonstrate all three string matching algorithms."""
    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print()
    
    m1, c1 = naive_search(text, pattern)
    m2, c2 = kmp_search(text, pattern)
    m3, c3 = rabin_karp(text, pattern)
    
    print(f"Naive  -> Matches at: {m1}, Comparisons: {c1}")
    print(f"KMP    -> Matches at: {m2}, Comparisons: {c2}")
    print(f"RK     -> Matches at: {m3}, Comparisons: {c3}")
    print()


def performance_comparison():
    """Compare performance on larger text."""
    text_large = ''.join(random.choices('ABCD', k=10000))
    patterns = ['AB', 'ABCD', 'ABCDAB', 'ABCDABCD']
    
    print(f"{'Pattern':>12} {'Naive':>10} {'KMP':>10} {'RK':>10}")
    print('-' * 50)
    
    for p in patterns:
        _, c1 = naive_search(text_large, p)
        _, c2 = kmp_search(text_large, p)
        _, c3 = rabin_karp(text_large, p)
        print(f"{p:>12} {c1:>10} {c2:>10} {c3:>10}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("EXPERIMENT 2: STRING MATCHING ALGORITHMS")
    print("=" * 70)
    print()
    
    demonstrate_algorithms()
    performance_comparison()
    
    print()
    print("=" * 70)
    print("CONCLUSION:")
    print("KMP achieves O(n+m) by avoiding re-comparisons.")
    print("Rabin-Karp uses hash filtering for efficiency with longer patterns.")
    print("KMP is best for single-pattern matching in general text.")
    print("=" * 70)


if __name__ == "__main__":
    main()
