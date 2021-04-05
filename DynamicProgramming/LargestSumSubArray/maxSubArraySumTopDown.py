# Python Function to get a subarray that adds up to a given sum using hashing
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
        print(sub_array_indexes)

        # insert (current sum, current index) pair into the dictionary
        sub_array_indexes[initial_sum] = i
    print("no subarray found with the given sum has been found!")


if __name__ == '__main__':
    # sample list of integers and expected sum value to test the max sub array sum
    array_ = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    sum_ = 15

    # array_ = [15, 2, 4, 8, 9, 5, 10, 23]
    # sum_ = 23

    # array_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # sum_ = 6





    findSublist(array_, sum_)