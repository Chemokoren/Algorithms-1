def moveElmentToEnd(array, target):
    startIdx = 0
    lastIdx = len(array) -1

    while startIdx <= lastIdx:
        if array[startIdx] == target and array[lastIdx] !=target:
            swap(startIdx,lastIdx, array)
            startIdx +=1
            lastIdx -=1
        elif array[startIdx] != target:
            startIdx +=1

        elif array[lastIdx] ==target:
            lastIdx -= 1
    return array

def swap(i, j, array):
    array[i],array[j] =array[j],array[i]

#[1,3,4,2,2,2,2,3]
my_array =[2,1,2,2,2,3,4,2]
target= 2

print(moveElmentToEnd(my_array,target))
