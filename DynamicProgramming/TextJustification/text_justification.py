"""
The problem “Text Justification” states that you are given a list s[ ] of type string 
of size n and an integer size.
Justify the text such that each line of text consists of size number of characters. 
You can use space(‘ ‘) as a character to complete the required number of characters 
in a line.

Input

s = {"TutorialCup", "is", "the", "best", "portal", "for", "programming."}
size = 12

TutorialCup
is  the best
portal   for
programming.

Explanation: As we can use spaces between the words, we have placed them properly as can 
be seen in the image embedded above.


s = {"This", "article", "is", "contributed", "by", "Akshita", "Jain"}
size = 13

This  article
is
contributed
by    Akshita
Jain


Algorithm for Text Justification LeetCode Solution

- Initialize a list s[ ] of type string of size n and an integer variable size.
- Traverse through the list and check for each word/string if the length of the current
  word is less than or equal to the given size, add the current word to the result.
- Else if the length of the current string/word is greater than the given size, use the 
  white spaces to complete the remaining positions of the line.
- If the sum of the length of the next word in the same line and the length of the 
  previous word in the same line is less than or equal to the given size, add the current 
  word to the result and adjust the remaining places with the white space.
- Else if the sum of the length of the next word in the same line and the length of the 
  previous word in the same line is greater than the given size, add the current word in 
  the next line of the result and fill the remaining places of current line with the 
  white space.
- Print the resulting string.

Complexity Analysis
Time Complexity

O(n) where n is size of the given string array s[ ]. We are running a while loop inside 
fullJustify which runs only until either of the i and j variable do not cross N. 
And this loop takes linear time to end. Thus time complexity is linear.

Space Complexity

O(n) because we used space to store n string.

"""
def justify_text(words, max_width):
    if not words:
        return ""
    if len(words) == 1:
        return words[0].ljust(max_width)

    current_word = words[0]
    remaining_words = words[1:]
    spaces_left = max_width - len(current_word)

    for i, word in enumerate(remaining_words):
        if len(current_word) + len(word) + 1 <= max_width:
            current_word += " " + word
            spaces_left -= 1
            remaining_words = remaining_words[i+1:]
            break

    num_spaces = spaces_left // (len(current_word.split()) - 1)
    extra_spaces = spaces_left % (len(current_word.split()) - 1)

    justified_text = ""
    for word in current_word.split():
        justified_text += word + " " * num_spaces
        if extra_spaces > 0:
            justified_text += " "
            extra_spaces -= 1

    return justified_text + justify_text(remaining_words, max_width)

# words = ["This", "is", "an", "example", "of", "text", "justification."]
# max_width = 16
# justified_text = justify_text(words, max_width)
# print(justified_text)

# words = ["TutorialCup", "is", "the", "best", "portal", "for", "programming."]
# max_width = 12
# justified_text = justify_text(words, max_width)
# print(justified_text)


# def justify_text(words, max_width):
#     if not words:
#         return ""
#     if len(words) == 1:
#         return words[0].ljust(max_width)

#     current_word = words[0]
#     remaining_words = words[1:]
#     spaces_left = max_width - len(current_word)

#     for i, word in enumerate(remaining_words):
#         if len(current_word) + len(word) + 1 <= max_width:
#             current_word += " " + word
#             spaces_left -= 1
#             remaining_words = remaining_words[i+1:]
#             break

#     num_spaces = spaces_left // (len(current_word.split()) - 1)
#     extra_spaces = spaces_left % (len(current_word.split()) - 1)

#     justified_text = ""
#     for word in current_word.split():
#         justified_text += word + " " * num_spaces
#         if extra_spaces > 0:
#             justified_text += " "
#             extra_spaces -= 1

#     return justified_text + "\n" + justify_text(remaining_words, max_width)


def justify_text(words, max_width):
    if not words:
        return ""
    if len(words) == 1:
        return words[0].ljust(max_width)

    current_word = words[0]
    remaining_words = words[1:]
    spaces_left = max_width - len(current_word)

    for i, word in enumerate(remaining_words):
        if len(current_word) + len(word) + 1 <= max_width:
            current_word += " " + word
            spaces_left -= 1
            remaining_words = remaining_words[i+1:]
            break

    if len(current_word.split()) > 1:
        num_spaces = spaces_left // (len(current_word.split()) - 1)
        extra_spaces = spaces_left % (len(current_word.split()) - 1)
    else:
        num_spaces = spaces_left
        extra_spaces = 0

    justified_text = ""
    for word in current_word.split():
        justified_text += word + " " * num_spaces
        if extra_spaces > 0:
            justified_text += " "
            extra_spaces -= 1

    return justified_text + "\n" + justify_text(remaining_words, max_width)


s = ["TutorialCup", "is", "the", "best", "portal", "for", "programming."]
size = 12
justified_text = justify_text(s, size)
print(justified_text)