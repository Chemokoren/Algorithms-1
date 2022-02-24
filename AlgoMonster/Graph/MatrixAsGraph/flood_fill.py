"""
Flood Fill

In computer graphics, an uncompressed raster image is presented as a matrix of numbers. Each 
entry of the matrix represents the color of a pixel. A flood fill algorithm takes a coordinate
r,c, a replacement color and replaces all pixels connected to r, c that has the same color
as r,c with replacement color(e.g. MS-Paint's paint bucket tool).

Input

r: row
c: column
replacement: replacemnt color
image: a 2D array of integers representing the image

Output

the replaced image

Example 1:

Input:
r =2
c =2
replacement = 9
arr =[[0,1,3,4,1],[3,8,8,3,8],[6,7,8,8,3],[12,3,1,3,2]]

Output: [[0,1,3,4,1],[3,9,9,3,3],[6,7,9,9,3],[12,9,2,9,9,1],[12,3,1,3,2]]

Explanation:

FROM                                        TO
0   1   3   4   1                   0   1   3   4   1
3   8   8   3   8                   3   9   9   3   3
6   7   8   8   3                   6   7   9   9   3
12  2   8   9   1                   1   2   9   9   1
12  3   1   3   2                   12  3   1   3   2


"""

from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))

        