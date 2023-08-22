"""
This is the simple Node class from which the tree and list
are built. This does not have any methods -- its just used
as dumb storage by TreeList.
The code below tries to be clear where it treats a Node pointer
as a tree vs. where it is treated as a list.
"""
class Node:
    def __init__(self, data):
        self.data =data
        self.small =None
        self.large =None

"""
TreeList main methods:
-join() -- utility to connect two list nodes
-append() -- utility to append two lists
-treeToList() --the core recurive function
-treeInsert() -- used to build the tree
"""
class TreeList:
    def __init__(self):
        self.head = None

    """
    helper function  --given two list nodes, join them
    together so the second immediately follow the first.
    sets the .next of the first and the .previous of the second.
    """
    def joinNodes(self,node_a, node_b):
        node_a.large = node_b
        node_b.small =node_a


    """
    helper function --given two circular doubly linked
    lists, append them and return the new list.

    """
    def append(self,node_a, node_b):
        # if either is null, return the other
        if (node_a==None):
            return (node_b)
        if (node_b==None):
            return (node_a)

        # find the last node in each using the .previous pointer
        aLast = node_a.small
        bLast = node_b.small

        # join the two together to make it connected and circular
        self.joinNodes(aLast, node_b)
        self.joinNodes(bLast, node_a);

        return (node_a);


    """
    -- Recursion --
    Given an ordered binary tree, recursively change it into
    a cirular doubly linked list which is returned.
    """
    def treeToList(self,node_root):
        # base case: empty tree -> empty list
        if (node_root == None):
            return None

        # Recursively do the subtrees
        aList = self.treeToList(node_root.small)
        bList = self.treeToList(node_root.large)

        # Make the single root node into a list length-1
        # in preparation for the appending
        node_root.small =node_root
        node_root.large =node_root

        # At this point we have three lists, and it's
        # just a matter of appending them together
        # in the right order (aList, root, bList)
        aList = self.append(aList, node_root)
        aList = self.append(aList, bList)

        return (aList)


    """
    Given a non-empty tree, insert a new node in the proper place.
    The tree must be non-rmpty because Java's lack
    of reference variables makes that case and this
    method messier than they should be.
    """
    def treeInsert(self,root, newData):
        if(newData <= root.data):
            if (root.small != None):
                self.treeInsert(root.small, newData)
            else:
                root.small =Node(newData)
        else:
            if(root.large !=None):
                self.treeInsert(root.large, newData)
            else:
                root.large =Node(newData)

    # Do an inOrder traversal to print a tree
    # Does not print the ending "\n"
    def printTree(self,node_root):
        if(node_root==None):
            return
        self.printTree(node_root.small)
        print("" +str(node_root.data))
        self.printTree(node_root.large)
    

   # Do a traversal of the list and print it out
    def printList(self,node_head):
        current =node_head
        while(current != None):
            print(str(current.data)+ " ")
            current = current.large
            if(current == node_head):
               break
            print()

# Demonstrate tree->list with list 1 .. 5

# first build the tree shown in the problem document
root = Node(25)
#        Node root = new Node(4);
#        treeInsert(root, 2);
#        treeInsert(root, 1);
#        treeInsert(root, 3);
#        treeInsert(root, 5);

treeList =TreeList()
treeList.treeInsert(root, 10)
treeList.treeInsert(root, 12)
treeList.treeInsert(root, 15)
#        treeInsert(root, 25);
treeList.treeInsert(root, 30)
treeList.treeInsert(root, 36)

print("tree:")
treeList.printTree(root) # 1 2 3 4 5
print()

print("list:")
head =treeList.treeToList(root);
treeList.printList(head) # 1 2 3 4 5


