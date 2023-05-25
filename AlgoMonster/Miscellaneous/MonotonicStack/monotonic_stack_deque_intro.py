"""
Monotonic Stack / Deque Intro


The word "monotonic" means a list or a function is either always increasing, or always decreasing. 
In that case, a "monotonic stack" or a "monotonic deque" is a stack or a deque that has this 
property.

Monotonic stack is like a regular stack with one key distinction in the push operation: Before we 
push a new element onto the stack, we first check if adding it breaks the monotonic condition.
If it does, then we pop the top element off the stack until pushing the new element no longer breaks
the monotonic condition.

Below is a graphical explanation of the idea. It is a monotonic stack that is decreasing, but the 
same idea can apply to deque and other monotonic properties as well.

Example implementation

Below is an example implementation of a monotonic stack.

"""
def mono_stack(insert_entries):
    stack =[]
    for entry in insert_entries:
        # The monotonic property can only break if and only if the container 
        # is not empty and the last item, compared to the entry, breaks
        # the property. While that is true, we pop the top item.
        while stack and stack[-1] <= entry:
            stack.pop()
            # Do something with the popped item here
        stack.append(entry)
"""
Applications of Monotonic Stack/Deque

There are a few interesting properties of a monotonic stack/deque that we can utilize in certain 
types of questions.

By definition, the monotonic property of this data structure is always maintained, so you know the 
entries in the stack/deque is sorted. Furthermore, we know that items that get popped during the 
insertion always sorted because the insertion breaks the monotonic property, so if a particular item
didn't get popped this way, it is because the monotonic property was maintained for that item.

For example, in the example above, consider the number 3 at index 0. When it gets popped, 6 was 
inserted and it breaks the monotonic property, but every insertion before did not break the property
for 3. Therefore, we know that the next larger or equal number for 3 is 6.


Next Largest or Smallest Element in a List

As shown above, this method is effective when you need to determine the next larger or smaller member
for each element in a list, as it can naturally be determined when you insert element into the stack
in order. The overall complexity of this algorithm is O(n), because each item in the list is 
inserted and popped at most once.

If there are other restrictions, such as the next larger/smaller member must be within a certain 
distance, then we can use a deque instead, and pop from the end of the deque when the range is 
exceeded.

For an example, see Daily Temperatures.

Maximum or Minimum Element in a Sliding Window

Furthermore, because the stack/deque is monotonic, you can easily access the maximum/minimum element
by looking at the start of the stack/queue. This means that for a sliding window, we can easily keep
track of its maximum/minimum element. When we insert an item from one side, we perform the monotonic
insertion method on the deque, and when we remove an item from the other side, we simply pop the 
item on the other side if the index matches.

For an example, see Sliding Window Maximum.

"""