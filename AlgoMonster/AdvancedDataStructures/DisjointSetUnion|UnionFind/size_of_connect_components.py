"""
Union Find | Disjoint Set Union | Set Size

    Prereq: Disjoint Set Union Review

For this problem we now ask you to do something similar to the introductory problem, but this time instead of checking whether or not 2 values belong to the same set, we want to know the size of the set that a value belongs to. Therefore, we now support a different set of 2 operations:

    merge(x, y) merge the sets that x and y belong to,
    count(x) returns the size of the set that x belongs to.

Example:

merge(1, 2)

merge(2, 3)

count(3) => 3

count(4) => 1

Explanation:

We merge elements 1 and 2 then we merge the set of 1 and 2 with the element 3, so we 
should have now have 2 sets, [1, 2, 3] and [4]. Therefore the set that 3 belongs to 
contains 3 elements, while the set that 4 belongs to contains 1 element.


"""

class SetCounter:
    def merge(self, x: int, y: int) -> None:
        # WRITE YOUR BRILLIANT CODE HERE
        pass

    def count(self, x: int) -> int:
        # AND HERE
        return 0

if __name__ == '__main__':
    sol = SetCounter()
    for _ in range(int(input())):
        op, *args = input().split()
        if op == 'union':
            [x, y] = map(int, args)
            sol.merge(x, y)
        elif op == 'count':
            [x] = map(int, args)
            res = sol.count(x)
            print(res)