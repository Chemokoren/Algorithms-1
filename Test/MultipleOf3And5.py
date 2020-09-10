def fizzBuzz(n):
    def isMultipleof5(n):
        while (n > 0):
            n = n - 5
            if (n == 0):
                return 1
        return 0

    def isMultipleOf3(n):
        odd_count = 0
        even_count = 0
        if (n < 0):
            n = -n
        if (n == 0):
            return 1
        if (n == 1):
            return 0

        while (n):
            if (n & 1):
                odd_count += 1
            if (n & 2):
                even_count += 1
            n = n >> 2

        return isMultipleOf3(abs(odd_count - even_count))

    for i in range(1, n+1):
        if (isMultipleOf3(i) == 1 and isMultipleof5(i) == 1):
            print('FizzBuzz')
        if (isMultipleOf3(i) == 1 and isMultipleof5(i) == 0):
            print('Fizz')
        if (isMultipleOf3(i) == 0 and isMultipleof5(i) == 1):
            print('Buzz')
        if (isMultipleOf3(i) == 0 and isMultipleof5(i) == 0):
            print(i)

print(fizzBuzz(3))

# if __name__ == '__main__':