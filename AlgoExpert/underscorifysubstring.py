# O(n + m) time | O(n) space

def underscorifysubstring(string, substring):
    locations =collapse(getLocations(string,substring))
    return underscorify(string, locations)

def getLocations(string, substring):
    locations =[]
    startIdx =0
    while startIdx < len(string):
        nextIdx =string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx =nextIdx + 1
        else:
            break
    return locations
def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous =newLocations[0]
    for i in range(1, len(locations)):
        current =locations[i]
        if current[0] <= previous[1]:
            previous[1] =current[1]
        else:
            newLocations.append(current)
            previous = current
    return newLocations

def underscorify(string, locations):
    locationsIdx =0
    stringIdx =0
    inBetweenUnderscores =False
    finalChars =[]
    i =0
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]: # [[0,4],[8,12],[19,23]]
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1
            i =0 if i == 1 else 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)

