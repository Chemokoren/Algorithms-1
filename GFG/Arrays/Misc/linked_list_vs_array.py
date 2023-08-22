"""
Arrays store elements in contiguous memory locaitons, resulting in easily calculable addresses for
the elements stored and this allows faster access to an element at a specific index.

Linked lists are less rigid in their storagne structure and elements are usually not stored in 
contiguous locations, hence they need to be stored with additional tags giving a reference to the
next element.
This difference in the data storage scheme decides which data structure would be more suitable for 
a given situation.

Major differences between array and linked-list are listed below:

Size: Since data can only be stored in contiguous blocks of memory in an array, its size cannot
be altered at runtime due to the rist of overwriting other data.
However, in a linked list, each node points to the next one such that data can exist at scattered
(non-contiguous) addresses. This allows for a dynamic size that can change at runtime.
Memory allocation: For arrays at compile time and at runtime for linked lists. But, a dynamically 
allocated array also allocates memory at runtime. 
Memory efficiency: For the same number of elements, linked lists use more memory as a reference
to the next node is also stored along with the data. However, size flexibility in linked lists
may make them use less memory overall; this is useful when there is uncertainty about size or 
there are large variations in the size of data elements.
Memory equivalent to the upper limit on the size has to be allocated(even if not all of it is being
used) while using arrays, whereas linked lists can increase their sizes step-by-step 
proportionately to the amount of data.
Execution time: Any element in an array can be directly accessed with its index. However, in the
case of a linked list, all the previous elements must be traversed to reach any element.
Also, better cache locality in arrays(due to contiguous memory allocation) can significantly 
improve performance. As a result, some operations(such as modifying a certain element) are faster
in arrays, while others(such as inserting/deleting an element in the data) are faster in linked
lists.

Insertion: in an array, insertion operation takes more time but in a linked list these 
operations are fast. For example, if we want to insert an element in the array at the end position
in the array and the array is full then we copy the array into another array and then we can add
an element whereas if the linked list is full then we find the last node and make it next to the
new node.

Dependency: In an array, values are independent of each other but in the case of linked list nodes
are dependent on each other. One node is dependent on its previous node. If the previous node is
lost then we can't find its next subsequent nodes.

Array                                   Linked Lists
- stored in contiguous location         - Not stored in contiguous location
- Fixed in size                         - Dynamic in size
- Memory is allocated at compile time   - Memory is allocated at runtime
- Uses less memory than LL              - Uses more memory(data + address of next node)
- Easy element access                   - Element access requires traversal of whole LL
- Insertion & Deletion operation takes time - Insertion and deletion operation is faster

Advantages of Linked Lists
- The size of the arrays is fixed: so we must know the upper limit on the number of elements in
advance. Also, generally, the allocated memory is equal to the upper limit irrespective of usage, 
and in practical uses, the upper limit is rarely reached.
- Inserting a new element in an array of elements is expensive because a room has to be created
for the new elements and to create a room existing elements have to be shifted.

Example
suppose we maintain a sorted list of IDs in an array id[ ] = [1000, 1010, 1050, 2000, 2040, …..]. 
And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all 
the elements after 1000 (excluding 1000). 
Deletion is also expensive with arrays unless some special techniques are used. For example, to
delete 1010 in id[], everything after 1010 has to be moved.

So Linked list provides the following two advantages over arrays:

    Dynamic size 
    Ease of insertion/deletion 

Disadvantages of Linked Lists

- Random access is not allowed. We have to access elements sequentially starting from the first
node. So we cannot do a binary search with linked lists.
- Extra memory space for a pointer is required for each element of the list.
- Arrays have a better cache locality that can make a pretty big difference in performance.
- It takes alot of time in traversing and changing the pointers.
- It will be confusing when we work with pointers.

Advantages of Arrays:

    Arrays store multiple data of similar types with the same name.
    It allows random access to elements.
    As the array is of fixed size and stored in contiguous memory locations there is no memory 
    shortage or overflow.
    It is helpful to store any type of data with a fixed size.
    Since the elements in the array are stored at contiguous memory locations it is easy to 
    iterate in this data structure and unit time is required to access an element if the index is 
    known.

Disadvantages of Arrays:

    The array is static in nature. Once the size of the array is declared then we can’t modify it.
    Insertion and deletion operations are difficult in an array as elements are stored in 
    contiguous memory locations and the shifting operations are costly.
    The number of elements that have to be stored in an array should be known in advance.
    Wastage of memory is the main problem in the array. If the array size is big the less 
    allocation of memory leads to wastage of memory.


"""