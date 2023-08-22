"""
 (OA) 2021 | Efficient Job Processing Service

In order to maximize the profit and minimize the cost, the HR has decided to create a program to filter
through the candidates and find suitable people to work for the company.

There are a total of n candidates, and the super advanced AI for the company has determined that for 
the ith candidate (starting from 0), the expected salary of that candidate is s[i] per month and the 
amount of work that candidate can do is w[i]. However, each candidate needs to be paid bonuses, health 
insurances, and other miscellaneous costs, so the monthly cost of each candidate is going to be double 
their expected salary.

The company has a monthly budget of b to spend on the new employees, and it's unlikely that they will 
be able to hire all the candidates. They want to maximize the amount of work done while making sure 
the amount of money spent on the new employees don't exceed their monthly budget.

That is where you come in. You need to write a function that takes each candidate's expected salary, 
the amount of work they can do, and the company's monthly budget, and calculate the most work the new 
employees can do (assuming the total work done is equal to the sum of the work done by each employee).

Parameters

    s: A list of integers representing the expected monthly salary of each candidate.
    w: A list of integers representing how much work that candidate can do if the company hires them.
    b: An integer representing the company's monthly budget.

Result

    An integer representing the maximum work done by the employees while not exceeding the company's 
    budget.

Examples
Example 1:

Input: s = [2, 2, 3, 4], w = [2, 4, 4, 5], b = 15

Output: 10

Explanation: The monthly cost on each candidate is double their expected salary, so [4, 4, 6, 8]. 
Hiring candidate 0, 1, 2, the total cost is equal to 4 + 4 + 6 = 14 <= 15 while the total work done is 
2 + 4 + 4 = 10, which is the maximum.

Restrictions

    1 <= n <= 1000
    1 <= s[i] <= 10^6 for each 0 <= i < n
    1 <= w[i] <= 100 for each 0 <= i < n
    1 <= b <= 1000

"""

from typing import List

def process_candidates(s: List[int], w: List[int], b: int) -> int:
    return 0

if __name__ == '__main__':
    s = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    b = int(input())
    res = process_candidates(s, w, b)
    print(res)