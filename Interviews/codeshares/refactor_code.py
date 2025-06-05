class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, other):
        if self._euros == other._euros and self._cents == other._cents:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if self._euros > other._euros:
            return True
        else:
            if self._euros == other._euros and self._cents > other._cents:
                return True

        return False

    def __lt__(self, other):
        if self._euros < other._euros:
            return True
        else:
            if self._euros == other._euros and self._cents < other._cents:
                return True

        return False

    def __add__(self, other):
        euros = self._euros + other._euros
        cents = self._cents + other._cents
        if cents >= 100:
            cents -= 100
            euros += 1

        return Money(euros, cents)

    def __sub__(self, other):
        euros = self._euros - other._euros
        cents = self._cents - other._cents
        if cents < 0:
            cents += 100
            euros -= 1

        if euros < 0:
            raise ValueError("Cannot be negative")

        return Money(euros, cents)


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)

    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)

    # e1 = Money(4, 10)
    # e2 = Money(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    # money1 = Money(3, 95)
    # money2 = Money(3, 95)

    # print(money1 > money2)
    # print(money1 < money2)

    # e1 = Money(4, 5)
    # e2 = Money(2, 95)

    # e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)

    # e5 = e2-e1

'''
refactored code

'''

class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents
 
    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"
 
    def __value(self):
        return self._euros * 100 + self._cents
 
    def __set_value(self, cents: int):
        self._euros = cents // 100
        self._cents = cents - self._euros * 100
 
    def __eq__(self, other):
        return self.__value() == other.__value()
 
    def __ne__(self, other):
        return not self.__eq__(other)
 
    def __gt__(self, other):
        return self.__value() > other.__value()
 
    def __lt__(self, other):
        return self.__value() < other.__value()
 
    def __add__(self, other):
        new = Money(0, 0)
        new.__set_value(self.__value() + other.__value())
        return new
 
    def __sub__(self, other):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("Cannot be negative")
 
        new = Money(0, 0)
        new.__set_value(self.__value() - other.__value())
        return new
 
 
if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents
 
    print(e1)
    print(e2)
 
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)
 
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)
 
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
 
    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)
 
    # money1 = Money(3, 95)
    # money2 = Money(3, 95)
 
    # print(money1 > money2)
    # print(money1 < money2)
 
    # e1 = Money(4, 5)
    # e2 = Money(2, 95)
 
    # e3 = e1 + e2
    # e4 = e1 - e2
 
    # print(e3)
    # print(e4)
 
    # e5 = e2-e1
 



"""
Latest Money refactor
"""
class Money:
    def __init__(self, euros: int, cents: int):
        """Initializes the Money object ensuring cents are within valid range."""
        total_cents = euros * 100 + cents
        self._euros, self._cents = divmod(total_cents, 100)

    def __str__(self):
        """Returns the money representation as a string in 'euros.cents eur' format."""
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, other):
        """Checks if two Money objects are equal."""
        return (self._euros, self._cents) == (other._euros, other._cents)

    def __ne__(self, other):
        """Checks if two Money objects are not equal."""
        return not self == other

    def __gt__(self, other):
        """Checks if self is greater than other."""
        return (self._euros, self._cents) > (other._euros, other._cents)

    def __lt__(self, other):
        """Checks if self is less than other."""
        return (self._euros, self._cents) < (other._euros, other._cents)

    def __add__(self, other):
        """Adds two Money objects."""
        return Money(self._euros + other._euros, self._cents + other._cents)

    def __sub__(self, other):
        """Subtracts two Money objects, ensuring the result is non-negative."""
        total_cents = (self._euros * 100 + self._cents) - (other._euros * 100 + other._cents)
        if total_cents < 0:
            raise ValueError("Cannot be negative")
        return Money(0, total_cents)







