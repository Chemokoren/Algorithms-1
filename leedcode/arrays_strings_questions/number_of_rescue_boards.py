"""
"""

class Solution:
    def numRescueBoats(self, people: int, limit:int)->bool:
        people.sort()

        left = 0
        right = len(people) -1

        boats_number = 0

        while(left <= right):
            if(left == right):
                boats_number += 1
                break
            if(people[left]+people[right] <= limit):
                left += 1

            right -= 1
            boats_number +=1
        return boats_number

# my_people=[1,2]
my_people=[3,2,2,1]
my_limit=3
sol = Solution()
print(sol.numRescueBoats(my_people,my_limit))