fo1=open(r"D:\pythonpractice60\Day10\abc.txt","r")
fo2=open(r"D:\pythonpractice60\Day10\abc1.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File copied")
