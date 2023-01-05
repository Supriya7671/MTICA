class Empolyee:
     empCount = 0
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Empolyee.empCount += 1
     def displayCount(self):
         print("Total Empolyee {0}".format (Empolyee.empCount))
     def displayEmpolyee(self):
         print("Name :",self.name, ",salary:",
               self.salary)
emp1=Empolyee("Bareera",9999)
emp1.displayEmpolyee()
emp1.salary=17000
emp1.experience=3
emp1.displayEmpolyee()
emp1.name='Manoj'
emp1.displayEmpolyee()
print(emp1.experience)
#del emp1.salary
emp1.displayEmpolyee()
