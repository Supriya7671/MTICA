student=[[60,'supriya',77,85],[7,'bareera',80,82],
         [3,'anu',80,86],[41,'nithya',82,92]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
