import heapq
"""
Find Median from Data Stream - Heap & Priority Queue

Median is the middle value in an ordered integer list. If the size of the list is even,
 there is no middle value. So the median is the mean of the two middle values.

 For example,
 [2,3,4], the median is 3

 [2,3], the median is (2+3)/2 =2.5

 Design a data structure that supports the following two operations:
    - void addNum(int num) -Add a integer number from the data stream to the data structure
    - double findMedian() - Return the median of all elements so far.

Example:
addNum(1)
addNum(2)
findMedian()-> 1.5
addNum(3)
findMedian() -> 2

"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, (minheap, maxheap)
        # heaps should be equal size
        self.small, self.large =[],[]

    def addNum(self, num:int)->None:
        heapq.heappush(self.small,-1 *num)

        # make sure every num small is <= every num in large
        if(self.small and self.large and ((-1 *self.small[0])> self.large[0])):
            val =(-1 * heapq.heapop(self.small))
            heapq.heappush(self.large, val)


            # uneven size?
            if len(self.small) > len(self.large) + 1:
                val = -1* heapq.heapop(self.small)
                heapq.heappush(self.large, val)

            if len(self.large) > len(self.small) + 1:
                val = heapq.heapop(self.large)
                heapq.heappush(self.small, -1 * val)

    def findMedian(self)-> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large)> len(self.small):
            return self.large[0]
        return ((-1*self.small[0])+self.large[0])/ 2

    def printVals(self):
        print(self.small, self.large)

# nums = [2,3,4]

md = MedianFinder()
md.addNum(1)
md.addNum(2)
# print(md.findMedian())
md.addNum(3)
# print(md.findMedian())
md.printVals()