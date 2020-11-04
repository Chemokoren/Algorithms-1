# For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:
#
# val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
#
# (Assume that the sum of zero elements equals zero.)
#
# For a given array A, we are looking for such a sequence S that minimizes val(A,S).
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.
#
# For example, given array:
#
#   A[0] =  1
#   A[1] =  5
#   A[2] =  2
#   A[3] = -2
# your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..20,000];
# each element of array A is an integer within the range [−100..100].

#
# MinAbsSum
# Given array of integers, find the lowest absolute sum of elements.
# Detected time complexity: O(N**2 * max(abs(A)))
# Task Score # 54% # Correctness # 83%  # Performance #20%
def solution(A):
    a = [abs(s) for s in A]
    su = sum(a)
    ta = su // 2

    dp = [[0 for _ in range(ta + 1)] for _ in range(len(a))]
    for i in range(a[0], ta + 1): dp[0][i] = a[0]
    for i in range(1, len(a)):
        for j in range(ta + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= a[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + a[i])

    return su - dp[-1][-1] - dp[-1][-1]


# Detected time complexity: O(N**2 * max(abs(A)))
# Task Score # 63% # Correctness # 100% # Performance # 20%
def solution2(A):
    # write your code in Python 3.6
    a = [abs(s) for s in A]
    su = sum(a)

    dp = [False for _ in range(su // 2 + 1)]
    dp[0] = True
    dp2 = dp.copy()
    for i in a:
        for p in range(i, su // 2 + 1):
            dp2[p] = dp[p] | dp[p - i]
        for p in range(i, su // 2 + 1):
            dp[p] = dp2[p]

    for i in range(su // 2, -1, -1):
        if dp[i]: return su - 2 * i


# you can write to stdout for debugging purposes, e.g.

from collections import Counter
def solution3(A):
    # write your code in Python 3.6
    if len(A) == 0: return 0
    if len(A) == 1: return abs(A[0])
    a = [abs(s) for s in A]
    su = sum(a)
    ma = max(a)
    d = Counter(a)

    dp = [-1 for _ in range(su // 2 + 1)]
    dp[0] = 0
    for i in range(1, ma + 1):
        if i not in d: continue
        for p in range(su // 2 + 1):
            if dp[p] >= 0: dp[p] = d[i]  # dp [p] can be reached, completely without the use of A [i]
            elif p >= i and dp[p] > 0: dp[p] = dp[p] - 1  # dp array even after many assignments, but DP [pi] represents a certain time to pi, left DP [pi ] a i

    for i in range(su // 2, -1, -1):
        if dp[i] >= 0: return su - 2 * i


# It goes through the array's elements one by one. Since we're adding consecutive numbers all we need to do is to make sure, that the sum does not get smaller. That's why we take a number and check how the sum changes.
#
# Formally we can write this the following way:
#
# max(solution([a1, a2, ..., an]) = sum(abs(a1), abs(a2), ..., abs(an)),
# where abs denotes the absolute value (|x| = x * signum(x)).

# solution 4
public static int solution(int[] A) {

    int N = A.length;

    if (N == 0) {
        return 0;
    }

    int sum = 0;
    int max = Integer.MIN_VALUE;

    for (int i = 0; i < N; i++) {

        int value = Math.abs(A[i]);
        sum += value;

        if (max < value) {
            max = value;
        }

        A[i] = value;
    }


    // A      = [1, 5, 2, -2]
    // A(abs) = [1, 5, 2, 2]

    // Max value = 5
    // Sum value = 10

    // counts  = [0, 1, 2, 0, 0, 1]
    int[] counts = new int[max + 1];

    for (int value : A) {
        counts[value]++;
    }

    // Total = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    int[] Total = new int[sum + 1];

    for (int i = 1; i < Total.length; i++) {
        Total[i] = -1;
    }

    for (int i = 1; i < counts.length; i++) {

        for (int j = 0; j < Total.length; j++) {

            if (Total[j] >= 0) {
                Total[j] = counts[i];
            } else if (j - i >= 0 && Total[j - i] > 0) {
                Total[j] = Total[j - i] - 1;
            }
        }
    }

    int result = sum;

    for (int i = 0; i < Total.length / 2 + 1; i++) {

        if (Total[i] >= 0 && result > Math.abs(sum - 2 * i)) {
            result = Math.abs(sum - 2 * i);
        }
    }

    return result;
}



# solution 5
# Detected time complexity: O(N * max(abs(A))**2) or O(N**2 * max(abs(A)))
# Task Score 90% Correctness 100% Performance 80%

public class MinAbsSum {
    public int solution(int[] a) {
        if (a.length == 0) {
            return 0;
        }
        int sum = 0;
        int max = Integer.MIN_VALUE;
        // O(N)
        for (int i = 0; i < a.length; i++) {
            final int value = Math.abs(a[i]);
            sum += value;
            if (max < value) {
                max = value;
            }
            a[i] = value;
        }
        // O(max(abs(a))) space but no more than O(sum(abs(a))), so ignore it
        // O(N)
        final int[] counts = new int[max + 1];
        for (int value: a) {
            counts[value]++;
        }
        // O(sum(abs(a)))
        final int[] r = new int[sum + 1];
        for (int i = 1; i < r.length; i++) {
            r[i] = -1;
        }
        // outer is O(max(abs(a)))
        // inner is O(sum(abs(a))) which is less than O(N * max(abs(a)))
        // we don't care of 0 values
        for (int i = 1; i < counts.length; i++) {
            // we check r[j]. if it's not less than 0, then it means we've reached j value with previous steps, so no need to spend current
            // if it's less than 0, spend 1 current number if r[j - i] has been reached
            for (int j = 0; j < r.length; j++) {
                // negative value means we haven't reached this value, so we have to spend 1 current if we can
                if (r[j] >= 0) {
                    r[j] = counts[i];
                } else if (j - i >= 0 && r[j - i] > 0) {
                    r[j] = r[j - i] - 1;
                }
                // the value in r[j] then means how many of the current values are left when we reached the value j
            }
        }
        int result = sum;
        // don't have to traverse all the arrays, since i - the sum of elements. if it's reachable then (sum - i) - reachable as well.
        // so if the value is reachable then the diff is abs(i - (sum - i)), which is the same as abs(sum - 2 * i)
        for (int i = 0; i < r.length / 2 + 1; i++) {
            if (r[i] >= 0 && result > Math.abs(sum - 2 * i)) {
                result = Math.abs(sum - 2 * i);
            }
        }
        return result;
    }
}


# solution 6
public static int solution(int[] A) {

        int N = A.length;

        int sum = 0;
        int max = 0;

        for (int i = 0; i < N; i++) {

            A[i] = Math.abs(A[i]);
            sum += A[i];

            max = Math.max(A[i], max);
        }


        int[] counts = new int[max + 1];

        for (int i = 0; i < N; i++) {
            counts[A[i]] += 1;
        }

        int[] Total = new int[sum + 1];

        Arrays.fill(Total, -1);
        Total[0] = 0;

        // Segment I
        for (int i = 1; i <= max; i++) {

            if (counts[i] > 0) {

                for (int j = 0; j <= sum; j++) {

                    // j th index is zero or positive
                    if (Total[j] >= 0) {
                        Total[j] = counts[i];
                    }
                    // (i-j) th index is positive
                    else if ((j - i) >= 0 && Total[j - i] > 0) {
                        Total[j] = Total[j - i] - 1;
                    }
                }
            }
        }

        int result = sum;

        // Segment II
        for (int i = 0; i < sum / 2 + 1; i++) {

            // i- th index if zero or positive
            // BODMAS_RULE = {Brackets, Orders, Division, Multiplication, Addition, Subtraction}
            if (Total[i] >= 0) {
                result = Math.min(result, sum - 2 * i);
            }
        }

        return result;
    }


# solution 7
# Detected time complexity: O(N * max(abs(A))**2)
# Task Score # 100% # Correctness # 100% # Performance # 100%

def solution7(A):
    # Since S could be 1 or -1, it does not matter that

    # each element in A is positive or negative.

    A = [abs(item) for item in A]

    sumOfA = sum(A)

    # Get the number distribution. So we do not need to try

    # each number for multiple times.

    numbers = {}

    for item in A:  numbers[item] = numbers.get(item, 0) + 1

    # This is the KEY point.

    # Typically, we will use possible = [False] * len to track, which numbers

    # could be the result by summing up subsets of A.

    # For a number, appeared for many times, there will be multiple attempts

    # for it. But in this way, when we are trying number n,

    # possible[i] == -1 means it is impossible.

    # possible[i] == i >= 0 means it is possible and there are i n(s) left to use.

    # So for ALL number n(s), we only need ONE scan over the record.

    possible = [-1] * (sumOfA // 2 + 1)

    possible[0] = 0

    for number in numbers:  # Try each distinct number

        for trying in range(sumOfA // 2 + 1):

            if possible[trying] >= 0:

                # Can be reached with previous numbers

                possible[trying] = numbers[number]

            elif trying >= number and possible[trying - number] > 0:

                # Cannot be reached with only previous numbers.

                # But could be achieved with previous numbers AND current one.

                possible[trying] = possible[trying - number] - 1

    # Divide the A into two parts: P and Q, with restriction P <= Q.

    # So P <= sumOfA // 2 <= Q. We want the largest possible P, so that

    # Q-P is minimized.

    for halfSum in range(sumOfA // 2, -1, -1):

        if possible[halfSum] >= 0:
            return sumOfA - halfSum - halfSum

    raise Exception("Should never be here!")

    return 0


print(solution([]))
print(solution([1, 5, 2, 2]))
print(solution([1, 5, 2, -2]))
print(solution([1, 2, 100]))

# my_array =[1, 5, 2, -2]
# my_array =[1,2,100]
my_array =[1,5,2,-2]




print(solution2(my_array))