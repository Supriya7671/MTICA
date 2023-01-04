def printBlue():
    print('you chose blue!\n')
    return
def printRed():
    print('you chose red!\n')
    return
def printOrange():
    print('you chose orange!\n')
    return
def printYellow():
    print('you chose yellow!\n')
    return
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orenge")
    print("3:Yellow")
    print("4:Quit")
    return
ColorSelect={0:printBlue,1:printRed,2:printOrange,3:printYellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("select a color option:"))
    if(selection>=0)and(selection<4):
        ColorSelect[selection]()
