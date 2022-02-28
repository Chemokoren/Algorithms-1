"""
Median of Data Stream

Given a stream of numbers, find the median number at any given time (accurate to 1 
decimal place). Do this in O(1) time complexity.

Example:

add_number(1)

add_number(2)

add_number(3)

get_median() == 2.0

add_number(4)

get_median() == 2.5

"""

class MedianOfStream: 
    
    def init(self): 
        self.larger_half=[] #min_heap 
        self.smaller_half=[]#max_heap 
        
    def add_number(self, num: float) -> None: 
        # WRITE YOUR BRILLIANT CODE HERE 
        heappush(self.larger_half, num) if len(self.larger_half) > len(self.smaller_half): heappush(self.smaller_half, -1*heappop(self.larger_half))

    def get_median(self) -> float:
        # ALSO HERE
        if len(self.larger_half) == len(self.smaller_half):
            return (self.larger_half[0]-self.smaller_half[0])/2
        else:
            return -1*self.smaller_half[0]

    