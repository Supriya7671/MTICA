class Rectangle:
    def __init__(self,width,length):
        assert(length>=0 and width>=0),'Invalid'
        self.length=length
        self.width=width
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp

    
l=int(input())
w=int(input())
try:
    obj=Rectangle(l,w)
    area=obj.calculateArea()
    peri=obj.calculatePerimeter()
    print('Area of rectangle is',area)
    print('perimeter of rectangle is',peri)
except AssertionError as obj:
    print(obj)
