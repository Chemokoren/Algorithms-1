"""
class Solution {
public int[] solution(int[] A, int[] B) {

// The task is to find out the number of ways
// someone can climb up a ladder of N rungs
// by ascending one or two rungs at a time.
// It is not very hard to see that
// this number is just the "Fibonacci number of order N"

// we implemented an easy dynamic programming approach
// to compute Fibonacci numbers, this will take complexity O(n)

// I use binary operators to keep track of "N modulo 2^{30}"
// otherwise.the Fibonacci numbers will cause a memory overflow (be careful~!!)
// and we are also asked to


return "numbers modulo some power of 2"

int
L = A.length;

// determine
the
"max"
for Fibonacci
    int
    max = 0;
for (int i = 0; i < L; i++) {
    max = Math.max(A[i], max);
}
// max += 2; // for Fibonacci

int[]
fibonacci = new
int[max + 1]; // plus
one
for "0"

// initial
setting
of
Fibonacci(importnat)
fibonacci[0] = 1;
fibonacci[1] = 1;

for (int i=2; i <= max; i++){
    fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2]) % (1 << 30);
// we want to find the result of "a number modulo 2^P"
// if we first let the number modulo 2 ^ Q (Q > P)
// then, modulo 2 ^ P, the esult is the same.
// So, "we first modulo 2^30" to avoid overflow
// where, 2 ^ 30 == 1 << 30
}

// to
find
"results"
int[]
results = new
int[L];

for (int i=0; i < L; i++){
    results[i] = fibonacci[A[i]] % (1 << B[i]); // where, "1 << B[i]" means 2 ^ B[i]
}

return results;
}
}


# solution 2 
class Solution {
      public int[] solution(int[] a, int[] b) {

        int[] result = new int[a.length];

        int n = getMax(a);
        int p = getMax(b);

        int[] cache = buildCache(n, p);

        for (int i = 0; i<a.length; i++) {
            result[i] = cache[a[i]] % (int) Math.pow(2, b[i]);
        }

        return result;
    }

    private static int getMax(int[] array) {
        int max = array[0];

        for (int i = 0; i<array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        return max;
    }

    public static int[] buildCache(int n, int p) {
        int[] cache = new int[n+1];
        int previous  = 1;
        int current = 1;

        cache[0] = 1;
        cache[1] = 1;

        int index = 3;

        while (index <= n+1){
            int temp = current;
            current = (previous + current)  % (int) Math.pow(2, p);
            previous = temp;

            cache[index-1] = current;

            index++;
        }

        return cache;
    }
}

"""


# Detected time complexity:
# O(L)
# Task Score 100%
# Correctness 100%
# Performance 100%
def solution(A, B):
    limit = len(A)  # The possible largest N rungs
    result = [0] * len(A)  # The result for each query
    B = [(1 << item) - 1 for item in B]  # Pre-compute B for optimization
    # Compute the Fibonacci numbers for later use
    fib = [0] * (limit + 2)
    fib[1] = 1
    for i in range(2, limit + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    for i in range(limit):
        # To climb to A[i] rungs, you could either
        # come from A[i]-1 with an one-step jump
        # OR come from A[i]-2 with a two-step jump
        # So from A[i] rungs, the number of different ways of climbing
        # to the top of the ladder is the Fibonacci number at position
        # A[i] + 1
        result[i] = fib[A[i] + 1] & B[i]
    return result



#solution 2
def solution2(A, B):
    limit = len(A)
    result = [0] * len(A)
    fib = [0] * (limit+2)
    fib[1] = 1
    for i in range(2, limit + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    for i in range(limit):
        result[i] = fib[A[i]+1] % (1<<B[i])
    return result


# solution 3


def solution3(A, B):
    limit    = max(A)                 # The possible largest N rungs
    result   = [0] * len(A)           # The result for each query
    modLimit = (1 << max(B)) - 1      # To avoid big interger in fibs
    # Compute the Fibonacci numbers for later use
    fib    = [0] * (limit+2)
    fib[1] = 1
    for i in range(2, limit + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) & modLimit
    for i in range(len(A)):
        # To climb to A[i] rungs, you could either
        # come from A[i]-1 with an one-step jump
        # OR come from A[i]-2 with a two-step jump
        # So from A[i] rungs, the number of different ways of climbing
        # to the top of the ladder is the Fibonacci number at position
        # A[i] + 1
        result[i] = fib[A[i]+1] & ((1<<B[i])-1)
    return result


#Bad solution:

def solution4(A, B):

    limit = len(A)

    result = [0] * len(A)


    fib = [0] * (limit+2)

    fib[1] = 1

    for i in range(2, limit + 2):

        fib[i] = fib[i - 1] + fib[i - 2]


    for i in range(limit):

        result[i] = fib[A[i]+1] % (1<<B[i])


    return result
