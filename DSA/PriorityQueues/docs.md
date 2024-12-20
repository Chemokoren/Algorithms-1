# Queues
- Queues collection of objects follows FIFO e.g. Customers waiting for service
- FIFO policy  does no suite many real applications e.g. Air Traffic control
- Though FIFO policy is reasonable, some situations require objects to be prioritized
- This is achieved through Priority Queues
### Priority Queues
- Priority Queues is a Collection of prioritized Objects or Elements 
- Allows element insertion
- Removal of element is based on priority
- A key is associated when element is inserted in the priority queue
- Element with minimum key will be next element to be removed
- 
### Heaps
- heap is an efficient realization of Priority Queue
- Heap is a Binary Tree
- Relational Property:
  - In a heap the value in each node is greater than or equal to  those in its children (Max Heap)
  - In a heap the value in each node is less than or equal to  those in its children (Min Heap)
- Structural Property
  - Heap is a complete binary tree
- Max Heap and Min Heap

# Heap ADT
- Heap ADT stores prioritized objects
- Members:
  - MaxSize
  - CurrentSize
  - HeapList
- Operations
  - insert(Object) : insert element
  - deleteMax(): remove & return element
  - max(): return root element
  - len(): returns number of elements
  - isEmpty(): whether stack is empty or not