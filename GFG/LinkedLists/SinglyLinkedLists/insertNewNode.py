#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 04:45:35 2021

@author: kibsoft

program to demonstrate insertion methods of a linkedlist
"""

# Node class
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
#LL class contains a Node object
class LinkedList:
    def __init__(self):
        self.head =None
    
    # function to insert node at the beginning    
    def insertBeginning(self, new_data):
        #allocate the Node and put in the data
        new_node =Node(new_data)
        
        # make next of new Node as head
        new_node.next =self.head
        
        # moake the head to point to new Node
        self.head =new_node
        
        
    # function to insert a new node after a given prev_node
    def insertAfter(self, prev_node, new_data):
        #check if the given prev_node exists
        if prev_node is None:
            print("prev_node must exist")
            return
        # create new_node & put in the data
        new_node =Node(new_data)
        
        # make next of new_node as next pf prev_node
        new_node.next =prev_node.next
        
        # make next of prev_node as new_node
        prev_node.next =new_node
    
    # append new node at the end
    def insertEnd(self, new_data):
        
        # create new_node, add new_data, set next as None
        new_node =Node(new_data)
        
        # if LL is empty, make new_node as head
        if self.head is None:
            self.head =new_node
            return
        
        # traverse till the last node
        last =self.head
        while(last.next):
            last =last.next
            
        # change next of last node to the new_node
        last.next =new_node
        
    # print the LL
    def printList(self):
        temp =self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    # Insert 6.  So linked list becomes 6->None
    llist.insertEnd(6)
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.insertBeginning(7);
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.insertBeginning(1);
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.insertEnd(4)
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
  
    print('Created linked list is:', llist.printList())
  

