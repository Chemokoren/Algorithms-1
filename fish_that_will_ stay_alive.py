"""
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
"""


def solution(A, B):
    # A -sizes of fish
    # B -directions of fish
    # P < Q
    # P -upstream
    # Q -downstream
    # P =A[P]B[P]

    # O- fish flowing upstream
    # 1 -fish flowing downstream
    final_val = 0
    for i in range(len(A)):
        # if i == A[len(A)]:
        #     final_val =1
        # if(A[len(A)]):
        #     print('come here')
        # print(A[len(A)-1])
        # print(A[i])
        if A[i] == A[len(A) - 1]:
            final_val = 1
            final_val += which_fish_eats_the_other(A[i], A[i + 1], A, B)
        return final_val


def which_fish_eats_the_other(P, Q, A, B):
    count_live_fish = 0
    if (P < Q and B[P] == 1 and B[Q] == 0):
        if A[P] > A[Q]:
            count_live_fish += 1
            print("P eats Q & still flowing downstream")
        if A[Q] > A[P]:
            count_live_fish += 1
            print("Q eats P & still flowing upstream")
    return count_live_fish


#
# solution 2
#
def solution1(A, B):
    totalFishes = 0
    downStream = []
    upStream = []
    direction = 0

    for i in range(A[len(A) - 1]):
        direction = B[i]
        if direction == 0:
            while len(downStream) > 0:
                d = downStream.pop()
            if d > A[i]:
                downStream.push(d)
                break
        if len(downStream) == 0:
            upStream.push(A[i])
        downStream.push(A[i])
    return len(downStream) + len(upStream)


#
# solution 3
#

def solution3(A, B):
    # special case: no fish
    if len(A) == 0:
        return 0;

        # main idea: use "stack" to store the fishes with B[i]==1
        # that is, "push" the downstream fishes into "stack"
        # note: "push" the Size of the downstream fish

    st = []
    numAlive = len(A);

    for i in range(len[A]-1):
        # case 1; for the fish going to downstrem
        # push the fish to "stack", so we can keep them from the "last" one
        B[i] == 1
        st.append(A[i]);  # push the size of the downstream fish

        # case 2: for the fish going upstream
        # check if there is any fish going to downstream
        if B[i] == 0:
            while len(st) != 0:
                # if the downstream fish is bigger (eat the upstream fish)
                if st.pop() > A[i]:
                    numAlive = numAlive - 1
            break;  # the upstream fish is eaten (ending)

            # if the downstream fish is smaller (eat the downstream fish)
        elif st.pop() < A[i]:
            numAlive = numAlive - 1
            st.pop();  # the downstream fish is eaten (not ending)

    return numAlive;


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution3(A, B))
