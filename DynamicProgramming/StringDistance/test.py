# def maxSubArraySum2(a, size):
#     max_so_far = - 1
#     max_ending_here = 0
#     start = 0
#     end = 0
#     s = 0
#
#     for i in range(0, size):
#
#         max_ending_here += a[i]
#
#         if max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#             start = s
#             end = i
#
#         if max_ending_here < 0:
#             max_ending_here = 0
#             s = i + 1
#
#     print("Maximum contiguous sum is %d" % (max_so_far))
#     print("Starting Index %d" % (start))
#     print("Ending Index %d" % (end))
#
#
# if __name__=='__main__':
#     arr = [15, 2, 4, 8, 9, 5, 10, 23]
#     expected_sum = 23
#     maxSubArraySum2(arr, expected_sum)


def findSublist(arr_, expected_sum):
    # insert `(0, -1)` pair into the set to handle the case when a
    # subarray with the given sum starts from index 0
    sub_array_indexes = {0: -1}

    # keep track of the sum of elements so far
    initial_sum = 0

    # traverse the original array
    for i in range(len(arr_)):

        # update initial_sum
        initial_sum += arr_[i]

        # if `initial_sum - expected_sum` is seen before, we have found
        # the subarray with expected_sum `expected_sum`
        if (initial_sum - expected_sum) in sub_array_indexes:
            print("subarray found between indexes (inclusive): ", (sub_array_indexes.get(initial_sum - expected_sum) + 1, i))
            return

        # insert (current sum, current index) pair into the dictionary
        sub_array_indexes[initial_sum] = i
    print("no subarray found with the given sum has been found!")


if __name__ == '__main__':
    # sample list of integers and expected sum value to test the max sub array sum
    array_ = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    sum_ = 15
    findSublist(array_, sum_)

    # array_ = [15, 2, 4, 8, 9, 5, 10, 23]
    # sum_ = 23


print(" ############################### my new test ################################ ")


# implementation program to convert RGB color code to Hex color code

# Function to convert decimal to hexadecimal
def decimalToHexa(n):
    # char array to store hexadecimal number
    hexaDecimalNumber = ['0'] * 100

    # hexadecimal's counter number array
    i = 0

    while (n != 0):

        #  remainder is stored in a temporary variable named __temp
        _temp = 0

        # Storing remainder in _temp variable.
        _temp = n % 16

        # Check if _temp < 10
        if (_temp < 10):
            hexaDecimalNumber[i] = chr(_temp + 48)
            i = i + 1

        else:
            hexaDecimalNumber[i] = chr(_temp + 55)
            i = i + 1

        n = int(n / 16)

    hexadecimalCode = ""
    if (i == 2):
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[1]

    elif (i == 1):
        hexadecimalCode = "0"
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]

    elif (i == 0):
        hexadecimalCode = "00"

    # Return the equivalent of hexadecimal color code
    return hexadecimalCode


# Function to convert the RGB to Hexadecimal color code
def RGBtoHexConverion(R, G, B):
    if ((R >= 0 and R <= 255) and
            (G >= 0 and G <= 255) and
            (B >= 0 and B <= 255)):

        hexadecimalCode = "#"
        hexadecimalCode = hexadecimalCode + decimalToHexa(R)
        hexadecimalCode = hexadecimalCode + decimalToHexa(G)
        hexadecimalCode = hexadecimalCode + decimalToHexa(B)
        return hexadecimalCode

    # If the hexadecimal color code does not exist return -1
    else:
        return "-1"


# main method to test the program code
if __name__=='__main__':
    R = 255
    G = 255
    B = 256
    print(RGBtoHexConverion(R, G, B))

    R = 0
    G = 0
    B = 0
    print(RGBtoHexConverion(R, G, B))

    R = 255
    G = 255
    B = 255
    print(RGBtoHexConverion(R, G, B))

    R = 25
    G = 56
    B = 123
    print(RGBtoHexConverion(R, G, B))

    R = 2
    G = 3
    B = 4
    print(RGBtoHexConverion(R, G, B))



