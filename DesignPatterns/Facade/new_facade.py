# Python arrays are dynamic by default, but this is an example of resizing
class Array:
    
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr =[0] * 2 # Array of capacity =2
        
    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.arr[self.length] = n
        self.length +=1
        
    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr =[0] * self.capacity