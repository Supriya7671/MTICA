class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        assert(self.num2!=0),"number is  divisible by 0"
        return self.num1/self.num2
n1=int(input())
n2=int(input())
Ob=Number(n1,n2)
try:
    print(n1,'/',n2,'=',Ob.div(),sep='')
except ZeroDivisionError as ob:
    print(ob)
print(n1,'+',n2,'=',Ob.add(),sep=' ')
print(n1,'-',n2,'=',Ob.sub(),sep=' ')
print(n1,'*',n2,'=',Ob.mul(),sep=' ')
    
