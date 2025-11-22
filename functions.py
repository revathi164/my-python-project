def addition(a , b):
    return a + b

print("addition = ",addition(3,5))


def add(a,/,b):
    return a+b

print("add = ", add(3, b=7))


def sub(*,a,b):
    return a-b

print("sub = ",sub(b=2,a=5))

def sub(a,b):
    return a-b

print("sub = ", sub(a=2,b=3))

def mul(*,a=1,b=3,c=7):
    return a*b*c

print("mul = ",mul(a = 8))

def mul(a=2,*,b):
    print("mul =",a*b)

mul(a = 0, b = 5)

def table(number):
    for i in range(1,11):
        print(number,"*",i,"=",number*i)

table(2)

def average(a,b,c):
    return (a+b+c)/3

result = average(89,80,90)
print("average = ", result)





