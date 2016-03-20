def add(a,b):
    print "ADDING %d + %d " %(a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a,b)
    return a - b

def multiply (a, b):
    print "MULTIPLY %d * %d" %(a,b)
    return a * b

def divide (a,b):
    print "Dividing %d / %d" %(a,b)
    return a / b

print "Let's do some Math with the functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100,2)

print "Age: %d \n Height: %d \n Weight: %d \n IQ: %d"%(age, height,weight,iq)

#puzzle for the extra credit, type it anyway
print "Here is a puzzle"

what = add(age, subtract(height,multiply(weight, divide(iq,2))))

print "That becomes: ",what,"\nCan you do it by hand?"
