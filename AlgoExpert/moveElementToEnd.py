my_array = [2,1,2,2,2,3,4,2]
val_to_move =2

def moveElementToEnd(array,toMove):
    i =0
    j =len(array)-1

    while i < j:
        while i < j and array[j] == toMove:
            j -=1
        if array[i] == toMove:
            array[i],array[j] =array[j],array[i]
        i +=1
    return array


print(moveElementToEnd(my_array, val_to_move))