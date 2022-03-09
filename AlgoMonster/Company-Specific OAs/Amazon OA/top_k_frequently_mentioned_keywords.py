"""

(OA) 2021 - Top K Frequently Mentioned Keywords | SHL

Practice on leetcode here: https://leetcode.com/problems/top-k-frequent-words/

"""

from heapq import heappop, heappush
import re
from typing import Counter, List

class Down:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

def top_mentioned(k: int, keywords: List[str], reviews: List[str]) -> List[str]:
    patt = re.compile(r'\b(:?{})\b'.format('|'.join(keywords)), flags=re.IGNORECASE)
    counts = Counter(
        word
        for review in reviews
        for word in set(match[0].lower() for match in patt.finditer(review))
    )
    queue =[]
    for word, count in counts.items():
        heappush(queue, (count, Down(word)))
        if len(queue) > k:
            heappop(queue)
    res =[]
    while len(queue) > 0:
        res.append(heappop(queue)[1].value)
    return res[::-1]

if __name__ =='__main__':
    k = int(input())
    keywords =[input() for _ in range(int(input()))]
    reviews =[input() for _ in range(int(input()))]
    res = top_mentioned(k, keywords, reviews)
    print(' '.join(res))

    
