"""
Segment Tree
Faster Range Queries

For this article we want to introduce the idea of a Segment Tree. Segment Trees allow us to quickly 
perform range queries as well as range updates. Suppose we had an array and we wanted to know the sum 
of a particular range of numbers as well as update the array when necessary. Normally, if we were to 
just use an array updating would take O(1) time but a sum query could take up to O(n) as it could 
entail looping through the entire array. Segment Trees make both operations a O(log(n)) operation.

Array to Tree

Segment trees work by breaking down the array into a binary tree where each node represents a segment 
of the array. Each node in the binary tree is created by taking the existing segment, cutting it in 
half and distributing it to the children nodes. Here is a graphic to give you an idea of how this 
tree looks like. Note that every node has [i,j] displayed which shows the interval covered by that 
particular node in the tree.


                                    [1:5]
                                   /     \
                              [1:3]       [4:5]
                             /    \       /    \
                       [1:2]       [3:3][4:4]   [5:5]
                      /    \
                  [1:1]     [2:2]      
                                    For an array of size 5

Query and Update

Suppose we want to compute the sum of an array on an interval. After building the tree we can compute 
this query by moving down the tree until the segment represented by our tree is completely within the
bounds of the interval. We then take all our segments and compute the sum of the segments to compute 
the sum of the interval.

Updating our tree works in a similar fashion. Suppose we want to update a particular point in the
array. This would mean we recursively work our way down to the leaf node that contains only that 
node and update it. Then when we resolve the recursive stack we make sure to update all the parent
nodes that contain that segment to the new value.

Now that we visually have a good understanding of what our data structure will look like, let's try 
putting it into some code. An implementation detail that can simplify things is that we can actually 
use a linear array to represent our tree. We can make a new left node by taking our current node and 
doing 2 * n if n is our current node and 2 * n + 1 to represent the right node. For this example we 
will assume we want to calculate the sum of the array on an interval. It can also be noted that both 
1-idexed and 0-indexed arrays can both work for segment trees and it is mostly up to personal 
preference. BUT, the segment tree must be 1-indexed.

For the Interview

Segment tree is only useful for problems involving range queries. The implementation is rather tricky
to get right. However, knowing the existence and concept of this data structure would likely impress
the interviewer. It's good to know but definitely focus on the more core patterns if you are short on
time. Consider this an extra credit.

Implementation

"""

class segment_tree:

    def __init__(self, arr):
        self.tree =[0] * (4 * len(arr))
        for i in range(len(arr)):
            self.update(1, 0, len(arr)-1, i, arr[i])

    def update(self, cur, cur_left, cur_right, idx, val):
        # make sure we reach leaf node when the left interval equals right interval and return the v
        if cur_left == cur_right and cur_left == idx:
            self.tree[cur] = val
        else:
            # compute value of the midpoint where we cut the segment in half
            cur_mid =(cur_left + cur_right) // 2
            # remember n * 2 is left child node and n *2 + 1 is the right child node
            if idx <= cur_mid:
                self.update(cur * 2, cur_left, cur_mid, idx, val)
            else:
                self.update(cur * 2 + 1, cur_mid + 1, cur_right, idx, val)
            # after updating the values, compute the new value for the node
            self.tree[cur] = self.tree[cur*2] + self.tree[cur * 2 + 1]
    def query(self, cur, cur_left, cur_right, query_left, query_right):
        # if our current left interval is greater than the queried right interval it means we are out of range
        # similarly, if the current right interval is less than the queried left interval we are out 
        # of range in both cases return 0

        if cur_left > query_right or cur_right < query_left:
            return 0
        # check if we are in range, if we return the current interval
        elif query_left <= cur_left and cur_right <= query_right:
            return self.tree[cur]
        # this means part of our interval is in range but part of our interval is not in range, we
        # must therefore query both children
        cur_mid =(cur_left + cur_right) // 2
        return self.query(cur * 2, cur_left, cur_mid, query_left, query_right) + self.query(cur * 2 + 1, cur_mid+1, cur_right, query_left, query_right)
        