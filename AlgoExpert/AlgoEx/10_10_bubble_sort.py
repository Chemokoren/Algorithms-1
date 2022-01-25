def bubbleSort(array):
    """
    bubbles up the value with the highest value to the right most array and repeats the
    process till it is sorted

    parameters:
        array: takes an array as the input.
    """
    issorted =False
    counter = 0
    while not issorted:
        issorted =True
        for i in range(len(array)-1-counter):
            if array[i]> array[i+1]:
                swap(i,i+1,array)
                issorted=False
        counter +=1
    return array

def swap(i, j, array):
    array[i],array[j] = array[j], array[i]


my_array =[8,5,2,9,5,6,3]

print("bubble sort: ", bubbleSort(my_array))