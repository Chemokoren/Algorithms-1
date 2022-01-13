from typing import List
"""
Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses that can be 
obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, 
seperated by single dots and cannot have leading zeros. For example, "0.1.2.201" and 
"192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1"
are invalid IP addresses.

Example 1:

Input: s ="25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s ="0000"
Output: ["0.0.0.0"]

"""
class Solution:

    def restoreIPAddresses(self, s:str)->List[str]:
        # 256 choices for each of the 4 spots BUT ...
        # The order of s stays same, 
        # We just place the "." in between

        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j+1, dots +1, curIP + s[i:j+1]+".")

        backtrack(0, 0, "")
        return res

str ="25525511135"
sol = Solution()
print(sol.restoreIPAddresses(str))