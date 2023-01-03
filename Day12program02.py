def printSeries(n):
    #sp='.'
    for i in range(1,n+1):
        num=1
        print()
    for j in range(i):
        print(num,end='')
        num+=1
        #print(sp*(n-i-1)+ Ch*(2*i+1)+sp*(n-i-1))
    return None
#inpCh=input()
inpNum=int(input())
printSeries(inpNum)
##try:
##   printSeries(inpCh,inpNum)
##except AssertionError as ob:
##  print(ob)
