
def merge(arr1, arr2):
    i = 0
    j = 0
    res =[]

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i +=1
        else:
            res.append(arr2[j])
            j +=1

    while i < len(arr1):
        res.append(arr1[i])
        i +=1

    while j < len(arr2):
        res.append(arr2[j])
        j +=1
    return res


 
def merge_sort(nums):

    def in_merge_sort(start, end, nums):
        if start >= end:
            return [nums[start]]
        
        mid = (start + end) // 2
        left = nums[start:mid + 1]
        right = nums[mid + 1:end + 1]
        
        left = in_merge_sort(0, len(left) - 1, left)
        right = in_merge_sort(0, len(right) - 1, right)
        
        return merge(left, right)
    
    return in_merge_sort(0, len(nums)-1, nums)

print(merge_sort([4, 1, 3, 2, 0, -1, 7, 10, 9, 20]))