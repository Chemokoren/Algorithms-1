"""
Decode Ways

We have a message to decode. Letters are encoded to digits by its position in the alphabet
1 A->1
2 B->2
3 C->3
4 ...
5 Y->25
6 Z->26

Given a non-empty string of digits, how many ways are there to decode it?

Input: "18"
Output: 2

Explanation : "18" can be decoded as "AH" or "R"

Input: "123"
Output: 3
Explanation: "123" can be decoded as "ABC","LC", "AW"

"""

def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    digits = input()
    res = decode_ways(digits)
    print(res)

    