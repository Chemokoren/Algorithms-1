def ClimbingStairsBottomUp(n):
    s = [-1]*(n + 1)
    s[1] = 1
    s[2] = 2

    for i in range(3,n):
        s[i] = s[i-1] + s[i-2]
        
    return s[n]

print(ClimbingStairsBottomUp(3))