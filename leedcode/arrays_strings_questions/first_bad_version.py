"""
The isBadVersion API is already defined for you.
@param version, an integer
@return a bool
def isBadVersion(version):
"""

def isBadVersion(version):
    if version == 5:
        return True
    else:
        return False

class Solution:

    def firstBadVersion(self,n):
        left = 1
        right = n

        while(left < right ):
            mid = left+(right-left)//2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left


