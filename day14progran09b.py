class Empolyee:
     empCount = 0
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Empolyee.empCount += 1
     def displayCount(self):
         print("Total Empolyee %d" % Empolyee.empCount)
     def displayEmpolyee(self):
         print("Name :",self.name, ",salary:",self.salary)
emp1=Empolyee("Bareera",9999)
emp1.displayEmpolyee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1, 'salary',7000)
print("Modified salary",getattr(emp1, 'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("Added Attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
