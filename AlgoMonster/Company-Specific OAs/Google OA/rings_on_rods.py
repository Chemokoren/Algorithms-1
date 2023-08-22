"""
2021 (OA) - Rings on Rods

You have 10 rods numbered from 0 to 9. There are three types of rings, red, green and blue, being put 
on the rods. You get a point for each rod that has a ring of each color on it, i.e. to get a point 
you need a red ring, green ring and blue ring on one rod.

A ring put on a rod is represented by two characters, the first describes the color of the ring and 
the second describes which number rod it is on from 0 to 9. For example "R8" means that a red ring is
being put on the 8th rod.

Input

    s: a corrent string of length 2N describing the N rings put on rods

Output

how many points you will get
Examples
Example 1:

Input:

s = B2R5G2R2

Output: 1

Explanation:

One point for rings put on the second rod.

"""
def solution(s: str) -> int:
    return 0

if __name__ == '__main__':
    s = input()
    res = solution(s)
    print(res)