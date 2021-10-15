"""
            1   3   4   10

            2   5   9   11
            
            6   8   12  15

            7   13  14  16

Output =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

"""

# O(n) time | O(n) space
def zigzagTraverse(array):
    height =len(array) -1
    width = len(array[0]) -1
    result = []
    row, col = 0,0
    goingDown = True
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col +=1
                else:
                    row +=1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col +=1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

my_array=[[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]

print(zigzagTraverse(my_array))