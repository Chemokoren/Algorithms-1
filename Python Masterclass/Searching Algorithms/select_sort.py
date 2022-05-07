"""
Similar to bubble sort, but instead of first placing large values into sorted position, it places small 
values into sorted position

Selection Sort Pseudocode
- Store the first element as the smallest value you've seen so far.
- Compare this item to the next item in the array until you find a smaller number
- If a small number is found, designate that smaller number to be the new "minimum" and continue until 
the the end of the array.
- If the "minimum" is not the value(index) you initially began with, swap the two values.
-Repeat this with the next element until the array is sorted.


"""
def selection_sort(arr):
    
    
    for i in range(len(arr)):
        smallest =i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[smallest]):
                    smallest =j
        if(i != smallest):
            arr[smallest], arr[i] =arr[i], arr[smallest]
    return arr
            
print(selection_sort([5,3,4,1,2]))