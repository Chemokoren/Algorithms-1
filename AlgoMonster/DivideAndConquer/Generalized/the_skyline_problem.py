"""
Generalized divide and conquer problems
Skyline problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in 
that city when viewed from a distance. Now suppose you are given the locations and heights
of all the buildings as shown on a cityscape photo (Figure A), write a program to output 
the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [
Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the 
ith building, respectively, and Hi is its height. It is guaranteed that 
0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are
perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: 
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ].

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
A key point is the left endpoint of a horizontal line segment. Note that the last key 
point, where the rightmost building ends, is merely used to mark the termination of
the skyline, and always has zero height. Also, the ground in between any two adjacent 
buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Input: [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]] Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

"""