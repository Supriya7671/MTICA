'''
File by Supriya
'''
x=5;y=7
#Function definition is here
def Changeme(mylist):
    "This fuction demonstrates local and global variable"
    p=89
    global x,y
    x=y+2
    mylist =[1,2,3,4]
    print("Values inside the function:",mylist)
    print("local variables are:",locals())
    print("global variables are:",globals())
    return
#Now you can changeme function
mylist_var =[10,20,30]
Changeme(mylist_var)
print("Values outside the function:",mylist_var)
