
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









