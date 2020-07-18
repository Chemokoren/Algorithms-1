"""
1. MinMaxDivision
Divide array A into K blocks and minimize the largest sum of any block.
Task Score
100%
Correctness
100%
Performance
100%
Task description
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].

"""
def solution(K, M, A):
    min = 0
    max_val = 0
    # get the sum as max, and the largest number as min
    for i in range (0,len(A)):
        max_val += A[i]
        min =max(min, i)

    result = max_val
    while (min <= max_val):
        mid = (min + max_val) // 2
        if (divisionSolvable(mid, K - 1, A)):
            max_val = mid - 1
            result = mid
        else:
             min = mid + 1

    return result

def divisionSolvable(mid, k, a):
    sum = 0
    for i  in range(0,len(a)):
        sum += a[i]
        if (sum > mid):
            sum = a[i]
            k =k-1
        if (k < 0):
            return False
        return True

# solution 2
# Detected time complexity:
# O(N*log(N+M))
# Task Score # 100%
# Correctness # 100%
# Performance # 100%
def blockSizeIsValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_cnt = 0

    for element in A:
        if block_sum + element > max_block_size:
            block_sum = element
            block_cnt += 1
        else:
            block_sum += element
        if block_cnt >= max_block_cnt:
            return False

    return True


def binarySearch(A, max_block_cnt, using_M_will_give_you_wrong_results):
    lower_bound = max(A)
    upper_bound = sum(A)

    if max_block_cnt == 1:      return upper_bound
    if max_block_cnt >= len(A): return lower_bound

    while lower_bound <= upper_bound:
        candidate_mid = (lower_bound + upper_bound) // 2
        if blockSizeIsValid(A, max_block_cnt, candidate_mid):
            upper_bound = candidate_mid - 1
        else:
            lower_bound = candidate_mid + 1

    return lower_bound


def solution1(K, M, A):
    return binarySearch(A, K, M)


# solution 3
# javascript
"""
function solution(K, M, A) {
  // M is a red herring
  return minimalLargeSumBinarySearch(K, A);
}

function minimalLargeSumBinarySearch(maxNumBlocks, arra) {
  var lowerBoundLargeSum = Math.max.apply(null, arra);
  var upperBoundLargeSum = arra.reduce((a,c)=>a+c,0);
  var result = -1;
  
  while (lowerBoundLargeSum <= upperBoundLargeSum) {
    var tentativeLargeSum = Math.floor((lowerBoundLargeSum+upperBoundLargeSum)/2);
    if (tentativeLargeSumIsPossible(arra, maxNumBlocks, tentativeLargeSum)) {
      result = tentativeLargeSum; // OK, but...
      // try a smaller one
      upperBoundLargeSum = tentativeLargeSum - 1;
    } else {
      // try a larger one
      lowerBoundLargeSum = tentativeLargeSum + 1;
    }
  }
  return result;
}

function tentativeLargeSumIsPossible(arra, maxNumBlocks, tentativeLargeSum) {
  var curBlockSum = 0;
  var numBlocks = 1; // at least...
  
  for (let elem of arra) {
    if (curBlockSum + elem <= tentativeLargeSum) {
      // make curBlock bigger
      curBlockSum += elem;
    } else {
      // start a new block containing element
      numBlocks++;
      curBlockSum = elem;
    }
    if (numBlocks > maxNumBlocks) return false;
  }
  return true;
}
"""


a = [ 2, 1, 5, 1, 2, 2, 2];
# (3, 5, [2, 1, 5, 1, 2, 2, 2])
print(solution1(3, 5, a));

