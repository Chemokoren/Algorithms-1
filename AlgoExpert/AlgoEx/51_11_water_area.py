"""
Water Area
"""

# O(n) time | O(n) space
def waterArea(heights):
    maxes =[0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)

my_array =[0,8,0,0,5,0,0,10,0,0,1,1,0,3]

print(waterArea(my_array))