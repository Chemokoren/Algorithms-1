def quicksort(A):
    low, high= 0, len(A)-1
    def rec_quick_sort(A, low, high):
        if low < high:
            p = partition(A, low, high)
            rec_quick_sort(A, low, p-1)
            rec_quick_sort(A, p+1, high)
        return A
    return rec_quick_sort(A, low, high)

def quicksort2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quicksort2(A, low, p-1)
        quicksort2(A, p+1, high)

def partition(A, low, high):
    i = low -1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] =A[high], A[i+1]

    return i + 1

A=[84, 21, 96, 15, 47]
print('Expected:[15, 21, 47, 84, 96], Actual:', quicksort([84, 21, 96, 15, 47]))
print(f'Original:{A}')
quicksort2(A, 0, len(A)-1)
print(f'After Sorting:{A}')



