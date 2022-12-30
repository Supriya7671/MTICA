def printMonth(dn):
    if (dn==1):
          return 'january'
    if (dn==2):
          return 'february'
    if (dn==3):
          return 'march'
    if (dn==4):
          return 'april'
    if (dn==5):
          return 'may'
    if (dn==6):
          return 'jun'
    if (dn==7):
          return 'july'
    else:
          return'invalid'
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
           
    
    
