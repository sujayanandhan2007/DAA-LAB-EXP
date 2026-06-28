# Design and Analysis of Algorithms (DAA) - Laboratory Manual

**Institution:** Chennai Institute of Technology  
**Department:** Computer Science and Engineering  
**Subject Code:** AD5303  
**Program:** B.Tech - Artificial Intelligence and Data Science  
**Semester:** III Semester  
**Credits:** 3 L : 0 T : 2 P : 4 C

---

## 📋 Experiment List

| Exp | Title | Filename | Algorithm Paradigm | Complexity |
|-----|-------|----------|-------------------|-----------|
| 1 | Implementation and Performance Analysis of Interpolation Search | `exp01_interpolation_search.py` | Searching | O(log log n) avg |
| 2 | Comparative Analysis of String Matching (Naive, KMP, RK) | `exp02_string_matching.py` | Pattern Matching | O(n+m) |
| 3 | Minimum Spanning Tree (Kruskal's & Prim's) | `exp03_mst_kruskal_prim.py` | Greedy Graphs | O(E log E) |
| 4 | Single Source Shortest Path (Dijkstra's) | `exp04_dijkstra.py` | Greedy Graphs | O((V+E)log V) |
| 5 | Min-Max using Divide and Conquer | `exp05_min_max_divide_conquer.py` | Divide & Conquer | O(n) |
| 6 | Matrix Chain Multiplication (DP) | `exp06_matrix_chain_multiplication.py` | Dynamic Programming | O(n³) |
| 7 | N-Queens Problem (Backtracking) | `exp07_n_queens.py` | Backtracking | O(N!) |
| 8 | Travelling Salesman Problem (Branch & Bound) | `exp08_tsp_branch_bound.py` | Branch & Bound | O(n!) |
| 9 | Bin Packing (Approximation Algorithms) | `exp09_bin_packing.py` | Approximation | O(n log n) |
| 10 | Randomized Quick Sort | `exp10_randomized_quicksort.py` | Randomized Algorithms | O(n log n) expected |

---

## 🔧 Requirements

### Python Version
- **Python 3.6 or higher** (Recommended: Python 3.8+)

### External Libraries
None! All experiments use only Python's standard library:
- `heapq` - For priority queue implementations
- `random` - For generating random data
- `time` - For performance measurements
- `itertools` - For permutations (TSP)
- `sys` - For system operations
- `math` - For mathematical functions (N-Queens analysis)

### Installation
No additional package installation required. The code is completely self-contained.

---

## ▶️ How to Run Each Experiment

### Single Experiment Execution
```bash
python exp01_interpolation_search.py
python exp02_string_matching.py
python exp03_mst_kruskal_prim.py
python exp04_dijkstra.py
python exp05_min_max_divide_conquer.py
python exp06_matrix_chain_multiplication.py
python exp07_n_queens.py
python exp08_tsp_branch_bound.py
python exp09_bin_packing.py
python exp10_randomized_quicksort.py
```

### Run All Experiments
```bash
# On Linux/macOS
for exp in exp*.py; do
    echo "====== Running $exp ======"
    python "$exp"
    echo ""
done

# On Windows
for /R %f in (exp*.py) do python %f
```

### Run with Output Redirection
```bash
# Save output to file
python exp01_interpolation_search.py > output_exp01.txt
```

---

## 📊 Experiment Descriptions

### Exp 1: Interpolation Search
- **Goal:** Implement interpolation search and compare with binary search
- **Key Features:**
  - Efficiently handles uniformly distributed sorted data
  - O(log log n) average complexity vs O(log n) for binary search
  - Performance analysis on datasets of 1K to 100K elements

### Exp 2: String Matching
- **Goal:** Compare Naive, KMP, and Rabin-Karp algorithms
- **Key Features:**
  - Naive: O(n*m) brute force
  - KMP: O(n+m) using failure function
  - Rabin-Karp: O(n+m) avg using rolling hash
  - Detailed comparison on 10K character text

### Exp 3: Minimum Spanning Tree
- **Goal:** Find MST using Kruskal's and Prim's algorithms
- **Key Features:**
  - Union-Find data structure with path compression
  - Priority queue implementation for Prim's
  - Both algorithms guarantee optimal solution
  - 7-vertex, 11-edge test graph

### Exp 4: Dijkstra's Algorithm
- **Goal:** Find shortest paths from single source
- **Key Features:**
  - Min-heap priority queue for efficiency
  - Path reconstruction
  - Handles directed weighted graphs
  - Works only with non-negative edge weights

### Exp 5: Divide and Conquer Min-Max
- **Goal:** Find minimum and maximum simultaneously with optimal comparisons
- **Key Features:**
  - D&C: 3n/2 - 2 comparisons
  - Naive: 2(n-1) comparisons
  - 25% reduction in comparisons
  - Theoretically optimal for simultaneous min-max

### Exp 6: Matrix Chain Multiplication
- **Goal:** Find optimal parenthesization for matrix multiplication
- **Key Features:**
  - Dynamic Programming: O(n³) vs exponential brute force
  - DP table construction and trace
  - Path reconstruction for optimal order
  - Example: 4 matrices (10×30, 30×5, 5×60, 60×10)

### Exp 7: N-Queens Problem
- **Goal:** Find all valid queen placements using backtracking
- **Key Features:**
  - Constraint satisfaction via backtracking
  - Diagonal attack detection
  - Solutions for N=4, 6, 8
  - Visual board display

### Exp 8: Travelling Salesman Problem
- **Goal:** Find minimum cost Hamiltonian cycle
- **Key Features:**
  - Brute force for small instances (n<10)
  - NP-Hard problem analysis
  - Nearest neighbor heuristic comparison
  - 5-city test problem

### Exp 9: Bin Packing
- **Goal:** Pack items into minimum bins using approximation algorithms
- **Key Features:**
  - First Fit (FF): Simple but suboptimal
  - First Fit Decreasing (FFD): O(n²) with good approximation
  - Best Fit Decreasing (BFD): Similar to FFD
  - Theoretical approximation ratios

### Exp 10: Randomized Quick Sort
- **Goal:** Compare deterministic vs randomized Quick Sort
- **Key Features:**
  - Deterministic: O(n²) worst case on sorted data
  - Randomized: O(n log n) expected on any input
  - Performance analysis on different input types
  - Worst-case demonstration

---

## 📈 Performance Metrics Collected

Each experiment measures:

1. **Correctness**
   - Output verification against expected results
   - Solution validation

2. **Efficiency**
   - Time complexity analysis
   - Comparison count or operation count
   - Actual execution time in milliseconds

3. **Scalability**
   - Performance on different input sizes
   - Trend analysis (linear, logarithmic, quadratic, exponential)

4. **Comparative Analysis**
   - Algorithm comparison on same inputs
   - Approximation ratio measurement

---

## 🎯 Learning Outcomes

After completing this lab, students will:

1. ✅ Implement classic algorithms from pseudocode
2. ✅ Analyze time and space complexity theoretically and empirically
3. ✅ Compare different algorithmic approaches for same problem
4. ✅ Understand algorithm paradigms:
   - Searching & Sorting
   - Divide & Conquer
   - Greedy Algorithms
   - Dynamic Programming
   - Backtracking
   - Branch & Bound
   - Randomized Algorithms
   - Approximation Algorithms

5. ✅ Apply algorithms to real-world problems

---

## 💻 Code Quality Standards

All experiments follow:

1. **PEP 8 Style Guide**
   - Proper indentation (4 spaces)
   - Meaningful variable names
   - Clear function documentation

2. **Documentation**
   - Module docstring
   - Function docstrings with Args, Returns, Time/Space complexity
   - Inline comments for complex logic

3. **Structure**
   - Modular functions
   - No unnecessary global variables
   - Proper main() function with if __name__ == "__main__"

4. **Correctness**
   - Input validation
   - Error handling
   - Output verification

---

## 📝 Example Usage

### Running Experiment 1
```bash
$ python exp01_interpolation_search.py

======================================================================
EXPERIMENT 1: INTERPOLATION SEARCH
======================================================================

Array: [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
Searching for: 35
Found at index: 5, Comparisons: 2

      Size   IS Time(ms)   BS Time(ms)  IS Comps  BS Comps
-------------------------------------------------------------
      1000        0.0021        0.0035        3       10
      5000        0.0025        0.0042        3       13
     10000        0.0028        0.0048        4       14
     50000        0.0031        0.0061        4       16
    100000        0.0035        0.0068        5       17

======================================================================
CONCLUSION:
Interpolation Search outperforms Binary Search on uniformly
distributed sorted data with O(log log n) complexity.
======================================================================
```

---

## 🔗 Related Topics & Extensions

### Suggested Extensions
1. **Exp 1:** Implement interpolation search with binary search hybrid
2. **Exp 2:** Add Boyer-Moore string matching algorithm
3. **Exp 3:** Implement with adjacency matrix for dense graphs
4. **Exp 4:** Add Bellman-Ford for negative edge weights
5. **Exp 5:** Extend to find k-th smallest element
6. **Exp 6:** Add memoization (top-down DP)
7. **Exp 7:** Implement using bit manipulation for faster is_safe
8. **Exp 8:** Add 2-opt local search improvement
9. **Exp 9:** Implement Next Fit and other variants
10. **Exp 10:** Add Median-of-Three pivot selection

### Real-World Applications
- **Exp 1:** Database indexing (phone books)
- **Exp 2:** Plagiarism detection, text search
- **Exp 3:** Network design, cable laying
- **Exp 4:** GPS navigation, OSPF routing
- **Exp 5:** Hardware optimization
- **Exp 6:** Compiler optimization, 3D rendering
- **Exp 7:** VLSI circuit design, constraint satisfaction
- **Exp 8:** Logistics, delivery routing, DNA sequencing
- **Exp 9:** Cloud resource allocation, memory management
- **Exp 10:** Practical sorting in production systems

---

## 🔍 Verification & Testing

### How Outputs Were Verified

Each experiment includes:
1. **Sample output from manual** - Expected results
2. **Generated output from code** - Actual results  
3. **Comparison** - Verification that they match

### Test Cases Provided

- **Small examples** - For manual verification
- **Edge cases** - Minimum sizes, boundary conditions
- **Large datasets** - For performance analysis
- **Different input types** - Random, sorted, reverse-sorted, etc.

---

## 📚 References

### Algorithm Resources
- **Textbook:** Introduction to Algorithms (CLRS)
- **Topics:** Algorithm design, analysis, and implementation
- **Complexity:** Time and space complexity analysis

### Python Resources
- Python Official Documentation: https://docs.python.org/3/
- Data Structures: https://docs.python.org/3/tutorial/datastructures.html

---

## ✍️ Author & Acknowledgments

**Lab Manual Implementation**  
Institution: Chennai Institute of Technology  
Department: Computer Science and Engineering  
Faculty: Mrs. A. Gayathri

**Code Quality:** Clean, well-documented, PEP 8 compliant  
**Testing:** Verified against sample outputs from manual

---

## 📄 License & Usage

These algorithms and implementations are provided for educational purposes.
Use them to learn algorithm design and analysis.

---

## ❓ FAQ

**Q: Can I use these files for assignment submission?**  
A: Yes, but ensure you understand and can explain each algorithm.

**Q: What if I get different performance numbers?**  
A: Normal! Performance depends on system hardware, background processes, etc.

**Q: How do I extend these experiments?**  
A: See "Suggested Extensions" section above.

**Q: Which experiments are hardest?**  
A: Typically Exp 7, 8, 10 require deeper understanding.

**Q: Can these handle larger inputs?**  
A: Most can, but some (like TSP) will be slow due to exponential complexity.

---

## 🚀 Quick Start

```bash
# 1. Navigate to DAA_Lab directory
cd DAA_Lab

# 2. Run all experiments
python exp0*.py

# 3. Check output for correctness
# All experiments print "CONCLUSION" at end with key insights

# 4. Modify and experiment!
# Try different input sizes, array types, etc.
```

---

**Happy Learning! 🎓**

For questions or clarifications, refer to the pseudocode in each experiment
or consult your course materials.
