"""
(OA) 2021 | Partition Array

You have n marbles in your collection. Some marbles in your collection are the same, while other 
marbles are different. You have given each type of marble an ID. If two marbles have the same ID, 
they are the same type, otherwise they are different.

You are feeling generous today and you want to gift these marbles to your friends. To make it fair for
everyone, you want to follow these rules:

    Every marble you have must be gifted to exactly one friend.
    Everyone you have gifted must receive exactly k marbles.
    No two marbles of the same type can be gifted to the same person.

There is an indefinite amount of friends that you can gift to. As long as you follow the rules 
described above, you don't need to gift all your friends.

The question is: is it possible to follow these rules and gift out your marbles?

Parameter

    marbles: A list of integers indicating the marbles you have and their type.
    k: An integer indicating the amount of marbles you gift to each person.

Result

    A boolean indicating whether you can follow the rules described above and gift out your marbles.

Examples
Example 1:

Input:

marbles = [1, 2, 3, 4] k = 2

Output: true

Explanation: You can gift the first two marbles to your first friend and the last two marbles to your
other friend, so the answer is true.

Example 2:

Input:

marbles = [1, 2, 2, 4] k = 3

Output: false

Explanation: You cannot gift the marbles so that each of your friend has 3 marbles, so the answer is
false.

Constraints

    1 <= n <= 100000
    1 <= k <= n
    0 <= marbles[i] <= 10^9 for each 0 <= i < n

"""
from typing import List

def can_gift(marbles: List[int], k: int) -> bool:
    return False

if __name__ == '__main__':
    marbles = [int(x) for x in input().split()]
    k = int(input())
    res = can_gift(marbles, k)
    print('true' if res else 'false')