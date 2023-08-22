# def inf_string(a, b):
#     y = a in b
#     return y
#
#
# print(inf_string("coming", "I am coming home"))


# def inf_string(a, b):
#     # return 1 if the string a can be found in b.
#     if a in b:
#         return 1
#     else:
#         return 0
#
#
# print(inf_string("Iam", "I am coming home"))
#
# if __name__ == '__main__':
#     t = int(input())
#     while t > 0:
#         string_first, string_second = input().split()
#         ans = inf_string(string_first, string_second)
#         if ans == 1:
#             print("YES")
#         else:
#             print("NO")
#         t -= 1
#


# Quiz
# Description
# Problem Statement
# In this problem you will be given a string S , consisting of lowercase alphabets (a-z), in which each character is unique. Another string INF is formed by repeating the string S infinitely many times.
#
# Example: If S = “abcde” then the string INF is …abcdeabcdeabcde… Here the dots (’.’) indicate that there are infinitely many characters before and after the string.
#
# Now you will be given another string A and asked to find whether there is any sub-string in INF which is identical to A.
#
# Input Format
# The first line contains the number of test-cases T.
# The next T lines will contain a space-separated string, made up of two parameters:
# The first parameter will be infStr, representing S from the above example
# The second parameter will be toFind, representing A from the above example.
# Output Format
# The function should print YES if A can be found in S, otherwise it should print NO.
# e.g., If the second line of input contains:
#
# abcd abce
# The function should print NO, because, if we repeat “abcd” infinitely many times we will get, “…abcdabcdabcdabcd…” . We will never get an “e”.
# Evaluation Parameters
# Sample Input
# ghijk ghijkghi
# Sample Output
# YES
# Explanation
# The infinite string of 'ghijk' contains 'ghijkghi' as it's sub-string, hence you print YES.
#
#
# Execution time limit
# Default.


def who_do_you_know():
    people = input("Enter the names of people you know, seperated by commas:")
    # people_list = people.split(",")

    # people_without_spaces = []
    # for person in people_list:
    #     people_without_spaces.append(person.strip())


    # return [ person.strip() for person in people_list]
    people_without_spaces =[person.strip() for person in people.split(",")]
    return people_without_spaces

print(who_do_you_know())