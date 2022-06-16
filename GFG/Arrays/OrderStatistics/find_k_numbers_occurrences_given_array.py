"""
Find k numbers with most occurrences in the given array

Given an array of n numbers and a postive integer k. The problem is to find k numbers with most 
occurrences, i.e., the top k numbers having the maximum frequency. If two numbers have the same
frequency then the larger number should be given preference.  The numbers should be displayed 
in decreasing order of their frequencies. It is assumed that the array consists of k numbers 
with most occurrences.

Examples:

Input: 
arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, 
k = 2
Output: 4 1
Explanation:
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and
4 is larger than 1.

Input : 
arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
k = 4
Output: 5 11 7 10
Explanation: 
Frequency of 5 = 3
Frequency of 11 = 2
Frequency of 7 = 2
Frequency of 10 = 1
These four have the maximum frequency and
5 is largest among rest.

Approach:
The through process should begin from creating a HashMap to store element-frequency pair in the
HashMap. HashMap is used to perform insertion and update in constant time. Then sort the
element-frequency pair in decreasing order of frequency. This gives the information about each
element and the number of times they are present in the array. To get k elements of the array,
print the first k elements of the sorted array.

Hashmap:

HashMap is part of Java's collection since Java 1.2. It provides basic implementation of the Map
interface of Java. It stores the data in (key, value)  pairs. To access a value one must 
know its key. HashMap is known as HashMap because it uses a technique called hashing. Hashing
is a technique of converting a large String  to small string that represents the same String.
A shorter value helps in indexing and faster searches. HashSet also uses HashMap internally. 
It internally uses a link list to store key-value pairs already explained in HashSet.

Algorithm:

1. Create a Hashmap hm, to store key-value pair, i.e. element-frequency pair.
2. Traverse the array from start to end.
3. For every element in the array update hm[array[i]]++
4. Store the element-frequency pair in a vector and sort the vector in decreasing order of 
frequency
5. Print the first k elements of sorted array.

Complexity Analysis:

Time Complexity: O(d log d), where d is the count of distinct elements in the array. 
To sort the array O(d log d) time is needed.
Auxiliary Space: O(d), where d is the count of distinct elements in the array. 
To store the elements in HashMap O(d) space complexity is needed.

"""

# function to print the k numbers with most occurrences
def pr_N_mostFrequentNumber(arr, n, k):
    um = {}
    for i in range(n):
        if arr[i] in um:
            um[arr[i]] += 1
        else:
            um[arr[i]] = 1
    
    a = [0] * (len(um))
    j = 0

    for i in um:
        a[j] = [i, um[i]]
        j += 1

    a = sorted(a, key=lambda x: x[0], reverse=True)
    a = sorted(a, key=lambda x: x[1], reverse=True)

    # display the top k numbers 
    print(k, "numbers with most occurrences are:")
    for i in range(k):
        print(a[i][0], end=" ")

if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    n = 8
    k = 2
    pr_N_mostFrequentNumber(arr, n, k)

"""
Method 2:

Create a HashMap to store element-frequency pair in the HashMap. HashMap is used to perform
insertion and updation in constant time. Then use a priority queue to store the element-frequency
pair(Max-Heap). This gives the element which has maximum frequency at the root of the Priority
Queue. Remove the top or root of Priority Queue K times and print the element. To insert and
delete the top of the priority queue O(log n) time is required.

Priority Queue: Priority queues are a type of container adapters, specifically, designed such
that the first element of the queue is the greatest of all elements in the queue and elements 
are in non increasing order (hence we can see that each element of the que has a 
priority{fixed order})

Algorithm:
1. Create a Hashmap hm, to store key-value pair, i.e. element-frequency pair.
2. Traverse the array from start to end.
3. For every element in the array update hm[arr[i]]++
4. Store the element-frequency pair in a Priority Queue and create the Priority Queue, this takes 
O(n) time.
5. Run a loop k times, and in each iteration remove the top of the priority queue and 
print the element.

Complexity Analysis: 

Time Complexity: O(k log d + d), where d is the count of distinct elements in the array. 
To remove the top of priority queue O(log d) time is required, so if k elements are removed then O(k log d) time is required and to traverse the distinct elements O(d) time is required.
Auxiliary Space: O(d), where d is the count of distinct elements in the array. 
To store the elements in HashMap O(d) space complexity is needed.

https://www.careercup.com/question?id=5082885552865280

"""

# program to find k numbers with most occurrences in the given array
import heapq

# Function to print the k numbers with most occurrences
def print_N_mostFrequentNumber(arr, n, k):
    mp =dict()

    # put count of all distinct elements in dictionary with element as key & count as the value
    for i in range(0, n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] +=1

    # using heapq data structure
    heap =[(value, key) for key, value in mp.items()]

    # Get the top k elements
    largest = heapq.nlargest(k, heap)

    # Insert the data from the map to the priority queue
    print(k, " numbers with most occurrences are: ", sep=" ")

    # print the top k elements
    for i in range(k):
        print(largest[i][1], end=" ")

if __name__=="__main__":
     
    arr = [ 3, 1, 4, 4, 5, 2, 6, 1 ]
    n = len(arr)
    k = 2
     
    print_N_mostFrequentNumber(arr, n, k)

'''
Tests

'''

def foo(a):
    for b in a:
        yield b
        

def k_occurrences(arr, k):
	dic ={}
	
	for i in (arr):
		if i not in dic:
			dic[i] =0
		dic[i] =dic[i] +  1
	pre_item= result_val ={k: v for k, v in sorted(dic.items(),reverse=True, key=lambda item: item[0])}
	result_val ={k: v for k, v in sorted(pre_item.items(),reverse=True, key=lambda item: item[1])}
	new_list =(list(result_val)[:k])
    #return new_list
	
	
	return [b for b in foo(new_list)]
	
print("expected 4, 1: actual", k_occurrences([3, 1, 4, 4, 5, 2, 6, 1], 2))
print("expected [5 11 7 10]: actual", k_occurrences([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4))
