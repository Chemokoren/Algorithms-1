"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in 
constant time.

Implement the MinStack class:
- MinStack() initializes the stack object
- void push(val) pushes the element val onto the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""

class MinStack:
    def __init__(self) -> None:
        self.st =[]
        self.minimum = float('inf')

    def push(self, x:int)->None:
        if(len(self.st)==0):
            self.minimum = x
        else:
            self.minimum = min(self.minimum, x)

        self.st.append(x)

    def pop(self)->None:
        if(len(self.st) > 0):
            top = self.st[-1]
            self.st.pop()
            if(top == self.minimum):
                self.minimum=min(self.st) if self.st else None

    def top(self)->int:
        if(len(self.st) == 0):
            return None
        return self.st[-1]

    def getMin(self)->int:
        return self.minimum


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.st)
print("min val:", minStack.getMin()) # return -3
minStack.pop()
print("after pop: ", minStack.st)
print("top element: ", minStack.top())    # return 0
print("min val 2: ", minStack.getMin()) # return -2