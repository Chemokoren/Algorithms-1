import time

class countDown:
    def my_count_down(n):
        if n < 0:
            return
        print(n)
        time.sleep(1)
        my_count_down(n - 1)


countD = countDown
countD.my_count_down(5)
# my_count_down(5)
