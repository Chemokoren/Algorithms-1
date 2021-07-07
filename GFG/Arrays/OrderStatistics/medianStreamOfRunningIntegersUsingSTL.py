"""

Median of Stream of Running Integers using STL

Given that integers are being read from a data stream. Find the median of all the elements read 
so far starting from the first integer till the last integer. This is also called the Median
 of Running Integers. The data stream can be any source of data, for example a file, an array
 of integers, input stream.


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

"""