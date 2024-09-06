# for addition
def addition(x,y):
    return (x+y)

# for subtraction
def subtraction(x,y):
    return(x-y)

# for multiplication
def multiplication(x,y):
    return(x*y)

#for division
def division(x,y):
    return(x/y)

#for reminder
def reminder(x,y):
    return(x%y)

#for square
def square(x):
    return(x**2)

#for cube
def cube(x):
    return (x**3)

def fname(name1):
    def mname(name2):
        def lname(name3):
            return name1+name2+name3
        return lname
    return mname