"""
Reconstructing Sequence

Check whether the original sequence original can be uniquely reconstructed from the sequences
in seqs.

The original sequence is a permutation of the integers from 1 to n.

Reconstruction means building a shortest common supersequence of the sequences in seqs(i.e, a
shortest sequence so that all sequences in seqs are subsequences of it).

Determine whether there is only one sequence that can be reconstructed from seqs and it is the
original sequence.

Parameters

original: A list of integers of size n representing the original sequence.
seqs: A list of sequences of size m representing the sequences to be reconstructed.

Result

- true or false, depending on whether the original sequence can be uniquelly reconstructed.

Example 1:

Input: orgignal: [1,2,3], seqs: [[1,2], [1,3]]

Output: false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid
sequence that can be reconstructed.

Example 2:

Input: orgignal: [1,2,3], seqs: [[1,2]]

Output: false

Explanation:
The reconstructed sequence can only be [1,2]

Example 3:

Input: orginal: [1,2,3], seqs: [[1,2], [1,3], [2,3]]

Output: true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence[1,2,3].

Example 4:

Input: orgignal: [4,1,5,2,6,3], seqs: [[5,2,6,3], [4,1,5,2]]

Output: true

Constrains

1<= n <= 10^4
1 <= m <=  10^4
1 <= len(seqs[i]) <=n



"""
from typing import List

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return False

if __name__ == '__main__':
    original = [int(x) for x in input().split()]
    seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = sequence_reconstruction(original, seqs)
    print('true' if res else 'false')