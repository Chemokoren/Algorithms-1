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
        # self.locked ={i : None for i in range(len(parent))} - alternative 
        self.locked = [None] * len(parent)
        self.child = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    # O(1) time
    def lock(self, num: int, user: int)->bool:
        if self.locked[num]: return False
        self.locked[num] = user
        return True

    # O(1) time
    def unlock(self, num:int, user:int)->bool:
        if self.locked[num] != user: return False
        self.locked[num] =None
        return True

    # O(n) time because for a node we have to go through all of its descendants
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
    

# ["LockingTree","upgrade","upgrade","upgrade","upgrade","upgrade","lock","unlock",
#  "upgrade","upgrade","upgrade","lock","upgrade","upgrade","upgrade","lock",
#  "unlock","upgrade","unlock","unlock","upgrade"]
# [[[-1,4,9,0,6,3,1]],[9,43],[4,27],[5,34],[7,31],[4,27],[2,47],[7,21],[4,12],[1,1],
#  [8,20],[5,50],[5,28],[0,11],[6,19],[9,27],[5,6],[0,5],[4,49],[4,22],[5,27]]


# Test Case: Basic Locking and Unlocking

lt = LockingTree([-1, 0, 0, 1, 1, 2])  # Create a LockingTree with parent list [-1, 0, 0, 1, 1, 2]
print(lt.lock(3, 1) == True)  # Lock node 3 with user 1
print(lt.locked == [None, None, None, 1, None, None])  # The locked list should be updated
print(lt.lock(3, 2) == False)  # Attempt to lock node 3 with a different user should fail
print(lt.unlock(3, 2) == False)  # Attempt to unlock node 3 with a different user should fail
print(lt.unlock(3, 1) == True)  # Unlock node 3 with the correct user
print(lt.locked == [None, None, None, None, None, None])  # The locked list should be updated


print("\n####### Test Case: Upgrading Lock #######\n")

lt = LockingTree([-1, 0, 1, 2])  # Create a LockingTree with parent list [-1, 0, 1, 2]
print(lt.lock(2, 1) == True)  # Lock node 2 with user 1
print(lt.locked == [None, None, 1, 1])  # The locked list should be updated
print(lt.upgrade(2, 1) == True)  # Upgrading the lock on node 2 to exclusive lock should be successful
print(lt.locked == [None, None, 1, None])  # The locked list should be updated


print("\n#######  Test Case: Failing to Upgrade Lock #######\n")

lt = LockingTree([-1, 0, 1, 2])  # Create a LockingTree with parent list [-1, 0, 1, 2]
print( lt.lock(2, 1) == True)  # Lock node 2 with user 1
print( lt.locked == [None, None, 1, 1])  # The locked list should be updated
print( lt.upgrade(0, 1) == False)  # Attempt to upgrade lock on node 0 should fail as it has locked descendants
print( lt.locked == [None, None, 1, 1])  # The locked list should remain unchanged

print("\n#######  Test Case: Locking Descendants Prevent Upgrade #######\n")
lt = LockingTree([-1, 0, 1, 2])  # Create a LockingTree with parent list [-1, 0, 1, 2]
print( lt.lock(1, 1) == True)  # Lock node 1 with user 1
print( lt.locked == [None, 1, 1, None])  # The locked list should be updated
print( lt.upgrade(0, 1) == False)  # Attempt to upgrade lock on node 0 should fail as it has locked descendants
print( lt.locked == [None, 1, 1, None])  # The locked list should remain unchanged

print("\n#######  Test Case: Locking Cycle #######\n")
lt = LockingTree([-1, 0, 1, 2])  # Create a LockingTree with parent list [-1, 0, 1, 2]
print(lt.lock(0, 1) == True)  # Lock node 0 with user 1
print( lt.lock(1, 2) == True)  # Lock node 1 with user 2
print( lt.lock(2, 3) == True)  # Lock node 2 with user 3
print( lt.locked == [1, 2, 3, None])  # The locked list should be updated
print( lt.upgrade(2, 3) == False)  # Attempt to upgrade lock on node 2 should fail due to locked ancestors
print( lt.locked == [1, 2, 3, None])  # The locked list should remain unchanged

print("\n#######  Test Case: Unlocking Root Node #######\n")
lt = LockingTree([-1, 0, 1, 2])  # Create a LockingTree with parent list [-1, 0, 1, 2]
print(lt.lock(0, 1) == True)  # Lock node 0 with user 1
print( lt.locked == [1, None, None, None])  # The locked list should be updated
print( lt.unlock(0, 2) == False)  # Attempt to unlock node 0 with a different user should fail
print( lt.unlock(0, 1) == True)  # Unlock node 0 with the correct user
print( lt.locked == [None, None, None, None])  # The locked list should be updated

