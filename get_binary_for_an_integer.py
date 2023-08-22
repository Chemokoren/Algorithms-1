def get_binary(n):
    x =""
    while(n>0):
        if n%2 == 1:
            x += '1'
        if n%2 == 0:
            x += '0'
        n = n//2
        get_binary(n)
    return x;


def get_binary_gap():
    text =get_binary(529)[::-1]
    # print(text)

    # Iterate over the string
    for element in text:
        if(element == 1):
            first_count=1;
        print(element, end=' ')
    print("\n")
# get_binary_gap();


def solution1(N):
     bin_rep = str(bin(N))[2:]
     bin_gap = False
     bin_max = 0
     bin_counter = 0
     for symbol in bin_rep:
         if symbol == '1':
             if bin_max < bin_counter:
                 bin_max = bin_counter
             bin_gap = True
             bin_counter = 0
         elif bin_gap:
             bin_counter += 1
     return bin_max


def solution2(N):
  return len(max(bin(N)[2:].strip('0').strip('1').split('1')))

#strip(str) and split(str) functions can be used for the string manipulation.
"""
#Big-O Calculation
"""

def solution(N):
     bin_rep = str(bin(N))[2:]   # Constant 1
     bin_gap = False
     bin_max = 0
     bin_counter = 0
     for symbol in bin_rep:      # Constant N
         if symbol == '1':
             if bin_max < bin_counter:
                 bin_max = bin_counter
             bin_gap = True
             bin_counter = 0
         elif bin_gap:
             bin_counter += 1
     return bin_max
## O(N)
print(solution(1041))

