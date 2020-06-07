def multiples(m, count):
    for i in range(0,count*m,m):
        print(i)

def mul_table(n,i=1):
    print(n*i)
    if i !=10:
        mul_table(n,i+1)


def multi(m):
    my_list =[]
    for i in range(1,m):
        if m%i ==0:
            my_list.append(i)
    return my_list

print(multi(30))
