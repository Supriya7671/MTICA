fo=open(r"D:\pythonpractice60\Day10\abc.txt","w+")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Write to file")
