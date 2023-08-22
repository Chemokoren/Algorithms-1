class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    # categories = food, clothing, and entertainment.

    def deposit(self,amount, description=""):
        self.dep =dict()
        #add amount and description
        self.dep["amount"] = amount
        self.dep["description"] =description
        self.ledger.append(self.dep)
        return ledger

    
    def withdraw(self, amount, description=""):
        # check if total amount is less than or greater than the amount to be withdrawn
        _result = self.check_funds(amount)
        if(_result ==True):
            self.withd=dict()
            self.withd["amount"] =-(amount)
            self.withd["description"]=description
            self.ledger.append(self.withd)
            return True

        else:
            return false


    def get_balance(self, balance):
        fund =0
        n =len(food.ledger)

        #get total fund from ledger
        for i in range(n):
            fund = fund+food.ledger[i]["amount"]
        return fund


    def transfer(self,amount, budget_category):
        budgetCategory =budget_category.name
        a =self.withdraw(amount, f"Transfer to{budgetCategory}")
        b =budget_category.deposit(amount,f"Transfer from {self.name}")
        if(a == True):
            return True
        else:
            return False


    def check_funds(self, amount):
        fund =0
        n =len(self.ledger)
        for i in range(n):
            fund =fund + self.ledger[i]["amount"]
        if fund > amount:
            return False
        else:
            return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output

    def create_spend_chart(categories):
        res = "Percentage spent by category\n"
        i = 100
        totals = getTotals(categories)
        while i >= 0:
            cat_spaces = " "
            for total in totals:
                if total * 100 >= i:
                    cat_spaces += "o  "
                    # print(categories[totals.index(total)].name)
                else:
                    cat_spaces += "   "
            res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
            i -= 10

        dashes = "-" + "---" * len(categories)
        names = []
        x_axis = ""
        for category in categories:
            names.append(category.name)

        maxi = max(names, key=len)

        for x in range(len(maxi)):
            nameStr = '     '
            for name in names:
                if x >= len(name):
                    nameStr += "   "
                else:
                    nameStr += name[x] + "  "
            nameStr += '\n'
            x_axis += nameStr

        res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
        return res


