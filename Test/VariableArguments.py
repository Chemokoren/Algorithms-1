# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    sum =0
    count=0
    for arg in argv:
        new_int=int(arg)
        sum=sum+new_int
        count=count+1
    print(sum/count)


myFun('4', '6', '3', '6')
