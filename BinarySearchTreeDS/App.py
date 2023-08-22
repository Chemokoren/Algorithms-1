from BinarySearchTreeDS.BST import BST

bst =BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

print(bst.getMax())
print("###################### first traversal #####################")
bst.traverseInOrder()
bst.remove(10)
print("###################### second traversal #####################")
bst.traverseInOrder()