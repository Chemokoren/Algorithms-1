"""
Python program for creating a hollow diamond pattern
"""
def drawHollowDiamondPattern(n):
    """

    :param n: is the number of rows for the diamond pattern
    :return:
    """
    k = 0

    '''
    drawing the upper triangular shape
    '''
    for j in range(1, n + 1):

        # first,print the spaces
        for p in range(1, n - j + 1):
            print(" ", end="")

        # secondly,print *
        while (k != (2 * j - 1)):
            if (k == 0 or k == 2 * j - 2):
                print("#", end="")
            else:
                print(" ", end="")
            k = k + 1

        k = 0

        # finally, proceed to next row
        print(""),

    n = n - 1

    '''
    drawing the lower triangular shape
    '''
    for j in range(n, 0, -1):
        #first, print the spaces
        for p in range(0, n - j + 1):
            print(" ", end="")

        # secondly, print *
        k = 0
        while (k != (2 * j - 1)):
            if (k == 0 or k == 2 * j - 2):
                print("#", end="")
            else:
                print(" ", end="")
            k = k + 1

        print(""),


'''
Driver code to test the program
'''
if __name__=='__main__':
    # number_of_rows = int(input('Input the Number of rows : '))
    number_of_rows = 8
    drawHollowDiamondPattern(number_of_rows)



# Python program to print a hollow
# pyramid pattern
#
# def printPattern(n):
#     k = 0
#     for i in range(1, n + 1):  # row 6
#
#         # Print spaces
#         for j in range(i, n):
#             print(' ', end='')
#
#         # Print #
#         while (k != (2 * i - 1)):
#             if (k == 0 or k == 2 * i - 2):
#                 print('#', end='')
#             else:
#                 print(' ', end='')
#             k = k + 1
#         k = 0;
#         print("")  # print next row
#
#     # print last row
#     for i in range(0, 2 * n - 1):
#         print('#', end='')
#
#
# # Driver code
# n = 6
# printPattern(n)