# O(n) time | O(d) space
def validateBST(tree):
    return validateBSTHelper(tree,float("-inf"),float("inf"))

def validateBSTHelper(tree,minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >=maxValue:
        return False