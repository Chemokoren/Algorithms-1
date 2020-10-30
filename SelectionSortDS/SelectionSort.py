class SelectionSort(object):
    def SelectionSort(self,arr):
        for i in range(len(arr) - 2):
            minIndex = i

            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp

        return arr

# def SelectionSortDS(arr):
#     for i in range(len(arr) - 2):
#         minIndex = i
#
#         for j in range(i+1,len(arr)):
#             if  arr[j] < arr[minIndex]:
#                 minIndex =j
#         temp = arr[minIndex]
#         arr[minIndex] = arr[i]
#         arr[i] =temp
#
#     return arr
#
# myArr=[3,6,9,5,8,7,1,22,11,45,33,10,38]
# print(SelectionSortDS(myArr))
