from LinkedListDS.LinkedList import LinkedList

linkedList =LinkedList()

linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertEnd(3)
linkedList.insertStart(31)

linkedList.traverseList()
linkedList.remove(12)
print("################## second traversal ######################")
linkedList.traverseList()
