"""
# https://github.com/MaximumBeings/GoogleCodingInterviewQuestions

Write a function that given an array A consisting of N integers returns the maximum sum
of two numbers whoose digits add up to an equal sum. If there are no two numbers whose
digits have an equal sum, the function should return -1

Examples: 
1. Given A =[51,71,17,42] the function should return 93. There are two pairs of numbers
whose digits add up to an equal sum:
(51,42) and (17,71). The first pair sums up to 93.

2. Given A=[42,33,60], the function should return 102. The digits of all numbers in A
add up to the same and choosing to add 42 and 60 gives the result of 102.

3. Given A =[51,32,43], the function should return -1, since all numbers in A have 
digits that add up to different, unique sums.

Write an efficient algorithm for the following assumptions:

-  N is an integer within the range[1 .. 200,000]
-  Each element of array A is an integer within the range [1..1,000,000,000]
"""

def max_sum_of_numbers(arr):
    have_same_sum ={}
    final_arr =[]
    current_sum= 0
    for i in arr:
        sum_val =sum([int(x) for x in str(i)])
        if sum_val not in have_same_sum:
            have_same_sum[sum_val]=[]
        have_same_sum[sum_val].append(i)
    if len(have_same_sum) == len(arr):
        return -1
    
    for i in have_same_sum:
        if len(have_same_sum[i]) >2:
            k =0
            w =1
            import itertools

            array = itertools.permutations(have_same_sum[i])
            for eachpermutation in array:
                print("anii:",sum(list(eachpermutation)))

            
            # while w < len(have_same_sum[i]):
            #     new_sum =have_same_sum[i][k] + have_same_sum[i][w]
            #     if(new_sum > current_sum):
            #         current_sum = new_sum
            #         k +=1
            #         w +=1
            # final_arr.append([have_same_sum[i][k-1],have_same_sum[i][w-1]])
        else:
            if( sum(have_same_sum[i]) > current_sum):
                current_sum = sum(have_same_sum[i])
                final_arr.append(have_same_sum[i])
            
        # print("woloo: ",current_sum)
            

    return current_sum, final_arr

# arr =[51,71,17,42]
arr =[42,33,60]
# arr =[51,32,43]
print(max_sum_of_numbers(arr))


# approach 2

input =[51, 71, 17,42]
input2 =[42, 33, 60]
input3 =[51,32, 43]
input4 = [598888888,688888888,5988888881111,6888888881111]
input5 = [5,9,6,8]
input6 = [59,68]

def stringAdder(digit):
    digit =str(digit)
    temp = 0
    res =[temp + int(x) for x in digit]
    return sum(res)

def stringChecker(input):
    res =[stringAdder(str(input[0]))]
    for x in range(1, len(input)):
        t = stringAdder(str(input[x]))
        if t not in res:
            pass
        elif t in res:
            res.append(t)
    if len(res) == 1:
        return False
    else:
        return True

def codeInteger(input):
    max_ = 0
    temp =[]
    if stringChecker(input) != False:
        for x in range(0, len(input),1):
            toUse = stringAdder(str(input[x]))
            for y in range(1, len(input), 1):
                toUse2 = stringAdder(input[y])
            if toUse == toUse2:
                temp.append(input[x]+input[y])
                break
    if len(temp) != 0:
        return max(temp)
    return -1


#test
print(codeInteger(input))
print(codeInteger(input2))
print(codeInteger(input3))
print(codeInteger(input4))
print(codeInteger(input5))
print(codeInteger(input6))