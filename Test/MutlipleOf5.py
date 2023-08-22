# Python code to check
# if a number is multiple of
# 5 without using / and %

# Assumes that n is a positive integer
def isMultipleof5(n):
    while (n > 0):
        n = n - 5

    if (n == 0):
        return 1

    return 0

print(isMultipleof5(22))

# # Driver Code
# i = 19
# if (isMultipleof5(i) == 1):
#     print(i, "is multiple of 5")
# else:
#     print(i, "is not a multiple of 5")
#
# # This code is contributed
# # by Sumit Sudhakar
