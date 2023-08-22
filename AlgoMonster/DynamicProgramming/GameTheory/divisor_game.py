"""
Divisor Game

James and Oliver take turns playing a game, with James starting first.

Initially, there is a number N on the chalkboard. On each player's turn, that player makes
a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0 where 1 <= N <= 1000.
    Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if James wins the game, assuming both players play optimally.
Example 1:
Input: 2
Output: true
Explanation:

James chooses 1, and Oliver has no more moves.

Example 2:
Input: 3
Output: false
Explanation:

James chooses 1, and Oliver chooses 1, and James has no more moves.
"""