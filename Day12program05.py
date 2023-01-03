class Student:
    college='MTCA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print("Name :"+self.name.title()+'\nRoll.no : '\
              +str(self.rollno))
        print('college : '+self.college+'\nCourse : '+self.course)

for i in range(2):
    n=input()
    r=int(input())
    obj=Student(n,r)
    obj.displayStudent()
