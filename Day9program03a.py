def printMonth(dn):
    mn=''
    if (dn==1):
          mn= 'january'
    elif (dn==2):
          mn= 'february'
    elif (dn==3):
          mn= 'march'
    elif (dn==4):
          mn= 'april'
    elif (dn==5):
          mn= 'may'
    elif (dn==6):
          mn= 'jun'
    elif (dn==7):
          mn= 'july'
    elif (dn==8):
          mn='auguest'
    elif (dn==9):
          mn='september'
    elif (dn==10):
          mn='october'
    elif (dn==11):
          mn='novamber'
    elif (dn==12):
          mn='december'
    else:
        mn='invalid'
    return mn
def printMonth1(dn):
    mn=''
    if (dn==1):
          mn= 'january'
    if (dn==2):
          mn= 'february'
    if (dn==3):
          mn= 'march'
    if (dn==4):
          mn= 'april'
    if (dn==5):
          mn= 'may'
    if (dn==6):
          mn= 'jun'
    if (dn==7):
          mn= 'july'
    if (dn==8):
          mn='auguest'
    if (dn==9):
          mn='september'
    if (dn==10):
          mn='october'
    if (dn==11):
          mn='novamber'
    if (dn==12):
          mn='december'
    return mn
import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*100000)
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*100000)       
    
    
