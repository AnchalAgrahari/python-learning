DATA STRUCTURE: a perticular way of Organizing and storing data.
linear dataStructure : accessed in a sequential order but it is not compulsory to stor ass the element sequentily. like stack and queues
non-linear dataStructure : stored in a non-linear order . like tree and graphs

ABSTRACT DATATYPE : to simplify the process of solving the problem , we combine the dataStructure with theri problem and  we call this ADts. 
decleration of data 
decleration of operation
ADTs : Linked Lists, Stacks, Queues, proritty queues,Binary Trees, Dictionary, Disjoint Sets(Union and Find), Hash table, Graphs
like stacks uses LIFO(Last In First Out) 

ALGORITHM : An algoritm is the step by step unambiguous instruction to solve the problem.
we have 2 criteria for judging the merits of the algorithm :
1. **Correctness** – Does it solve the problem accurately?
2. **Efficiency** – Does it do so using minimal time and space?

ANALYSIS/GOAL  of Algorithim : The goal of algorithm analysis is to determine which algorithm is more efficient, mainly in terms of:
        - **Time complexity**
        - **Space complexity**

It may also involve other factors like:

- **Memory usage**
- **Developer effort**
- **Readability / maintainability**

RUNNING TIME ANALYSIS 

HOW TO COMPARE ALGO : 
        1. execution time?
        2. number of statement executed?
        3. ideal solution?

RATE of GROWTH :
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


we have 3 type of analysis :
 1. worst case : slowest time to complete(Omega Ω)
 2. best case : fastest time to complete ( Big-O)
 3. aveerage case                       (Theta θ)
                LOWER BOUND <= Average Time <= UPPER BOUND




