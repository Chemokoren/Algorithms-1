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

Approach
- The idea is to traverse each row or column(depending on given direction) from side x of row or
column towards x'(opposite of x). For example, if the given value of x is 'l' (left) then start
scanning each row from left side to right. While traversing, store row or column element in the
temporary 1-D array (say temp[]) by skipping elements having value 0 and sum of the consecutive
element if they have equal value. After that, start copying the temporary array temp[0..k] to the
the current row or column from the x side(of row or column) to x'(opposite x) and fill reset of 
the element by 0.

Let, x='l' i.e move towards left. So, start copying each row from left most index to right most
index of the row and store in temporary array with processing of ignoring 0s and adding two 
consecutive element into one if they have same value. Below is the illustration for row 1,

2   9   <--     1   1   0   0   9   Row1
                                    Row2
                                    Row3
                                    Row4
                                    Row5

Now, for each, copy temporary array to current row from left most index to right most index. Below
is illustration for row 1

2   9   -->     2   9   0   0   0   Row1
                                    Row2
                                    Row3
                                    Row4
                                    Row5


Time Complexity: O(n2)
Auxiliary Space: O(n), since n extra space has been taken.


"""
# move matrix elements in given direction with add element with same value
MAX = 50
# Function to shift the matrix in the given direction
def move_matrix(a):

    n = len(a)
    d = ["l"] * 2

    # for right shift move
    if(d[0]=='r'):
        # for each row from top to bottom
        for i in range(n):
            v =[]
            w =[]

            # for each element of row from right to left
            for j in range(n-1, -1, -1):

                # if not 0
                if(a[i][j]):
                    v.append(a[i][j])

                # for each temporary array
                j = 0
                while(j < len(v)):
                    # if two elements have same value at consecutive position
                    if(j < len(v) -1 and v[j]==v[j+1]):
                        # Insert only one element as sum of two same element
                        w.append(2*v[j])
                        j+=1
                    else:
                        w.append(v[j])
                    j +=1

                # Filling each row element to 0
                for j in range(n):
                    a[i][j] = 0

                j = n-1

                # copying the temporary array to the current row
                for it in w:
                    a[i][j] = it
                    j -=1

    # for left shift move
    elif(d[0] == 'l'):
        # for each row
        for i in range(n):
            v =[]
            w =[]

            # for each element of the row from left to right
            for j in range(n):
                # if not 0
                if(a[i][j]):
                    v.append(a[i][j])
            # for each temporary array
            j =0
            while(j < len(v)):
                # if two elements have same value at consecutive position
                if(j < len(v) -1 and v[j]==v[j+1]):
                    # Insert only one element as sum of two same element
                    w.append(2*v[j])
                    j+=1

                else:
                    w.append(v[j])

                j += 1

            # Filling the each row element to 0
            for j in range(n):
                a[i][j] =0

            j = 0
            for it in w:
                a[i][j] = it
                j += 1

    # for down shift move
    elif(d[0] =='d'):

        # for each column
        for i in range(n):
            v =[]
            w =[]

            # for each element of column from bottom to top
            for j in range(n-1, -1, -1):
                # if not 0
                if(a[j][i]):
                    v.append(a[j][i])

            # For each temporary array
            j = 0
            while(j < len(v)):
                # if two elements have same value at consecutive position
                if(j < len(v) -1 and v[j]==v[j+1]):

                    # insert only one element as sum of two same element
                    w.append(2*v[j])
                    j +=1
                else:
                    w.append(v[j])

                j += 1

            # Filling the each column element to 0
            for j in range(n):
                a[j][i] =0
            j = n-1

            # copying the temporary array to the current column
            for it in w:
                a[j][i] = it
                j -=1


    # for up shift move
    elif(d[0] =='u'):
        # for each column
        for i in range(n):
            v =[]
            w =[]

            # For each element of column from top to bottom
            for j in range(n):
                # if not 0 
                if(a[j][i]):
                    v.append(a[j][i])

            # For each temporary array
            j = 0
            while(j < len(v)):
                # if two elements have same value at consecutive position
                if(j < len(v) -1 and v[j]==v[j+1]):

                    # Insert only one element as sum of two same element
                    w.append(2*v[j])
                    j +=1

                else:
                    w.append(v[j])

                j +=1

            # Filling the each column element to 0
            for j in range(n):
                a[j][i] = 0

            j = 0

            # copying the temporary array to the current column
            for it in w:
                a[j][i]=it
                j +=1




a = [ [ 32, 3, 3, 3, 3 ],
          [ 0, 0, 1, 0, 0 ],
          [ 10, 10, 8, 1, 2 ],
          [ 0, 0, 0, 0, 1 ],
          [ 4, 5, 6, 7, 8 ] ]
 
move_matrix(a)
 
# Printing the final array
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end = " ")
 
    print()
 























