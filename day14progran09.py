class Empolyee:
     empCount = 0
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Empolyee.empCount += 1
     def displayCount(self):
         print("Total Empolyee :",Empolyee.empCount)
     def displayEmpolyee(self):
         print("Name :",self.name,",salary:",self.salary)
emp1=Empolyee("Bareera",55000)
print("Total Empolyee ",Empolyee.empCount)
emp2=Empolyee("Supriya",54000)
emp1.displayEmpolyee()
emp2.displayEmpolyee()
print("Total Empolyee{0}".format(Empolyee.empCount))
emp3=Empolyee("Anusha Royal",55500)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
print("Total Empolyee{0}".format(Empolyee.empCount))
