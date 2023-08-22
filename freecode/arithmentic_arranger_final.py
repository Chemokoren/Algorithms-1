# ### Assignment
#
# Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
# ```
#   235
# +  52
# -----
# ```
#
# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.
#
# ### For example
#
# Function Call:
# ```py
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# ```
#
# Output:
# ```
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
# ```
#
# Function Call:
# ```py
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# ```
#
# Output:
# ```
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# ```
#
# ### Rules
#
# The function will return the correct conversion if the supplied problems are properly formatted, 
# otherwise, it will **return** a **string** that describes an error that is meaningful to the user.
#
#
# * Situations that will return an error:
#   * If there are **too many problems** supplied to the function. The limit is **five**, anything 
#      more will return:
#     `Error: Too many problems.`
#   * The appropriate operators the function will accept are **addition** and **subtraction**. 
#     Multiplication and division will return an error. Other operators not mentioned in this bullet 
#      point will not need to be tested. The error returned will be:
#     `Error: Operator must be '+' or '-'.`
#   * Each number (operand) should only contain digits. Otherwise, the function will return:
#     `Error: Numbers must only contain digits.`
#   * Each operand (aka number on each side of the operator) has a max of four digits in width. 
#      Otherwise, the error string returned will be:
#     `Error: Numbers cannot be more than four digits.`
# *  If the user supplied the correct format of problems, the conversion you return will follow 
#       these rules:
#     * There should be a single space between the operator and the longest of the two operands, 
#       the operator will be on the same line as the second operand, both operands will be in the
#       same order as provided (the first will be the top one and the second will be the bottom.
#     * Numbers should be right-aligned.
#     * There should be four spaces between each problem.
#     * There should be dashes at the bottom of each problem. The dashes should run along the entire
#       length of each problem individually. (The example above shows what this should look like.)



def arithmetic_arranger_final(problems, answers=False):
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    # This is referenced in the loop, but is important to define outside of the loop
    number_of_problems_left = len(problems)
    formatted_problems = []

    # Too many problems requirement
    if len(problems) > 5:
        return "Error: Too many problems."

    # "problems" is a list of strings
    for problem in problems:

        # For each loop iteration of the loop, there's one less problem to check
        number_of_problems_left = number_of_problems_left - 1

        # Break up each problem string
        new_problem = problem.split()
        first_operand = new_problem[0]
        operator = new_problem[1]
        second_operand = new_problem[2]

        # Only digits requirement
        if (first_operand.isdigit() != True) or (second_operand.isdigit() != True):
            return "Error: Numbers must only contain digits."
        # Only 4 digits requirement
        if (len(first_operand) > 4) or (len(second_operand) > 4):
            return "Error: Numbers cannot be more than four digits."

        # Only "+" or "-" requirement
        if (operator != "+") and (operator != "-"):
            return "Error: Operator must be '+' or '-'."

        # Initialize "answer", used directly below
        answer = ""

        # Does the actual arithmetic
        if operator == "+":
            answer = int(first_operand) + int(second_operand)
        else:  # operator must be "-"
            answer = int(first_operand) - int(second_operand)

        # This defines how many dashes there should be at the bottom of each problem
        width_of_problem = max(len(first_operand), len(second_operand)) + 2

        # "rjust" will right-align a string, using a space as the default fill character
        # Formatting of each problem is here

        first_line += str(first_operand.rjust(width_of_problem))
        second_line += str(operator + second_operand.rjust(width_of_problem - 1))
        dash_line += str("-" * width_of_problem)
        answer_line += str(answer).rjust(width_of_problem)

        if number_of_problems_left > 0:
            column_width = "    "
            first_line += column_width
            second_line += column_width
            dash_line += column_width
            answer_line += column_width

        if answers == True:
            formatted_problems = (first_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line)
        else:
            formatted_problems = (first_line + "\n" + second_line + "\n" + dash_line)

    return formatted_problems



print(arithmetic_arranger_final(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# print(arithmetic_arranger_final(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger_final(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# print(arithmetic_arranger_final(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger_final(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger_final(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger_final(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger_final(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))

