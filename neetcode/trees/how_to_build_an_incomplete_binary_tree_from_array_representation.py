"""
if the input is an array, where null means no node.

input:
[1,2,3,null,5,null,7]

Please assume that I have already checked the input.

For each array[i], its parents array[i/2] not be null(recursively,
so root cannot be null).

How to build a tree with such logic relation

Example 1: [1,2,3,null,5,null,7]

                1
               / \
              2   3
              \     \
               5     7

Example 2: [5,4,8,11,null,17,4,7,null,null,null,5]

                        5
                       / \
                      4   8
                     /   / \  
                    11  17  4
                   /        /
                  7        5

each node should be represented by a TreeNode object.
"""

class TreeNode():
    def __init__(self,val) -> None:
        self.val =val
        self.left  = None
        self.right = None

def createTree(array):
    if (array == None or len(array)==0):
        return None

    treeNodeQueue = []
    integerQueue  = []

    for i in range(1,len(array)):
        integerQueue.append(array[i])
    

    treeNode = TreeNode(array[0])
    treeNodeQueue.append(treeNode)

    while (len(integerQueue)> 0):

        leftVal  = None if len(integerQueue)== 0 else integerQueue.pop(0)
        rightVal = None if len(integerQueue)== 0 else integerQueue.pop(0)

        current = treeNodeQueue.pop(0)

        if (leftVal !=None):
                left = TreeNode(leftVal)
                current.left = left
                treeNodeQueue.append(left)
        
        if (rightVal !=None):
                right = TreeNode(rightVal)
                current.right = right
                treeNodeQueue.append(right)
        
    
    return treeNode

# inorder traversal
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val,end='--')
        inorderTraversal(root.right)

# preorder traversal
def preorderTraversal(root):
    if root:
        print(root.val, end='--')
        preorderTraversal(root.left)
        preorderTraversal(root.right)

# postorder traversal
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val, end='--')


'''
implementation 2

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right

def createBTree(data):
    if data == None or len(data) == 0:
        return None
    treeNodeQueue = []
    integerQueue  = []

    for i in range(1, len(data)):
        print(i)
        integerQueue.append(data[i])

    treeNode = TreeNode(data[0])
    treeNodeQueue.append(treeNode)

    while integerQueue:
        if integerQueue:
            leftVal = integerQueue.pop(0)
        if integerQueue:
            rightVal =integerQueue.pop(0)

        current = treeNodeQueue.pop(0)

        if leftVal is not None:
            left = TreeNode(leftVal)
            current.left = left
            treeNodeQueue.append(left)
        if rightVal is not None:
            right =TreeNode(rightVal)
            current.right = right
            treeNodeQueue.append(right)

    return treeNode


test_data =[5,4,8,11,None,17,4,7,None,None,None,5]

test_data=[-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,
3,53,-81,33,4,None,-51,-44,-60,11,None,None,None,None,78,None,-35,-64,26,-81,
-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,-49,-11,-51,67,None,None,None,
None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,-4,None,
None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,
37,None,None,73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,
-65,-88,-53,None,None,None,-33,86,None,81,-42,None,None,98,-40,70,-26,24,None,None,
None,None,92,72,-27,None,None,None,None,None,None,-67,None,None,None,None,None,None,
None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,None,None,None,None,
None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,None,
None,-93,None,None,None,98]

print("inorder traversal: ",inorderTraversal(createTree(test_data)))
print("preorder traversal: ",preorderTraversal(createTree(test_data)))
print("postorder traversal: ",postorderTraversal(createTree(test_data)))