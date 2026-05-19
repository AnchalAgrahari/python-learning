## Why Do We Use Asymptotic Analysis?

1. Actual running time depends on hardware, compiler, and coding style — making it unreliable for fair comparison between algorithms.
2. Asymptotic analysis ignores machine-dependent constants and focuses solely on the **growth rate** of an algorithm as input size increases.

---

## Guidelines for Asymptotic Analysis

These general rules help determine the time complexity of an algorithm:

### 1. Loops
The running time of a loop is at most the running time of the statement(s) inside the loop, multiplied by the number of iterations.
> Total Time = c × n = **O(n)**

### 2. Nested Loops
Analyze from the innermost loop outward. The total running time is the product of the sizes of all loops.
> Total Time = c × n × n = **O(n²)**

### 3. Consecutive Statements
Add the time complexities of each statement individually, then take the dominant term.
> Total Time = C₀ + C₁n + C₂n² = **O(n²)**

### 4. If-Else Statements
Take the worst-case running time — the condition check plus whichever branch (then or else) takes longer.
> Total Time = C₀ + C₁ × n = **O(n)**

### 5. Logarithmic Complexity
An algorithm is O(log n) if it takes constant time to reduce the problem size by a constant fraction
(e.g., halving the input each step, as in binary search).
> Total Time = **O(log n)**

---

## Algorithm Analysis

The goal of algorithm analysis is to predict the resources (primarily **time** and **space**) an algorithm
requires without implementing it. We express this using **Big-O notation**, which describes the upper bound
on growth rate and allows us to compare algorithms in a machine-independent way.

| Complexity   | Name          | Example              |
|--------------|---------------|----------------------|
| O(1)         | Constant      | Array index access   |
| O(log n)     | Logarithmic   | Binary search        |
| O(n)         | Linear        | Linear search        |
| O(n log n)   | Linearithmic  | Merge sort           |
| O(n²)        | Quadratic     | Bubble sort          |
| O(2ⁿ)        | Exponential   | Recursive Fibonacci  |