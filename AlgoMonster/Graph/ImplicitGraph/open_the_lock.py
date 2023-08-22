"""
Open the Lock

You commissioned a locksmith to craft a special combination lock for you, because you are a 
lich and you want to hide your phylactery in somewhere secure. It looks like a regular 4-digit
combination lock, with each digit can be one of the digits from 0-9.
Each digit can be turned forwards by 1 and backwards by 1, and the first and the last digit
is connected (9 goes to 0 when moving forward, and 0 goes to 9 when moving backward). The
lock starts at 0000.

However, because you don't want people to find your phylactery, you have trapped certain 
combinations of this combination lock. If someone were to set the combination to a trapped
combination, bad things happend to them, which this question would not elaborate upon

You know the combination, and you know the trapped combinations. You wonder if the lock can be
opened without triggering the traps, and if so, how many digit changes must be made to the lock 
to unlock it.

Input

- combo: a string representing the four digit combination to open the lock.
- trapped_combos: a list of strings representing the trapped combinations.

Output
An integer representing the number of steps it takes to open the lock, or -1 if you can't open
it without triggering the trap.

Example 1:

Input

combo = "0202"
trapped_combos =["0201","0101","0102","2002"]

Output: 6

0000->1000->1100->1200->1201->1202->0202 , a total of 6 steps

Constrains
-The starting combination (0000) and the final combination is not trapped because that defeats
the purpose of the lock.

"""
from typing import List

def num_steps(combo: str, trapped_combos: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    combo = input()
    trapped_combos = input().split()
    res = num_steps(combo, trapped_combos)
    print(res)