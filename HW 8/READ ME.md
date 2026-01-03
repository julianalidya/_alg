Similarities and Differences between Lookup Table and Dynamic Programming versions of $C(n,k)$

1. Similarities
```text
Mathematical Basis: Both methods are based on Pascal's identity, where $C(n, k) = C(n-1, k-1) + C(n-1, k)$.
Efficiency Goal: Both approaches aim to solve the performance issues of pure recursion by storing intermediate results to avoid redundant calculations.
Base Cases: Both versions define the same base cases where $C(n, k) = 1$ if $k=0$ or $k=n$.
```

2. Differences
Direction of Calculation: The Dynamic Programming version (Reference 1) uses a "Bottom-up" approach, starting from the smallest subproblems and filling the table using loops. The Lookup Table version (Reference 2) uses a "Top-down" approach, starting from the target $C(n, k)$ and recursing downwards only when a value is missing.
Implementation Method: The Dynamic Programming version is implemented using nested "for-loops" (iteration). The Lookup Table version is implemented using a recursive function combined with a "memoization" check.
Table Filling: The Dynamic Programming version pre-fills the entire relevant portion of the $N \times N$ table. The Lookup Table version only fills the specific cells needed to reach the final answer, leaving other cells empty (None).
Memory Initialization: The Dynamic Programming version typically initializes the array based on the input size $N$ during runtime. The Lookup Table version in the provided reference uses a pre-defined global array of fixed size (e.g., 100x100).
