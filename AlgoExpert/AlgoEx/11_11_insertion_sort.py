# O(n^2) | O(1) time
def insertionSort(array):
    for i in range(1, len(array)):
        print(i)
        while i>0 and array[i] < array[i-1]:
            swap(i,i-1,array)
            i -=1
        
    return array


def swap(i, j, array):
    array[i],array[j] =array[j], array[i]

my_array =[8,5,2,9,5,6]

# print(insertionSort(my_array))
insertionSort(my_array)