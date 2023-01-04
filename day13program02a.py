def printSunday():
    print("Sunday")
def printMonday():
    print("Monday")
def printTuesday():
    print("Tuesday")
def printWednesday():
    print("Wednesday")
def printThursday():
    print("Thursday")
def printFriday():
    print("Friday")
def printSaturday():
    print("Saturday")
def choice():
    print("Enter a  day number 1-7")
    return
DayDict={0:printSunday,1:printMonday,2:printTuesday,3:printWednesday,4:printThursady,5:printFriday,6:printSaturday}
choice()
dayNo=int(input())
if dayNo>=1 and DayNo<=7:
    dayDict[dayNo]()
else:
    print('INVALID')
