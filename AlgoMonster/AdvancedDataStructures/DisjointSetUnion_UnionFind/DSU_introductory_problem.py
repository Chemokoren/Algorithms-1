"""
Union Find | Disjoint Set Union Introductory Problem

    Prereq: Depth First Search Review

Now we will start with an introductory problem to get you familiar with the data structure. Complete the class below to support the following two operations:

    merge(x, y) merges the sets that the x and y belong to,
    is_same(x, y) determines if x and y belong to the same set. If so return true, otherwise false.

Example:

merge(1, 2)

merge(2, 3)

is_same(1, 3) => true

is_same(2, 4) => false

Explanation:

We merge elements 1 and 2 then we merge the set of 1 and 2 with the element 3, so we 
should have now have 2 sets, [1, 2, 3] and [4]. Therefore 1 and 3 are in the same set,
while 2 and 4 are in different sets.


"""
class SameSet:
    def merge(self, x: int, y: int) -> None:
        # WRITE YOUR BRILLIANT CODE HERE
        pass

    def is_same(self, x: int, y: int) -> bool:
        # AND HERE
        return False

if __name__ == '__main__':
    sol = SameSet()
    for _ in range(int(input())):
        op, *args = input().split()
        x, y = map(int, args)
        if op == 'union':
            sol.merge(x, y)
        elif op == 'is_same':
            res = sol.is_same(x, y)
            print('true' if res else 'false')