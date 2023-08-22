"""
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness
should be constant.
However, it should have different heights in different places. The height of the wall is specified
by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the
right of its left end.
In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular).
Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    def solution(H)

that, given an array H of N positive integers specifying the height of the wall,
returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].


"""


# solution 1


def solution1(H):

    block_count = 0
    # stack is used to hold height used to building and remove all the blocks from it,
    # if any of the block of stack is greater than current block(to be added for building)
    stack = []
    for height in H:
        print(" ")
        print("Current Height " + str(height))
        print("Current stack " + str(stack))
        # Remove all blocks that are bigger than current height, stack should not be empty
        while stack and stack[-1] > height:
            stack.pop()
        print("After remove bigger blocks than current height, stack is " + str(stack))

        # stack is not empty and top item of stack is equal to current height
        if stack and stack[-1] == height:
            # Already used this size of block
            print("Already used this size of block " + str(height))
            continue
        else:
            # new block is required, push it's size to the stack
            block_count += 1
            stack.append(height)
            print("Add this block.... " + str(height) + " Minimum Blocks " + str(block_count))

    return block_count

# solution 2
def solution(H):
    stack, count = [], 1
    for i in H:
        if stack:
            if i == stack[-1]:
                continue
            if i < stack[-1]:
                while stack and stack[-1] > i:
                    stack.pop()
            if stack:
                if i > stack[-1]:
                    count+=1
                    stack.append(i)
            else:
                count+=1
                stack.append(i)
        else:
            stack.append(i)
    return count


if __name__ == '__main__':

    result = solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
    print("")
    print("Solution " + str(result))
