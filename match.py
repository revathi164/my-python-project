def add(option, x=None, y=None):   # ✅ renamed params
    match option:
        case 1:
            print(x + y)
        case 2:
            print(x * y)
        case 3 | 4:
            print("That's not a number")


choice = int(input("Enter a number: "))

if 1 <= choice <= 2:
    num1 = int(input("Enter a number a: "))
    num2 = int(input("Enter another number b: "))
    add(choice, num1, num2)
else:
    add(choice)


def s(a=None, b=None):   # ✅ renamed params to avoid PyCharm scope warning
    value = (a, b)
    match value:
        case (0, 0):
            print("0")
        case (_, 0):      # new local variable a (safe)
            print("1")
        case (0, _):      # new local variable b (safe)
            print("1")
        case _:
            print("enter correct value")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter b number: "))
s(num1, num2)