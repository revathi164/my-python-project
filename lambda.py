# ------------------lambda----------------

# Add two numbers

add = lambda a, b : a+b
print("add = ",add(5,7))

# find max of two numbers

maximum = lambda a,b : max(a,b)
print("maximum = ",maximum(-2,0))

# Reverse a string

name = lambda word : word[::-1]
print("reverse = ",name("python"))

#----------------map------------------

#convert celsius to fahrenheit

celsius = [34, 56, 78]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("fahrenheit = ",fahrenheit)
print("celsius = ",celsius)

#-----------------reduce-----------------