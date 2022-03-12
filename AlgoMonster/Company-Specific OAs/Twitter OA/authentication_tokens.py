"""
(OA) 2021 | Authentication Tokens

Most websites that requires user login now utilize a "token" system. Every time a user logs into the 
website, they are issued a token so that when they go to the website again, they are authenticated 
with the token so they don't have to log in again. Usually a token has an expiration time so that 
after certain amount of inactivity, the token is voided.

In this particular system, there are two commands:

    0 <token_id> <time>: Generates a token token_id at time minutes. The token is valid for expiry_time
    minutes unless it is reset. This operation can only be done on a token that does not already exist. If a token with this ID already exist, regardless of whether it is active or expired, nothing happens.
    1 <token_id> <time>: Resets the token whose ID is token_id at time minutes. This operation resets 
    the expiry timer so that this token will be valid for expiry_time minutes from time unless it is
    reset again. The token must exist and be active when this operation is performed. If the token 
    does not already exist, or is already expired, this operation does nothing. A token can be reset 
    multiple times, as long as each time the token is still valid.

Given a list of operations sorted chronologically, determine how many tokens are still active after 
the final operation.
Parameters

    expiry_time: How long since the token was generated or reset before it expires.
    operations: An integer matrix with n rows. Each row has 3 entries: operation, token_id, and time, 
    representing an operation.

Result

    The number of tokens still valid after the final operation.

Examples
Example 1:

Input:

expiry_time = 4

operations = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]

Output: 1

Explanation: Token 1 is initialized at T = 1 and token 2 is initialized at T = 2. When token 1 is
reset at T = 5, it is still in the active period, so the token's lifespan is increased to T = 5 + 4 = 9. 
When token 2 is reset at T = 7, it already expired so nothing happens. After this operation, only 
token 1 is still valid.

Restrictions

    1 <= expiry_time <= 10^8
    1 <= n <= 10^5
    1 <= token_id <= 10^8
    1 <= T <= 10^8

"""
from typing import List

def active_tokens(expiry_time: int, operations: List[List[int]]) -> int:
    return 0

if __name__ == '__main__':
    expiry_time = int(input())
    operations = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = active_tokens(expiry_time, operations)
    print(res)