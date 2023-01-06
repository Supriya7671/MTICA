def outer():
    print('outer function')
    
    def inner():
       #nonlocalmessages
        print=('inner function')
    inner()

outer()
    
        
