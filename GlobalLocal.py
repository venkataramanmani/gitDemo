x=123 #Global variable
def display():
    x=600 #Local Variable
    print(x)
    print(globals()['x']) #to access global variable
print(x)
z = display # functions can be assigned to a variable and invoked.
z()
z()
z()
