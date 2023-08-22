"""
Minimum Spanning Tree | Forests

The Umbristan Department of Forestry(UDF) is tackling a rather difficult problem and the 
Umbristan government has detached you one of its best workers to go resolve the issue. When you 
arrive you are quickly briefed on the problem at hand. Inside the Umbristan National Park there
exists an area that has been closed off as fencing needs to be erected in the area. 
The department for whatever reason needs to set up some very expensive fencing between the trees.
The department has also set up some rules for the fence

    - The fence needs to be set up such that every tree in the area is connected to the fence.

    - The department is on a very strict operating budget and so needs to minimize the metres of
    fencing required.

    - The department has counted the number of trees in the area as well as determined all 
    possible tree pairs where a fence can be built between the pair.

4.Can you help them figure out the smallest amount of fencing required?

It is possible that not all the nodes will be connected to one another depending on the tree
pairs. Input will consist of trees the number of trees in the area labelled from 1 to n as well 
as pairs, a list consisting of the tuple [a, b, d] which denotes that a fence can be built 
between the trees a and b that will be d metres in length.
Constraints

1 <= trees <= 10^5
Examples
Example 1:
Input: trees = 5, pairs = [[1, 2, 1], [2, 4, 2], [3, 5, 3], [4, 4, 4]]
Output: 6
Explanation:

We can erect fencing between trees for the following pairs, 1 and 2, 2 and 4, 3 and 5. With this
 every tree is connected by a fence and we have used 6 metres of fencing.
 
"""