"""
In unbalanced binary search tree, the worst time complexity is O(n)

This time, you'll implement search() and insert(). You should rewrite search() and not use your code from the
last exercise so it takes advantage of BST properties. Feel free to make any helper functions you feel like
 you need, including the print_tree() function from earlier for debugging. You can assume that two nodes 
 with the same value won't be inserted into the tree. 

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root, new_val)

    def insert_helper(self,start, new_val):
        if start:
            if start.value > new_val:
                self.insert_helper(start.left,new_val)
            elif self.root.value <new_val:
                self.insert_helper(start.right, new_val)
        else:
            start =Node(new_val)

    def insert_helper_updated(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper_updated(current.right, new_val)
            else:
                current.right =Node(new_val)
        else:
            if current.left:
                self.insert_helper_updated(current.left, new_val)
            else:
                current.left = Node(new_val)
        

    
    def search(self, find_val):
        return self.search_helper(self.root,find_val)

    def search_helper(self,start, find_val):
        
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                # check left root
                return self.search_helper(start.left, find_val)
            else:
                # check right
                return self.search_helper(start.right, find_val)
        else:
            return False
        
    def search_helper_updated(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper_updated(current.right, find_val)
            else:
                return self.search_helper_updated(current.left, find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
