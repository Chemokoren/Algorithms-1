"""
Find unique elements in a matrix

Given a matrix mat[][] having n rows and m columns. We need to find unique elements in a matrix 
i.e., thos eelements which are not repeated in a matrix or those element whose frequency is 1.

Examples: 

Input :  20  15  30  2
         2   3   5   30
         6   7   6   8
Output : 3  20  5  7  8  15 

Input :  1  2  3  
         5  6  2
         1  3  5
         6  2  2
Output : No unique element in the matrix

Follow these steps to find unique element:
1. Create an empty hash table or dictionary
2. Traverse through all the elements of the matrix
3. If element is present in the dictionary, then increment its count
4. Otherwise insert element with value =1

    Time Complexity: O(m*n) where m is the number of rows & n is the number of columns.
    Auxiliary Space: O(max(matrix)). 
    
"""
# program to find unique element in matrix
def unique(mat):
    n = 4
    m = 4
    maximum = 0
    flag = 0
    for i in range(0, n):
        for j in range(0, m):
            # find maximum element in a matrix
            if(maximum < mat[i][j]):
                maximum = mat[i][j]
    uniqueElementDict =[0] * (maximum+1)

    # loops to traverse through the matrix
    for i in range(0, n):
        for j in range(0, m):
            uniqueElementDict[mat[i][j]] +=1

    # Print all those keys whose count is 1
    for key in range(maximum+1):
        if uniqueElementDict[key] ==1:
            print(key, end=" ")
            flag = 1
    if(flag == 0):
        print("No unique element in the matrix")


mat = [[1, 2, 3, 20],
       [5, 6, 20, 25],
       [1, 3, 5, 6],
       [6, 7, 8, 15]]
unique(mat)


print("\n my tests \n")
def my_tests(mat):
    dic =dict()
    res =[]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dic[mat[i][j]] =dic.get(mat[i][j],0) +1
    
    for k, v in dic.items():
        if v == 1:
            res.append(k)

    return res

mat =[
        [20,15,30,2],
        [2, 3, 5, 30],
        [6, 7, 6, 8]
        ]

mat1 =[
     [1, 2, 3 ],
     [5, 6, 2 ],
     [1, 3, 5 ],
     [6, 2, 2 ]
]
print("Expected:[ 3  20  5  7  8  15 ], Actual", my_tests(mat))
print("Expected:[], Actual", my_tests(mat1))