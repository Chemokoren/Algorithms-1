class Category:
    def __init__(self, name):
        self.ledger = []
        self.category = name
        # added another variable to get balance easier
        self.balance = 0

    def deposit(self, amount, description=None):
        # if no description is given
        if description == None:
            description = ""

        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        return self.balance

    def transfer(self, amount, Cat):
        if self.withdraw(amount, "Transfer to " + Cat.category):
            Cat.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        # checks whether amount can be withdrawn or not
        if self.balance < amount:
            return False
        return True

    def withdraw(self, amount, description=None):
        if description == None:
            description = ""
        # checks for sufficient funds for withdrawl operation
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # def __str__(self):
    #     # adding * symbols and category name
    #     s = "*" * ((30 - len(self.category)) // 2) + self.category
    #     # adding * symbols for right side
    #     s = s + "*" * (30 - len(s)) + "\n"
    #     for i in self.ledger:
    #         # making description left justified and amount right justified
    #         s += i["description"][:23].ljust(23) + str("{:.2f}".format(i["amount"]).rjust(7)) + "\n"
    #     s += "Total: " + str(self.balance)
    #     return s

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
                     f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output


def round_to_nearest_ten(n):
    if n < 10:
        return 0
    return round(n / 10.0) * 10

def create_spend_chart(categories):
    withdrawls = []

    # used to find the category name with max length
    max_len_category = 0
    s = 0

    for i in categories:

        withdraw_amount = 0

        for j in i.ledger:

            # adding withdrawls to string
            if j["amount"] < 0:
                withdraw_amount += -j["amount"]
                s += (-j["amount"])

        # finding max len category name
        if len(i.category) > max_len_category:
            max_len_category = len(i.category)
        withdrawls.append([i.category, withdraw_amount])

    # used to calculate the percentage of a certain category
    for i in withdrawls:
        i.append(round_to_nearest_ten((i[1] / s) * 100))
    s = ""
    s += "Percentage spent by category\n"
    t = 100
    while t >= 0:

        # prints number and | symbol
        s += str(t).rjust(3) + "|" + " "

        # loop for printing 'o' if the percentage>=t

        for i in range(len(withdrawls)):
            if withdrawls[i][2] >= t:
                s += "o" + "  "
            else:
                s += "   "
        t -= 10
        s += "\n"

    # adding '-' to the last lines
    s += "    " + ("-" * 10) + "\n"

    loop_var = 0

    for i in range(max_len_category):
        s += "     "
        for j in range(len(withdrawls)):
            # checks whether a character exists at a length
            if len(withdrawls[j][0]) - 1 < loop_var:
                # if no character exists adds empty string and 2 spaces
                s += "   "
            else:
                # adds character
                s += withdrawls[j][0][loop_var] + "  "
        loop_var += 1
        if i != max_len_category - 1:
            s += "\n"

    return s



################################# approach 2####################################################
# class Category:
#     def __init__(self, name):
#         self.name = name
#         self.ledger = list()
#
#     def check_funds(self, amount):
#         funds = 0
#         for i in range(len(self.ledger)):
#             funds = funds + self.ledger[i]["amount"]
#         if funds < amount:
#             return False
#         else:
#             return True
#
#     def deposit(self, amount, description=''):
#         self.dep = dict()
#         self.dep["amount"] = amount
#         self.dep["description"] = description
#         self.ledger.append(self.dep)
#
#     def withdraw(self, amount, description=''):
#         self.withd = dict()
#         self.withd["amount"] = amount
#         self.withd["description"] = description
#         if self.check_funds(amount):
#             self.ledger.append(self.withd)
#             return True
#         else:
#             return False
#
#     def get_balance(self):
#         total_dep = 0
#         total_withd = 0
#         for i in range(len(self.ledger)):
#             total_dep += self.ledger[i]["amount"]
#         return total_dep
#
#
#     def transfer(self, amount, another_category):
#         a = self.withdraw(amount, f"Transfer to {another_category.name}")
#         b = another_category.deposit(amount, f"Transfer from {another_category.name}")
#
#     def __str__(self):
#         title = f"{self.name:*^30}\n"
#         items = ""
#         total = 0
#         for i in range(len(self.ledger)):
#             items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
#             total += self.ledger[i]['amount']
#         output = title + items + "Total: " + str(total)
#         return output
#
#     def calculate_total_withdrawals(self):
#         total_withdrawal = 0
#         for i in range(len(self.ledger)):
#             if self.ledger[i]['amount'] < 0:
#                 total_withdrawal += self.ledger[i]['amount']
#         return total_withdrawal
#
#
# def calculate_percentage(sum, number):
#     percentage = round(number/sum * 100, -1)
#     return percentage
#
# def create_spend_chart(categories):
#     title = "Percentage spent by category\n"
#     full_withdrawals = 0
#     percentages = []
#     x_axis = []
#     y_axis = []
#     bar = []
#     for i in categories:
#         full_withdrawals += Category(i).calculate_total_withdrawals()
#     for i in range(len(categories)):
#         percentages.append(calculate_percentage(full_withdrawals, Category(categories[i]).calculate_total_withdrawals()))
#     for i in range(10):
#         y_axis.append(str(int(i) * 10) + '|')
#         for per in percentages:
#             if per == i:
#                 bar[percentages.index(per)] += 'o '
#             else:
#                 bar[percentages.index(per)] += '  '