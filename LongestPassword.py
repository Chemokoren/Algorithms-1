# Tasks Details
# Easy
# 1. LongestPassword
# Given a string containing words, find the longest word that satisfies specific conditions.
# Task Score
# 100%
# Correctness
# 100%
# Performance
# Not assessed
# Task description
# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
#
# it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
# there should be an even number of letters;
# there should be an odd number of digits.
# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.
#
# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).
#
# Write a function:
#
# class Solution { public int solution(String S); }
#
# that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.
#
# For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.
#
# Assume that:
#
# N is an integer within the range [1..200];
# string S consists only of printable ASCII characters and spaces.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

def solution(S):
    longest = -1
    num_of_letters = 0
    num_of_digits = 0
    num_of_others = 0
    for letter in S:
        if letter.isalpha():
            num_of_letters += 1
        elif letter.isdigit():
            num_of_digits += 1
        elif letter == " ":
            # Check whether it's a valid password.
            if num_of_others == 0 and \
               num_of_letters % 2 == 0 and \
               num_of_digits % 2 == 1:
                if longest < num_of_letters + num_of_digits:
                    longest = num_of_letters + num_of_digits
            # Reset the counters for the next word.
            num_of_letters = 0
            num_of_digits = 0
            num_of_others = 0
        else:
            num_of_others += 1
    # Check whether the last word is a valid password.
    if num_of_others == 0 and \
       num_of_letters % 2 == 0 and \
       num_of_digits % 2 == 1:
        if longest < num_of_letters + num_of_digits:
            longest = num_of_letters + num_of_digits
    return longest


def solution1(S):
    return max([len(str) for str in S.split() if len(str) & 1 and str.isalnum() and sum(c.isdigit() for c in str) & 1] + [-1])

print(solution('test 5 a0A pass007 ?xy1'))