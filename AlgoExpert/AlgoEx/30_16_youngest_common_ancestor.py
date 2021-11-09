"""
youngest common ancestor - similar to lowest common manager(main diff - data model (interface of the input))
We are told that the 3 inputs are instances of a class that have 1 ancestor property
that points to their direct ancestor
This is a graph problem -trees

"""

# O(d) time | O(1) space where d -deeper of the descendants
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne,descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo,descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant
    