# O(b^2 * r) time | O(b) space
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks =[float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween[i, j])
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
        return getIdxAtMinValue(maxDistancesAtBlocks)

def getIdxAtMinValue(array):
    idxAtMinValue =0 
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


"""
Approach 2

"""
# O(b * r) time | O(br) space
def apartmentHuntingTwo(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req:getMinDistances(blocks, req), reqs)) # O(br)
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks) # O(br)
    return getIdxAtMinValue(maxDistancesAtBlocks) # O(b) ---> O(b * (r + 1))

def getMinDistances(blocks, req):
    minDistances =[0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
            minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(len(blocks)))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks =[0 for blocks in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] =max(minDistancesAtBlock)
    return maxDistancesAtBlocks

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a,b):
    return abs(a - b)

my_reqs =["G","Sc","St"]
my_blocks={1:"Sc",2: "G",3:["G","Sc"],4:["Sc","St"]}

print(apartmentHuntingTwo(my_blocks, my_reqs))