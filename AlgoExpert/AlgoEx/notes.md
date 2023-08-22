# topics to review (ensure they are running)

- https://www.youtube.com/watch?v=Nabbpl7y4Lo
- https://laravel.com/docs/8.x/eloquent-relationships
- https://algo.monster/problems/stats
- https://www.youtube.com/watch?v=G_UYXzGuqvM
- https://www.youtube.com/watch?v=A80YzvNwqXA
- https://www.youtube.com/watch?v=rf6uf3jNjbo&list=PLpXOY-RxVRTM_-Lvss2ezy1lVl6VUrzW2&index=13
- https://www.youtube.com/watch?v=ngCos392W4w
- https://www.youtube.com/watch?v=9i6ZiwrLscY


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    temp = []
    if checkerString(A) != False:
        for x in range(0, len(A),1):
            toUse = AddString(str(A[x]))
            for y in range(1,len(A),1):
                toUse2 = AddString(A[y])
            if toUse == toUse2 :
                temp.append(A[x] + A[y])
                break
    if len(temp) != 0:
        return max(temp)
    return -1
    

def AddString(digit):
    digit = str(digit)
    temp = 0
    res = [temp + int(x) for x in digit]
    return sum(res)

def checkerString(input):
    res = [AddString(str(input[0]))]
    for x in range(1,len(input)):
       t =  AddString(str(input[x]))
       if t not in res:
           pass
       elif t in res:
           res.append(t)
    if len(res) == 1:
        return False
    else:
        return True
    


