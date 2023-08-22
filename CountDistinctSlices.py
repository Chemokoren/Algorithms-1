
# solution
# Complexity:
# expected worst-case time complexity is O(N);
#
# expected worst-case space complexity is O(M)
#
# Execution:
# Using the caterpillar method I expand the caterpillar to the right as long as a duplicate element is found. The right side has to retract as long as this duplicate element has been eliminated from the next slice. An observation showed that the number of sub-slices is equal to front-back+1.
def solution(M, A):
    the_sum = 0
    front = back = 0
    seen = [False] * (M + 1)
    while (front < len(A) and back < len(A)):
        while (front < len(A) and seen[A[front]] != True):
            the_sum += (front - back + 1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1

            seen[A[back]] = False
            back += 1

    return min(the_sum, 1000000000)


#solution 1 -Javascript
# function solution(M, A) {
#   // write your code in JavaScript (Node.js 8.9.4)
#   const memory = new Set();
#   let count = 0;
#   let tail = 0;
#
#   for (let i = 0; i < A.length; i++) {
#     if (!memory.has(A[i])) {
#       memory.add(A[i]);
#       continue;
#     }
#     count += slices(i - tail);
#     while (A[tail] !== A[i]) {
#       memory.delete(A[tail]);
#       tail++;
#     }
#     tail++;
#     count -= slices(i - tail);
#   }
#   count += slices(A.length - tail);
#   return Math.min(count, 1000000000);
# }
#
# function slices(n) {
#     return n * (n + 1) / 2;
# }

# solution 2
def solution2(M, A):
    rst = 0
    start = 0
    duplicate = 0
    n = len(A)
    mp = {}
    for i, v in enumerate(A):
        if v > M:
            rst += (i-start)*(i-start+1)//2
            start = i + 1
            continue
        if v not in mp:
            mp[v] = i
        else:
            if mp[v] >= start:
                rst += (i-start)*(i-start+1)//2
                start = mp[v] + 1
            if start < i:
                duplicate += (i - start) * (i - start + 1) //2
                mp[v] = i
                rst += (n-start)*(n-start+1)//2
    return min(int(1e9),rst - duplicate)

# solution 3 -java
# class Solution {
#     public int solution(int M, int[] A) {
#
#         // This solution is more clever, and much faster O(n)
#
#         // main idea:
#         // use "boolean[]" to record if an integer is already seen
#         // also use "leftEnd" and "rightEnd"
#
#         boolean[] seen = new boolean[M+1]; // from 0 to M
#         // Arrays.fill(seen, false); // note: "false" by default
#
#         int leftEnd=0;
#         int rightEnd=0;
#         int numSlice =0;
#
#         // key point: move the "leftEnd" and "rightEnd" of a slice
#         while(leftEnd < A.length && rightEnd < A.length){
#
#             // case 1: distinct (rightEnd)
#             if( seen[A[rightEnd]] == false){
#                 // note: not just +1
#                 // there could be (rightEnd - leftEnd + 1) combinations (be careful)
#                 numSlice = numSlice + (rightEnd - leftEnd + 1);
#                 if(numSlice >= 1_000_000_000)
#                     return 1_000_000_000;
#
#                 // increase the slice to right by "1" (important)
#                 seen[A[rightEnd]] = true;
#                 rightEnd++;
#             }
#             // case 2: not distinct
#             else{
#                 // decrease the slice from left by "1" (important)
#                 // remove A[leftEnd] from "seen" (be careful)
#                 seen[A[leftEnd]] = false;
#                 leftEnd++;
#             }
#         }
#
#         return numSlice;
#     }
# }
print(solution2(6, [3, 4, 5, 5, 2]))
