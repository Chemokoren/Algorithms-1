from collections import deque
from typing import List
"""
Operations on Tree

You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent
array parent where parent[i] is the parent of the ith node. The root of the tree is
node 0, so parent[0] =-1 since it has no parent. You want to design a data structure
that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

-Lock: Locks the given node for the given user and prevents other users from locking
the same node. You may only lock a node if the node is unlocked.
-unlock: unlocks the given node for the given user. You may only unlock a node if it
is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants.
You may only upgrade a node if all 3 conditions are true:
- The node is locked, 
- It has at least one locked descendant (by any user), and
- It does not have any locked ancestors.

Implement the LockingTree class:
-LockingTree(int[] parent) initialies the data structure with the parent array.
-lock(int num, int user) returns true if it is possible for the user with id user
to lock the node num, or false otherwise. If it is possible, the node num will
become locked by the user with id user.
-unlock(int num, int user) returns true if it is possible for the user with id user
to unlock the node num, or false otherwise. If it is possible, the node num will 
become unlocked.
-upgrade(int num, int user) returns true if it is possible for the user with id user
to upgrade the node num, or false otherwise. If it is possible, the node num will be 
upgraded.

"""

class LockingTree:

    def __init__(self, parent: List[int]) -> None:
        self.parent = parent

        self.locked = [None] * len(parent)
        self.child = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int)->bool:
        if self.locked[num]: return False
        self.locked[num] = user

    def unlock(self, num:int, user:int)->bool:
        if self.locked[num] != user: return False
        self.locked[num] =None
        return True

    def upgrade(self, num: int, user: int)->bool:
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]

        lockedCount, q=0, deque([num])
        while q:
            n = q.popleft()
            if self.locked[n]:
                self.locked[n]= None
                lockedCount +=1
            q.extend(self.child[n])

        if lockedCount > 0:
            self.locked[num] = user
        return lockedCount > 0