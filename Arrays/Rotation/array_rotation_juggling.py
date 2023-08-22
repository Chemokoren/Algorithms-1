def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

# A = array, n= length of array, k= rotation value
def ArrayRotate(A, n, k):
    d=-1
    temp=None
    j=None
    
    for i in range(gcd(n,k)):
        j =i
        temp=A[i]
        while(True):
            d = (j+k)%n
            if(d==i):
                break
            A[j] = A[d]
            j = d
        A[j] =temp
    
def displayArray(A, n):
    for i in range(n):
        print(A[i],end="")
    print(" ")

if __name__=='__main__':
    arr =[1,2,3,4,5,6,7,8,9]
    n =len(arr)
    k=3
    displayArray(arr, n)
    ArrayRotate(arr,n,k)
    displayArray(arr, n)



