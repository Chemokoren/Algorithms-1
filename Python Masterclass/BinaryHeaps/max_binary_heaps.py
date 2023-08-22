"""
- Define what a binary heap is
- Compare and contrast min and max heaps
- implement basic methods on heaps
- understand where heaps are used in the real world and what other data structures
can be constructed from heaps

What is a binary heap?

Very similar to a binary search tree, but with some different rules

MaxBinaryHeap = parent nodes are always larger than child nodes
MinBinaryHeap = parent nodes are always smaller than child nodes
-There is no order in left-right child

Max Binary Heap
-Each parent has at most two child nodes
-The value of each parent node is always greater than its child nodes
-In a max Binary Heap the parent is greater than the children, but there are no 
guarantees between sibling nodes
-A binary heap is as compact as possible. All the children of each node are as full 
as they can be and left children are filled out first.(Takes up the least amount of
space possible - so every left & right is filled before we move down)

Why do we need to know this?
- Binary heaps are used to implement Priority Queues, which are very common data 
structures
- They are also used with graph traversal algorithms

There's an easy way of storing a binary heap:
- using a list/array

Representing a Heap
-For any index of an array n...
* The left child is stored at 2n + 1
* The right child is stored at 2n + 2

What if we have a child node and want to find its parent?
- For any child node at index n...
* Its parent is at index(n-1)//2

Adding to a MaxBinaryHeap
- Add to the end (of array)
- Bibble up(swap it till it finds it's correct resting place)

Insert Pseudocode
- Push the value into the values property on the heap
- Bubble the value up to its correct spot!

Insert Pseudocode(Detailed)
- push the value into the values property on the heap
- Bubble Up:
    - Create a variable called index which is the length of the values property -1
    - create a variable called parentIndex which is the floor of(index-1)/2
    - keep looping as long as the values element at the parentInde is less than the 
    values element at the child index

Removing From a Heap
- Remove the root
- Replace with the most recently added
- Adjust (bubble-down)

The process of deleting the root from the heap(effectively extracting the maximum 
element in a max-heap or the minimum element in a min-heap) and restoring the properties
is called down-heap or:
- bubble-down
- percolate-down
- sift-down
- trickle down
- heapify-down
- cascade-down
- extract-min/max

REMOVING (extractMax)

- swap the first value in the values property with the last one
- pop from the values property, so you can return the value at the end.
- Have the new root "Bubble down" to the correct spot ...
    - Your parent index starts at 0 (the root)
    - Find the index of the left child: 2 * index + 1(make sure its not out of bounds)
    - Find the index of the right child: 2 * index + 2(make sure its not out of bounds)
    - if the left or right child is greater than the element ...swap. If both left and
    right children are larger, swap with the largest child.
    -The child index you swapped to now becomes the new parent index.
    -Keep looping and swapping until neither child is larger than the element.
    -Return the old root!
"""



class maxBinaryHeap:

    def __init__(self) -> None:
        self.values = []

    def __str__(self) -> str:
        return self.values

    def insert(self, val):
        self.values.append(val)
        self.bubbleUP()

    def bubbleUP(self):
        index = len(self.values)-1
        parentIndex  = (index-1) // 2

        while self.values[parentIndex] < self.values[index]:
            self.values[parentIndex],self.values[index] =self.values[index],self.values[parentIndex]
            index =parentIndex

    def extractMax(self):
        if len(self.values) > 1:
            parent = self.values[0]
            end = self.values.pop()
            self.values[0] = end
            self.bubbleDown()
            return parent
        return self.values.pop()

    def bubbleDown(self):
        parentIdx = 0
        leftChildIdx = (parentIdx * 2) + 1
        rightChildIdx = (parentIdx * 2) + 2

        length = len(self.values)

        while rightChildIdx < length:

            leftChild  = self.values[leftChildIdx]
            rightChild = self.values[rightChildIdx]
            element =self.values[parentIdx]

            greaterChild =max(leftChild, rightChild)
            greaterChildIdx =self.values.index(greaterChild)

            if greaterChild > element:
                self.values[greaterChildIdx],element= element,self.values[greaterChildIdx]
                parentIdx = greaterChildIdx
        





sol = maxBinaryHeap()
sol.insert(40)
sol.insert(20)
sol.insert(80)
print(sol.__str__())
print("max : ",sol.extractMax())
print(sol.__str__())
print("max : ",sol.extractMax())
print(sol.__str__())
print("max : ",sol.extractMax())
print(sol.__str__())