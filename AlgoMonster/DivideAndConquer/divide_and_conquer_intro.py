"""
Divide and Conquer

There are three types of divide and conquer problems. The first type of problem mainly 
focuses on binary search aspect of divide and conquer. The second type of problems 
focuses on different types of sorting algorithms and how they can be incorporated into 
divide and conquer questions. The third type of problems is generalizied divide and 
conquer problem. We will discuss each one of these seperately in the coming tutorials.

The main idea of divide and conquer problem is splitting the main problem into two 
smaller components, assume that each one of the components have already been solved 
recursively and then try to solve the bigger problem using the solution of the two 
smaller components. For example, merge sort is a perfect case of a divide and conquer 
problem.

In merge sort, we first divide the array given into two components, the first half and
the second half. After dividing them into these two components, we then recursively 
apply merge sort algorithm on each of these components and assume they are already
sorted. Now the problem becomes given two sorted arrays, how do we merge them into one
sorted array. We can use a pointer on each of these sorted arrays to solve the last part 
of the problem.

"""