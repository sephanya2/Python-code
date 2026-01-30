#use of local, global and nonlocal variables

x = 10        
def outer():
    y = 20   

    def inner():
        nonlocal y
        global x

        z = 30  

        y = y + 5
        x = x + 5

        print("Local variable z =", z)
        print("Nonlocal variable y =", y)
        print("Global variable x =", x)

    inner()

outer()
