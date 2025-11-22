# =========== functions ==============

# def hello(first_name, last_name, age):
#     print("Hello",first_name,last_name)
#     print("your age is ",age)
#     print("have a nice day")
#
#
# hello("bro","code", 21)

# def multify(num1,num2):
#     result = num1*num2
#     return result
#
# x = multify(1,2)
# print(x)
# print(multify(1,2))


# def hello(first,middle,last):
#     print("hello",first,middle,last)
#
# hello(last = "code",first = "bro",middle = "dude")

# num = float(input("Enter a number: "))
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a number: ")))))

# name = "bro"   # global variable
#
# def display_name():
#       name = "code"   #local variable
#       print(name)
#
# display_name()
# print(name)

# ===== *args =======

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0]= 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

# ======= **kwargs ======

# def hello(**names):
#     # print('Hello',kwargs['first'],kwargs['middle'],kwargs['last'])
#     print("hello",end =" ")
#     for key,value in names.items():
#         print(value, end =" ")
#
# hello(title = "mr",first = "bro",middle = "dude", last = "code")