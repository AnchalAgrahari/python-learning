## DATA STRUCTURE: 
a perticular way of Organizing and storing data.
linear dataStructure : accessed in a sequential order but it is not compulsory to stor ass the element sequentily. like stack and queues
non-linear dataStructure : stored in a non-linear order . like tree and graphs

## ABSTRACT DATATYPE :
 to simplify the process of solving the problem , we combine the dataStructure with theri problem and  we call this ADts. 
decleration of data 
decleration of operation
#### ADTs : 
Linked Lists, Stacks, Queues, proritty queues,Binary Trees, Dictionary, Disjoint Sets(Union and Find), Hash table, Graphs
like stacks uses LIFO(Last In First Out) 

## ALGORITHM : 
An algoritm is the step by step unambiguous instruction to solve the problem.
we have 2 criteria for judging the merits of the algorithm :
1. **Correctness** – Does it solve the problem accurately?
2. **Efficiency** – Does it do so using minimal time and space?

## ANALYSIS/GOAL  of Algorithim : 
The goal of algorithm analysis is to determine which algorithm is more efficient, mainly in terms of:
 - **Time complexity**
 - **Space complexity**

It may also involve other factors like:

- **Memory usage**
- **Developer effort**
- **Readability / maintainability**

RUNNING TIME ANALYSIS 

## HOW TO COMPARE ALGORITHMS : 
1. **Execution time** – How long does it take to run?
2. **Number of statements executed** – How much work is being done internally?
3. **Ideal solution** – Can we do better? Is it optimal?
## RATE of GROWTH :
        ### Commonly Used Rates of Growth:

| Time Complexity | Name                | Example                                                 |
|-----------------|---------------------|---------------------------------------------------------|
| 1               | Constant            | Adding element to the front of a linked list            |
| log n           | Logarithmic         | Finding an element in a sorted array                    |
| n               | Linear              | Finding an element in an unsorted array                 |
| n log n         | Linear Logarithmic  | Sorting n elements using divide-and-conquer (mergesort) |
| n²              | Quadratic           | Shortest path between two nodes in a graph              |
| n³              | Cubic               | Matrix multiplication                                   |
| 2ⁿ              | Exponential         | The Tower of Hanoi problem                              |

// Relatipship between different Rate of Growth :
        1 -> log logn -> √logn -> log^2 n -> 2 ^logn -> n -> log(n!) -> n logn -> n^2 -> 2^n -> 4^n -> n! -> 2^2^n


#### we have 3 type of analysis :
 1. worst case : slowest time to complete(Omega Ω)
 2. best case : fastest time to complete ( Big-O)
 3. aveerage case                       (Theta θ)
                LOWER BOUND <= Average Time <= UPPER BOUND

**Big -O  Notation (WORST case)**
It gives the upper bound of an algorithm
It describe the performance or complexity of an algorithim in term of time(how much time it takes) and space(how much memory it uses)

**Omega (Ω)  Notation (BEST case)**
It gives lower bound of an algorithm
I describe the best case performance or complexity of an algorithm -- how fast it can run or what is the least amount of time or step algorithem could take.

**Theta (θ) Notation (AVERAGE/EXACT case)**
It gives the tight bound of an algorithim.
It means the agorithm always takes about the same time no matter the case it is best or worst 

## Asymptotic Analysis :
It tells us how fast or slow an algorithm becomes when the input size increases.

Asymptotic Analysis is the mathematical way of evaluating the efficiency of algorithms by focusing on their growth rate as input size approaches infinity.

**Why do we use it?**
1. Actual running time depends on hardware, compiler, coding style → not reliable for comparison.
2. Asymptotic analysis ignores machine-dependent constants and focuses only on the growth rate of the algorithm.

### Guideline for Asymptotic Analysis 
we have some genarel rules to help us determine the running time of the Algorithim.

1. **Loops** : The runnig time of the loop is at most, the runtime of the statement inside the loops multiplied by the the number of iterations.
 -  Total Time = a constant c * n = Cₙ = O(n).
2. **Nested Loop** : Analysis fron inside out. Total running time si the product of size of all loops 
 - Total Time = c * n * n = O(n²).
3. **Consecutive statement** : Add the time complexities for each statment.
 - Total tile = C₀ + C₁ n + C₂ n² = O(n²).
4. **If-else-statment** : worst case running time . the test plus either  the then part or the else part
 -  Total time = C₀ + C₁ * n = O(n).
5. **Loagrithim Compliexity** : An algorithm is  O(*logn*) if ti take constant time to cut th eproblem size by fraction.
 - Total time = O(*logn*)
