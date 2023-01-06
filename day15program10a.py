def outer():
    message='outer function'
    print(message)
    def inner():
       #nonlocalmessages
        print=(message)
    inner()

outer()
    
        
