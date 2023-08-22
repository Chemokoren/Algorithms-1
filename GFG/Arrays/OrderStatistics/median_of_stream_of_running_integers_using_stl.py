"""

Median of Stream of Running Integers using STL

Given that integers are being read from a data stream. Find the median of all the elements read 
so far starting from the first integer till the last integer. This is also called the Median
 of Running Integers. The data stream can be any source of data, for example a file, an array
 of integers, input stream.

What is Median?

Median can be defined as the element in the data set which separates the higher half of the 
data sample from the lower half. In other words, we can get the median element as, 
when the input size is odd, we take the middle element of sorted data. 
If the input size is even, we pick an average of middle two elements in the sorted stream.

Examples:

Input: 5 10 15 
Output: 5, 7.5, 10 

Explanation: Given the input stream as an array of integers [5,10,15]. Read integers one by 
one and print the median correspondingly. So, after reading first element 5,median is 5. 
After reading 10,median is 7.5 After reading 15 ,median is 10.

Input: 1, 2, 3, 4 
Output: 1, 1.5, 2, 2.5 
Explanation: Given the input stream as an array of integers [1, 2, 3, 4]. Read integers one 
by one and print the median correspondingly. So, after reading first element 1,median is 1. 
After reading 2,median is 1.5 After reading 3 ,median is 2.After reading 4 ,median is 2.5. 
 


 Algorithm: 
 

Create two heaps. One max heap to maintain elements of lower half and one min heap to
maintain elements of higher half at any point of time..

Take initial value of median as 0.

For every newly read element, insert it into either max heap or min-heap and calculate 
the median based on the following conditions: 

If the size of max heap is greater than the size of min-heap and the element is less than
the previous median then pop the top element from max heap and insert into min-heap
and insert the new element to max heap else insert the new element to min-heap.

Calculate the new median as the average of top of elements of both max and min heap.

If the size of max heap is less than the size of min-heap and the element is greater than 
the previous median then pop the top element from min-heap and insert into the max heap 
and insert the new element to min heap else insert the new element to the max heap.
Calculate the new median as the average of top of elements of both max and min heap.

If the size of both heaps is the same. Then check if the current is less than the previous
median or not. If the current element is less than the previous median then insert it to 
the max heap and a new median will be equal to the top element of max heap. 
If the current element is greater than the previous median then insert it to min-heap and 
new median will be equal to the top element of min heap.

Complexity Analysis: 
 

Time Complexity: O(n Log n). 
Time Complexity to insert element in min heap is log n. So to insert n element is O( n log n).

Auxiliary Space : O(n). 
The Space required to store the elements in Heap is O(n).

"""


# program to find median in stream of running integers

# method to calculate med of stream
def  printMedian(a):
    
    med = a[0]

    # max heap to store the smaller half elements
    smaller = []
    
    # min-heap to store the greater half elements
    greater = []

    final =[]
    
    smaller.append(a[0])
    final.append(med)
    
    # reading elements of stream one by one

    '''
    At any time we try to make heaps balanced and
	their sizes differ by at-most 1. If heaps are
	balanced,then we declare median as average of
	min_heap_right.top() and max_heap_left.top()
	If heaps are unbalanced,then median is defined
	as the top element of heap of larger size 

    '''
    
    for i  in range(1, len(a)):
        
        x = a[i]

        # case1(left side heap has more elements)
        
        if(len(smaller) > len(greater)):
            if(x < med):
                smaller.sort(reverse=True)
                greater.append(smaller.pop(0))
                smaller.append(x)
            
            else:
                greater.append(x)
                smaller.sort(reverse=True)
                greater.sort()
                med = (smaller[0] + greater[0])/2
        
        # case2(both heaps are balanced)
        elif(len(smaller) == len(greater)):
            if(x < med):
                smaller.append(x)
                smaller.sort(reverse=True)
                med = smaller[0]
            else:
                greater.append(x)
                greater.sort()
                med = greater[0] 
        
        # case3(right side heap has more elements)
        
        else:
            if(x > med):
                
                greater.sort()
                smaller.append(greater.pop(0))
                greater.append(x)
			
            else:
                
                smaller.append(x)
                smaller.sort(reverse=True)
                med = (smaller[0] + greater[0])/2

        final.append(med)
    
    return final
			

arr=[5, 15, 10, 20, 3]
print("expected:[5, 10, 10, 12.5,10], actual:",printMedian(arr))
print("expected:[5, 7.5, 10 ], actual:",printMedian([5,10,15]))
print("expected:[1, 1.5, 2, 2.5 ], actual:",printMedian([1, 2, 3, 4 ]))

