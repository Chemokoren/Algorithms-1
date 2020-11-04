def arithmetic_arranger(problems):

    final_val =""
    for i in range(len(problems)-1):
        arranged_problems =problems[i].split()
        firstVal =arranged_problems[0]
        secondVal=arranged_problems[1]
        thirdVal =arranged_problems[2]
        final_val +=firstVal.rjust(5,' ') +'\n'+secondVal+ thirdVal.rjust(4,' ')+'\n'+"-----".rjust(5,' ')+'\n\n'


    return final_val


def arithmetic_arranger1(problems,answer=False):
  count=len(problems)
  elements=list()
  leftoperand=list()
  operator=list()
  rightoperand=list()
  lenleftoperand=list()
  lenrightoperand=list()
  out=list()
  results=list()
  resultslen=list()
  if count>5:
    prob="Error: Too many problems."
    print(prob)
    return prob
  else:
    for x in problems:
        endl=x.find(" ")
        lno=x[0:endl]
        lenlno=len(lno)

        if lenlno>4:
            probl="Error: Numbers cannot be more than four digits."
            print(probl)
            return probl
        else:
            lenleftoperand.append(lenlno)
        rno=x[endl+3:]
        lenrno=len(rno)
        if lenrno>4:

            probl="Error: Numbers cannot be more than four digits."
            print(probl)
            return probl
        else:
            lenrightoperand.append(lenrno)
        op=x[endl+1]

        if op!="+"and op!="-":
            probo="Error: Operator must be '+' or '-'."
            print(probo)
            return probo

        try:
            leftoperand.append(int(lno))
            operator.append(x[endl+1])
            rightoperand.append(int(rno))
        except:
            prob1="Error: Numbers must only contain digits."
            print(prob1)
            return prob1
    if answer==True:
        l=0
        i=0
        while l < count:
            maximum=max(lenleftoperand[i],lenrightoperand[i])
            i=i+1
            out.append(maximum+2)
            l=l+1
        p=0
        r=0
        while p < count:
            miss=out[r]-lenleftoperand[r]
            for k in range(miss):
                print(" ",end="")
            print(leftoperand[r],end="")
            print("    ",end="")
            r=r+1
            p=p+1
        print("",end="\n")
        q=0
        w=0
        while q < count:
            miss=out[w]-lenrightoperand[w]-1
            print(operator[w],end="")
            for k in range(miss):
                print(" ",end="")
            print(rightoperand[w],end="")
            print("    ",end="")
            w=w+1
            q=q+1
        print("",end="\n")
        g=0
        h=0
        while g < count:
            for k in range(out[h]):
                print("-",end="")
            print("    ",end="")
            g=g+1
            h=h+1
        print("",end="\n")
        l=0
        i=0
        while l < count:
            if operator[i]=='+':
                sum1=leftoperand[i]+rightoperand[i]

                results.append(sum1)
            else:
                if leftoperand>rightoperand:
                    diff=leftoperand[i]-rightoperand[i]
                    results.append(diff)
                else:
                    diff=leftoperand[i]-rightoperand[i]
                    sdiff=str(diff)
                    mdiff="-"+ sdiff


                    results.append(sdiff)

            l=l+1
            i=i+1
        for x in results:
            size=str(x)
            z=len(size)
            resultslen.append(z)
        a=0
        w=0
        while a < count:
            miss=out[w]-resultslen[w]

            for k in range(miss):
                print(" ",end="")
            print(results[w],end="")
            print("    ",end="")
            w=w+1
            a=a+1
        print("",end="\n")
    else:
        l=0
        i=0
        while l < count:
            maximum=max(lenleftoperand[i],lenrightoperand[i])
            i=i+1
            out.append(maximum+2)
            l=l+1
        p=0
        r=0
        while p < count:
            miss=out[r]-lenleftoperand[r]
            for k in range(miss):
                print(" ",end="")
            print(leftoperand[r],end="")
            r=r+1
            p=p+1
            if p==count:
                break
            print("    ",end="")
        print("")
        q=0
        w=0
        while q < count:
            miss=out[w]-lenrightoperand[w]-1
            print(operator[w],end="")
            for k in range(miss):
                print(" ",end="")
            print(rightoperand[w],end="")

            w=w+1
            q=q+1
            if q==count:
                break
            print("    ",end="")
        print("")
        g=0
        h=0
        while g < count:
            for k in range(out[h]):
                print("-",end="")
            g=g+1
            h=h+1
            if g==count:
                break
            print("    ",end="")
        print("")
problems =["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(arithmetic_arranger1(problems))