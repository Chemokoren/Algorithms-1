'''

sort a linked list using quick sort

The important things about implementation are, that it changes pointers rather than 
swapping data.

Follow the given steps to solve the problem:

- Call partition function to get a pivot node placed at its correct position
    - In the partition function, the last element is considered a pivot
    - Then traverse the current list and if a node has a value greater than the pivot,then
        move it after the tail. If the node has a smaller value, then keep it at its
        current position.
    - return pivot node

- Find the tail node of the list which is on the left side of the pivot and recur for 
    the left list
- Similarly, after the left side, recur for the list on the right side of the pivot
- Now return the head of the linked list after joining the left and right list, as the 
whole linked list is now sorted


Time Complexity: O(N * log N), It takes O(N2) time in the worst case and O(N log N) in 
the average or best case.
Auxiliary Space: O(N), As extra space is used in the recursion call stack.

'''
from generic_singly_linked_list import generic_singly_linked_list


class QuickSortLinkedList(generic_singly_linked_list):
    def __init__(self) -> None:
        super().__init__()


    ''' takes first and last node,but do not break any links in	the whole linked list'''
    def paritionLast(self,start, end):
        if (start == end or start == None or end == None):
            return start

        pivot_prev = start
        curr = start
        pivot = end.data

        '''
        iterate till one before the end, no need to iterate till the end because end is
        pivot
        '''

        while (start != end):
            if (start.data < pivot):
                # keep tracks of last modified item
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next

        '''swap the position of curr i.e. next suitable index and pivot'''

        temp = curr.data
        curr.data = pivot
        end.data = temp

        ''' return one previous to current because current is now pointing to pivot '''
        return pivot_prev

    def sort(self, start, end):
        if(start == None or start == end or start == end.next):
            return

        # split list and partion recurse
        pivot_prev = self.paritionLast(start, end)
        self.sort(start, pivot_prev)

        '''
        if pivot is picked and moved to the start,that means start and pivot is same 
        so pick from next of pivot
        '''
        if(pivot_prev != None and pivot_prev == start):
            self.sort(pivot_prev.next, end)

        #if pivot is in between of the list,start from next of pivot,
        #since we have pivot_prev, so we move two nodes
        elif (pivot_prev != None and pivot_prev.next != None):
            self.sort(pivot_prev.next.next, end)

if __name__ == "__main__":
    ll = QuickSortLinkedList()
    ll.insert_end(30)
    ll.insert_end(3)
    ll.insert_end(4)
    ll.insert_end(20)
    ll.insert_end(5)

    # n is the value of the pivot, which is the last value
    n = ll.head
    while (n.next != None):
        n = n.next

    print("\nLinked List before sorting")
    ll.print_given_LL_head(ll.head)

    ll.sort(ll.head, n)

    print("\nLinked List after sorting");
    ll.print_given_LL_head(ll.head)

