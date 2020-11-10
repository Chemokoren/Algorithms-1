# 1. Every points location can be defined by an array of quadrants and their orientation (it will have
# N elements) - each element representing the quadrant in the previous quadrant. The whole maze having
# upwards orientations
# 2. You need to define this array for both points. For example: if N = 2 and the point is in the lower left
# quadrant then it will have the orientation to the left. We take this quadrant and we rotate our coordinate
# system so it will the same orientation. This way we define the next quadrant and orientation pair in our
# new system. So if we have our point in the lower left quadrant then it will have orientation to the left,
# but as this was relative to our previous orientation (which was also to the left) this will become an
# upwards orientation.
# 3. At this point we have all the quadrants and orientation down to the smallest maze that contains our point.
# From backwards (from the smallest maze) we need to solve them. Every maze can be solved by the
# following rules:
#
# - if our point in our current quadrant is on any of the extremes (meaning that any of the coordinate's
# components are either the lowest or highest of the quadrant) we leave it where it was, otherwise check
# next points.
# - if our point is downwards or at the middle of the current quadrant then we move to the quadrants lowest
# middle point (these goes relative the previously defined orientation, i.e.: if our orientation is upwards
# then we will move our point at the topmost middle point)
# - if our point is upwards (in the relative direction) we will have to move it to the topmost middle point

#4. Storing these moves, we check if we have any common elements in the two array belonging to the two points:
#
# - if not we calculate the distance between the two endpoints and the we add up all the distances from the
# two moves list (in this list every distance can be calculated as coordinate component subtractions,
# i.e.: abs(x1-x2) + abs(y1-y2))
# - if we have common elements then we delete every move after that including the common elements and we
# calculate the distance as mentioned at the point before
#
# Edit: Here is my implementation of the above presented solution in Swift3: https://codility.com/demo/results/training9WWFXU-EWC/
#
