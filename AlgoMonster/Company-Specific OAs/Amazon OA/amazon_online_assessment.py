"""
Amazon Online Assessment Questions 2021/2022 Preparation | Amazon OA 2022

Amazon OA, i.e. Amazon Online Assessment on platforms such as Hackerrank or Codility is the first step
a candidate needs to take to get into an SDE role at Amazon. The assessment result will be used to 
decide if the candidate can move on to the phone or on-site (or virtual online aka VO) interviews.

Amazon OA1, OA2, OA3

You may have heard of the terms OA1, OA2, or even OA3. What this means is part 1, part 2 and part 3 of
the online assessment. OA 1 is debugging questions and OA2 is LeetCode style coding questions.
Sometimes there is also an OA3 which is a work style assessment with no coding.

If you are an experienced SDE you will likely only be required to pass one OA, the OA2. If you are 
interviewing for an Amazon SDE intern or new grad position, you will be required to write OA1 and OA2 
and maybe OA3.


Amazon OA1

OA1 is debugging and logic reasoning. For debugging, you will be given a short code with a subtle 
error and asked to fix the error. The common errors include incorrect loop conditions causing infinite
loop and off-by-one etc. Typically there are 5-7 debugging question. There may also be logic and 
reasoning questions or simple math questions. For example, given a sequence like this 
4 12 6 18 12 36 30, what should the next number be? The answer is 90 because you may notice the 
numbers in the even positions are 3x the numbers in the previous odd positioned number.

Amazon OA2

OA2 is the LeetCode style coding questions. You will be given one to two questions to solve in 1.5
hour. See the list below for practice.


Amazon OA3

OA3 is work style assessment and logic reasoning. For work style assessment, you will be put in a 
hypothetical situation and required to take the most “Amazonian” action. Be sure to review the 14 
leadership principles and use them to guide your choices.

Amazon Online Assessment Practice

Practice question	                                                Pattern

Robot Bounded in Box	                                            Math logic
Number Game	                                                        Bitmask
Find All Combination of Numbers Sum to Target / Shopping Options	DFS
Fill the Truck	                                                    Basic coding/greedy
Slowest key	                                                        Basic coding
Binary Tree Level Order Traversal	                                BFS
Longest Substring without Repeating Characters	                    Two Pointers
Five Star Seller	                                                Priority Queue/Heap
Subarray Sum Divisible by K	Prefix                                  Sum
Merge Two Sorted Lists	                                            Priority Queue/Heap
LRU Cache Misses	                                                Data Structure Design
Music Pairs	                                                        Two Pointers
Minimum Difficulty of a Job Schedule	                            Dynamic programming
Autoscaling Policy/Utilization Checks	                            Two Pointers
Optimal Utilization	                                                Two Pointers
Minimum Total Container Size	                                    Dynamic programming
Shopping Patterns	                                                Graph
Amazon Prime Air Route	                                            Two Pointers
Move The Obstacle	                                                Graph BFS
K Closest Points	                                                Priority Queue/Heap
Number of Swaps to Sort / Algorithm Swap	                        Divide and Conquer
Reorder Data in Log Files/Upgrading Junction Boxes	                Basic coding
Top K keywords	                                                    Priority Queue/Heap


Core Patterns Asked in Amazon Online Assessment and Virtual Onsite Interviews

Almost all Amazon questions can be solved using one of the following patterns.

    Two Pointers
    Breadth-first Search
    Depth-first Search
    Backtracking
    Heap and Priority Queue

Each pattern is divided into a number of sub-patterns. We have introduction articles and practice 
problems for each of sub-pattern. Make sure you know them well before going into the interview.

You may also need to know a little bit of dynamic programming but just the basics like coin change 
and house robber.

More frequently asked questions about Amazon OA:

Does amazon online assessment use webcam?

At the beginning of the OA, you will be asked to take a picture of your ID using the webcam. 
But the actual OA test is not recorded by webcam.

Is amazon online assessment timed?

Yes. The time may vary depending on the platform. On HackerRank it's typically 135 min.

Is amazon SDE online assessment proctored?

There is no human to proctor the assessment but you will be asked to take a picture of your ID at the
beginning of the test and your browser activity is monitored. So don't switch tabs too frequently -
it may get picked up as a signal for looking things on Google.

Can you google during amazon online assessment?

Your browser activity is monitored. So be sure to get familiar with the syntax and common data 
structures of your language of choice.

How is amazon online assessment evaluated?

Your solutions will be tested against open and hidden test cases and the results will be used to 
decide whether you move to the next round of interview.

How hard is amazon online assessment?

It depends on your luck. It could range from leetcode easy to hard. But most of the questions are not
too difficult. See the list above to get a sense of difficulty and practice the corresponding patterns.

How to prepare for amazon online test?

Use the list above and AlgoMonster's Amazon patterns to prepare.
What happens after amazon online assessment?

You will hear back from the recruiter in a few days. If you are looking for an intern role, you will 
be given multiple OAs and then the "virtual onsite" interview (commonly referred to as the VO). 
If you are an experienced engineer, you will go onto the (possible virtual) onsite interview directly.


"""