class Solution:

    def word_convert(self, word1 : str, word2:str) -> int:

        def dfs(i, j, count):
            # base case 1
            if word2 =="":
                return len(word1)
            # base case 2
            if word1 =="":
                return len(word2)

            # ensure that the count parameter is always increasing
            if count > len(word1) + len(word2):
                return count


            if (i<= len(word1)-1 and j <= len(word2)-1):
                if (word1[i] == word2[j]):
                    dfs(i + 1, j + 1,  count)

            # I need to make three decisions: replace, delete, and Insert
            replace_operation=dfs(i+1, j+1, count+1)
            delete_operation=dfs(i+1, j,  count+1)
            insert_operation=dfs(i, j +1, count+1)
            count = min(replace_operation, delete_operation, insert_operation)
            return count
        return dfs(0, 0, count=0)
    
    def word_convert_2(self, word1 : str, word2:str) -> int:
        def dfs(i, j, count):
            # base case 1: word 2 is empty
            if word2 == "":
                return len(word1)

            # base case 2: word 1 is empty
            if word1 == "":
                return len(word2)
            
            if word1 =="" and word2=="":
                return 0

            # recursive case
            if (i <= len(word1) - 1 and j <= len(word2) - 1):
                if (word1[i] == word2[j]):
                    count = dfs(i + 1, j + 1, count)

                # replace
                replace_operation = dfs(i + 1, j + 1, count + 1)

                # delete
                delete_operation = dfs(i + 1, j, count + 1)

                # insert
                insert_operation = dfs(i, j + 1, count + 1)

                count = min(count, replace_operation, delete_operation, insert_operation)

            return count
        return dfs(0, 0, count=0)
    
    # def convert_word_3(self, word1, word2):
    #     ROW, COL = len(word1), len(word2)

    #     dp =[[0]  * (ROW +1) for i in range(COL +1)]
    #     for i in range(ROW-1, -1, -1):
    #         for j in range(COL-1, -1, -1):
    #             if word1[i] == word2[j]:
    #                 dp[i][j] = dp[i+1][j+1]
    #             else:
    #                 dp[i][j] =min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
    #                 # dp[i][j] = min(dp[min(i+1, ROW-1)][min(j+1, COL-1)], dp[min(i+1, ROW-1)][j], dp[i][min(j+1, COL-1)])
    #         print(dp[i])
        # return dp[0][0]
    def convert_word_3(self, word1, word2):
        ROW, COL = len(word1), len(word2)

        # Create a 2D list to store the dynamic programming table
        dp = [[0] * (COL + 1) for i in range(ROW + 1)]
        # Populate the dynamic programming table
        for i in range(ROW - 1, -1, -1):
            dp[i][COL] = 1 + dp[i+1][COL]
            
            for j in range(COL - 1, -1, -1):
                dp[ROW][j] = 1 + dp[ROW][j+1]
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # Choose the minimum value among three possibilities
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        for i in range(ROW+1):
            print(dp[i])
        # Return the result stored in the top-left cell of the table
        return dp[0][0]
    
    def convert_word_4(self, word1: str, word2:str)->int:

        cache =[[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

        return cache[0][0]



        
sol = Solution()
print(sol.word_convert_2("horse", "ros"))
print("----")
print(sol.convert_word_3("abd", "acd"))
print("----")
print(sol.convert_word_3("horse", "ros"))

