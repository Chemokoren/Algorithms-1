"""
Shortest path to reach one prime to other by changing single digit at a time

Given two four digit prime numbers, suppose 1033 and 8179, we need to find the shortest 
path from 1033 to 8179 by altering only single digit at a time such that every number 
that we get after changing a digit is prime. For example a solution is 1033, 1733,
3733, 3739, 3779, 8779, 8179

Examples:

Input : 1033 8179
Output :6

Input : 1373 8017
Output : 7

Input  :  1033 1033
Output : 0

The question can be solved by BFS and it is pretty interesting to solve as a starting
problem for beginners. We first find out all 4 digit prime numbers till 9999 using
technique of sieve of eratosthenes. And then using those numbers formed  the graph using
adjacency list. After forming the adjacency list, we used simple BFS to solve the 
problem.
"""
# program to reach a prime number from another changing single digits and using only prime
# numbers
import queue

class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.l =[[] for i in range(V)]

    def addedge(self, V1, V2):
        self.l[V1].append(V2)
        self.l[V2].append(V1)

# in1 and in2 are two vertices of graph which are actually indexes in pset[]
def bfs(self, in1, in2):
    visited =[0] * self.V
    que = queue.Queue()
    visited[in1] = 1
    que.put(in1)
    while(not que.empty()):
        p = que.queue[0]
        que.get()
        i = 0
        while i < len(self.l[p]):
            if(not visited[self.l[p][i]]):
                visited[self.l[p][i]] = visited[p] + 1
                que.put(self.l[p][i])
            if (self.l[p][i] == in2):
                return visited[self.l[p][i]] -1
            i += 1

    # returns true if num1 and num differ by single digit.

# Finding all 4 digit prime numbers
def sieveOfEratosthenes(v):
    # Create a boolean array "prime[0 .. n]" and  initialize  all the entries it as true.
    # A value  in prime[i] will finally be false if i is not a prime, else true.
    n = 9999
    prime =[True] * (n + 1)

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if(prime[p] == True):
            # update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False

    p += 1

    # Forming a vector of prime numbers
    for p in range(1000, n + 1):
        if(prime[p]):
            v.append(p)

def compare(num1, num2):

    # To compare the digits
    s1 = str(num1)
    s2 = str(num2)
    c = 0
    if(s1[0] != s2[0]):
        c += 1
    if(s1[1] != s2[1]):
        c += 1
    if(s1[2] != s2[2]):
        c += 1
    if(s1[3] != s2[3]):
        c += 1

    # If the numbers differ only by a single difit return true else false
    return(c == 1)

def shortestPath(num1, num2):
    # Generate all 4 digit
    pset = []
    sieveOfEratosthenes(pset)

    # Create a graph where node numbers are indexes in pset[] and there is an 
    # edge between two nodes only if they differ by a single  digit.
    g = Graph(len(pset))
    for i in range(len(pset)):
        for j in range(i + 1, len(pset)):
            if(compare(pset[i], pset[j])):
                g.addedge(i, j)

    # since graph nodes represent indexes of numbers in pset[], we find indexes of num1
    # and num2

    in1, in2 = None, None
    for j in range(len(pset)):
        if(pset[j] == num1):
            in1 = j
    for j in range(len(pset)):
        if(pset[j] == num2):
            in2 = j

    return g.bfs(in1, in2)


if __name__ == '__main__':
  
    num1 = 1033
    num2 = 8179
    print(shortestPath(num1, num2))




