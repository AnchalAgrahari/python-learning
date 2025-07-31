DATA STRUCTURE: a perticular way of Organizing and storing data.
linear dataStructure : accessed in a sequential order but it is not compulsory to stor ass the element sequentily. like stack and queues
non-linear dataStructure : stored in a non-linear order . like tree and graphs

ABSTRACT DATATYPE : to simplify the process of solving the problem , we combine the dataStructure with theri problem and  we call this ADts. 
decleration of data 
decleration of operation
ADTs : Linked Lists, Stacks, Queues, proritty queues,Binary Trees, Dictionary, Disjoint Sets(Union and Find), Hash table, Graphs
like stacks uses LIFO(Last In First Out) 

ALGORITHM : An algoritm is the step by step unambiguous instruction to solve the problem.
we have 2 criteria for judging the merits of the algorithm : 1: correctness , 2: efficiency 

ANALYSIS/GOAL  of Algorithim : helps to detremine which algo is more efficient mainly in term of time and space  factor but also in other( memory,developer effort etc)
RUNNING TIME ANALYSIS 

HOW TO COMPARE ALGO : 
        1. execution time?
        2. number of statement executed?
        3. ideal solution?

RATE of GROWTH :
        commanilly use RATE of GROWTH :
        +-----------------------+-----------------------+------------------------------------------------------------+
        | Time Complexity       | Name                  | Example                                                    |
        +-----------------------+-----------------------+------------------------------------------------------------+  
        |        1              | Constant              |  adding element to the front of a linked list              |
        |      logn             | logirithimic          |  finding an element in a sorted array                      |
        |       n               | linear                |  finding an element in an unsorted array                   |
        |      nlogn            | linear logirithmic    |  sorting n element by divide-and-conqure   -mergsort       |
        |       n^2             | quadratic             |  shortest path between two nodes in graph                  |
        |       n^3             | cubic                 |  matrix multiplication                                     |
        |       2^n             | exponential           |  the tower of hanoi problem                                |
        +-----------------------+-----------------------+------------------------------------------------------------+

we have 3 type of analysis :
 1. worst case : slowest time to complete(Omega Ω)
 2. best case : fastest time to complete ( Big-O)
 3. aveerage case                       (Theta θ)
                LOWER BOUND <= Average Time <= UPPER BOUND




