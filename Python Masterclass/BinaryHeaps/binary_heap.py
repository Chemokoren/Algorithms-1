"""
[41, 39, 33, 18, 27, 12]
"""
class BinaryHeap:

    def __init__(self) -> None:
        self.values =[41, 39, 33, 18, 27, 12]

    def insertHeap(self, value):
        self.values.append(value)
        self.bubbleUP()

    def __str__(self) -> str:
        return self.values

    def bubbleUP(self):
        idx = len(self.values) -1
        element =self.values[idx]
        
        
        while idx > 0:
            parentIdx = (idx -1)// 2
            parent =self.values[parentIdx]

            if(element <= parent):
                break
            self.values[parentIdx], self.values[idx] = self.values[idx], self.values[parentIdx]
            idx = parentIdx

    def extractMax(self):
        if len(self.values) > 0:
            max = self.values[0]
            end = self.values.pop()

            if len(self.values)> 0:
                self.values[0] = end
                self.trickleDown()
                # self.sinkDown()
            else:
                print("Done")
            return max
        print("Max operation not possible on an empty array")


    # work in progress
    def sinkDown(self):

        # start sink-down process
        parentIdx = 0

        leftChildIdx  = (parentIdx * 2) + 1
        rightChildIdx = (parentIdx * 2) + 2
        length = len(self.values)

        while rightChildIdx < length: 

            if(self.values[parentIdx] > self.values[leftChildIdx] and self.values[parentIdx] > self.values[rightChildIdx]):
                break
            parent =self.values[parentIdx]
            leftChild =self.values[leftChildIdx]
            rightChild =self.values[rightChildIdx]

            greatest_child = max(leftChild, rightChild)

            childIdx = self.values.index(greatest_child)
            newChild = self.values[childIdx]
        

            if greatest_child > parent:
                parent, newChild = newChild,parent
                parentIdx = childIdx

 

    def trickleDown(self):
        idx = 0
        length = len(self.values)
        parent = self.values[0]

        while(True):
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            swap = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if(leftChild > parent):
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]

                if(
                    (swap == None and rightChild > parent) or
                    (swap != None and rightChild > leftChild)
                ):
                    swap = rightChildIdx
            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = parent
            idx = swap





sol = BinaryHeap()
# print("original list: ",sol.__str__())
# sol.insertHeap(55)
# sol.bubbleUP()
# print("After inserting 55:", sol.__str__())
# sol.insertHeap(1)
# sol.bubbleUP()
# print("after inserting 1: ", sol.__str__())
# sol.insertHeap(199)
# sol.bubbleUP()
# print("after inserting 199: ", sol.__str__())

# print("max value: ", sol.extractMax())
# print(sol.__str__())
# sol.insertHeap(67)
# sol.bubbleUP()
# print("after adding 67: ", sol.__str__())

print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())
sol.extractMax()
print("values: ",sol.__str__())

sol.insertHeap(10)
print("values: ",sol.__str__())
sol.insertHeap(30)
print("values: ",sol.__str__())
sol.insertHeap(99)
print("values: ",sol.__str__())