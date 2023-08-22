def maxSum(arr, windowsize):
    arraysize = len(arr)
    if(arraysize <= windowsize):
        print("Not Possible")
        return -1

    # compute the summation of the first window of size k
    window_sum = sum(arr[i] for i in range(windowsize))
    # before going into any window, the maximum will be the sum of first window
    max_sum = window_sum 

    # compute sums of remaining windows by removing first element of previous 
    # window and adding last element of the current window

    for i in range(arraysize-windowsize):
        window_sum = window_sum-arr[i] + arr[i+ windowsize] 
        max_sum = max(window_sum, max_sum)

    return max_sum

arr =[1, 2, 100, -1, 5]
k = 3

answer = maxSum(arr, k)
print(answer)