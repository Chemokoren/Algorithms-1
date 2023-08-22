"""
(OA) 2021 | University Career Fair

You are an event organizer at a university, and n companies would like to do a presentation about 
their company at your university on Career Day. However, each company have a tight schedule as to 
when they can come and present and how long they will present. For the ith company, starting from 0,
they can present starting from minute starts[i] and they can present for durations[i] minutes. 
To give every student a chance to listen to every presentation, the University can allow only one 
company to present at a time. You would like to host as many presentations as possible, so given each
company's schedule, find the maximum number of presentations that the university can hold.

Parameters

    starts: A list of integers with size n representing each company's starting time.
    durations: A list of integers with size n representing the duration of the presentation for each 
    company.

Result

    The maximum number of presentations that the university can hold.

Examples
Example 1:

Input:

starts = [1, 3, 3, 5, 7]

durations = [2, 2, 1, 2, 1]

Output: 4

Explanation: Company 0 will present from minute 1~3, either company 1 present from minute 3~5 or 
company 2 present from minute 3~4. Then. company 3 and 4 can present without conflict. 
Therefore, a total of 4 companies can present.

Restrictions

    1 <= n <= 50
    1 <= starts[i] <= 1000
    1 <= durations[i] <= 1000

"""
from typing import List

def max_presentations(starts: List[int], durations: List[int]) -> int:
    return 0

if __name__ == '__main__':
    starts = [int(x) for x in input().split()]
    durations = [int(x) for x in input().split()]
    res = max_presentations(starts, durations)
    print(res)