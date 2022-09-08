"""
Move matrix elements in given direction and add elements with same value

Given a matrix m[][] of size n*n consisting of integers and given a character 'x' indicating
the direction. Value of 'x' can be 'u','d','l','r' indicating Up, Down, Left, Right 
correspondingly. The task is to move the element to given direction such that the consecutive 
elements having same value are added into single value and shift the rest element. Also, shift the
element if the next element in given direction is 0.

Consider x = ‘l’ and matrix m[][], 
32 3 3 
0 0 1 
10 10 8
After adding 3 in first row, 10 in third row and moving 1 in second row, 
Matrix will become 
32 6 0 
1 0 0 
20 8 0

Examples :  

Input : x = 'l'
m[][] = { { 32, 3, 3, 3, 3 },
          { 0, 0, 1, 0, 0 },
          { 10, 10, 8, 1, 2},
          { 0, 0, 0, 0, 1},
          { 4, 5, 6, 7, 8 } }
Output :
32 6 6 0 0
1 0 0 0 0
20 8 1 2 0
1 0 0 0 0 0
4 5 6 7 8

Input : x = 'u'
m[][] = { { 10, 3, 32 },
        { 10, 0, 96 },
        { 5, 32, 96 } }
Output :
20 3 32
5 32 192
0 0 0

"""