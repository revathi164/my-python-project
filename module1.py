# print("hello world")
# first_name = "revathi"
# last_name = "chenchu"
# full_name = first_name + " " + last_name
# # print("hello "+ name)
# print(full_name)
import time

# age = 21
# age = age + 10
# age += 1
# print(age)
# print(type(age))
# print('your age is :'+str(age))

# height = 250.5
# print("your height is " + str(height) + "cm")
# height = height + 5
# print("your height is " + str(height) + "cm")
# print(type(height))
#
# human =  True
# print("are you a human: " + str(human))
# print(type(human))

# name = "bro"
# age = 21
# attractive = False
#
# name, age, attractive = "revathi", 21, True
# print(name, age, attractive)
#
#  a = 30
#  b = 30
#  c = 30
#
# a = b = c = 30
# print(a, b, c)

# name = "bro code"
# print(len(name))
# print(name.find("bro"))
# print(name.find("code"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "a"))
# print(name * 3)

# x = 1
# y = 2.0
# z = "3"
#
# y = str(y)
# z = str(z)
# x = str(x)
#
# print(x)
# print(y)
# print(z*3)

# name = input("what is your name : ")
# age = int(input("what is your age : "))
# height = float(input("how tall are you : "))
#
# print("hello " + name)
# print("your age "+str(age)+"years old")
# print("you are "+ str(height)+ "cm tall")

# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3


# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x, y, z))
# print(min(x, y, z))

# name = "bro code"
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name[::-1]
#
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1= "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print( website1[slice])
# print( website2[slice])

# age = int(input("how old are you : "))
# if age == 100:
#     print("you are a century old!")
# elif age >= 18:
#     print("you are an adult!")
# elif age < 0:
#     print("you haven't been born yet")
# else:
#     print("you are a child!")

# temp = int(input("what is the temperature outside : "))
# if not(temp >= 0 and temp <= 30):
#     print("the temperature is good today!")
#     print("go outside!")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is bad today!")
#     print("stay inside!")

# while 1 == 1:
#      print("Help! i am stuck in a loop!")


# name = ""
# while len(name) == 0:
#     name = input("enter your name : ")
# print("hello "+name)

# name = None
# while not name :
#     name = input("Enter your name: ")
# print(name)

# for i in range(10):
#     print(i+1)

# for i in range(50,101,2):
#     print(i)

# for i in "revathi":
#     print(i)

# import time
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("happy new year!")

# rows = int(input("How many rows?"))
# columns = int(input("How many columns?"))
# symbol = input("What is your symbol?")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# import math
# print(math.ceil(67.9))
# print(math.remainder(4,2))

# while True:
#     name = input("enter your name: ")
#     if name != "":
#         break


# phone_number = "123-456-7892"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     else:
#         print(i,end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)
#
# food =["pizza", "hamburger", "hotdog", "cup cake"]
# food[0] = "sushi"



# food.append("pizza")
# print(food)
# food.remove("pizza")
# print(food)
# food.pop()
# print(food)
# food.insert(0,"pizza")
# print(food)
# food.sort()
# food.clear()
#
# for i in food:
#     print(i)


# drinks = ['coffee', 'milk', "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream", "dessert"]
#
# food = [drinks, dinner, dessert]
# print(food[1][0])

# students = ("bro" , 21, "male")
# print(students.count("bro"))
# print(students.index("male"))
#
# for i in students:
#     print(i)
#
# if "bro" in students:
#     print("bro is here")

# u = {"fork", "spoon", "knife","knife"}
# d = {"bowl", "plate", "cup", "knife"}
# u.add("knight")
# u.remove("knight")
# u.clear()
# d.update(u)
# dinner_table = u.union(d)
# print(dinner_table)
#
# for i in dinner_table:
#     print(i)

# print(d.difference(u))
# print(u.intersection(d))

# capitals ={"usa":"washington",
#            "india":"new dehli",
#            "china":"beijing",
#             "russia":"moscow"}
#
# capitals.update({"germany":"berlin"})
# capitals.update({"usa":"las vegas"})
# capitals.pop("china")
# capitals.clear()
#
# # print(capitals["germany"])
# # print(capitals.get("germany"))
# print(capitals)
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# for key, value in capitals.items():
#     print(key, value)

# ========index operator []===========

# name = "bro code!"
#
# # if (name[0].islower()):
# #     name = name.capitalize()
#
# first_name = name[:3].upper()
# last_name = name[4:]
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)

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


# ==========str.format=========

# animal = "cow"
# item = "moon"

# print("the {1} jumped over the {1}".format(animal,item))  # positional argument
# print("the {animal} jumped over the {animal}".format(animal="cow",item="moon"))  # keyword argument

# text = "the {} jumped over the {}"
# print(text.format(animal, item))
#
# name = "bro"
#
# print("hello, my name is {}".format(name))
# print("hello, my name is {:10} nice to meet you".format(name))
# print("hello, my name is {:<10} nice to meet you".format(name))
# print("hello, my name is {:>10} nice to meet you".format(name))
# print("hello, my name is {:^10} nice to meet you".format(name))


# number = 15000
# print("the number pi is {:.3f}".format(number))
# print("the number pi is {:b}".format(number))
# print("the number pi is {:0}".format(number))
# print("the number pi is {:x}".format(number))
# print("the number pi is {:X}".format(number))
# print("the number pi is {:e}".format(number))
# print("the number pi is {:E}".format(number))
# print("the number pi is {:,}".format(number))


# ========= random=============

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
#
# mylist = ["rock", "paper", "scissor"]
# z = random.choice(mylist)
#
# cards = [1,2,3,4,5,6,7,8,9,"j","k","q","A"]
# random.shuffle(cards)
#
#
# print(x)
# print(y)
# print(z)
# print(cards)

# ================= exception handling ===========

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
#
# except ValueError as e:
#     print(e)
#     print("enter only numbers")
#
# except Exception as e:
#      print(e)
#      print("something went wrong")
#
# else:
#     print(result)
#
# finally:
#     print("this will always execute")


# import os
#
# path = "C:\\Users\\Abcom\\folder"
#
# if os.path.exists(path):
#     print("location exists")
#     if os.path.exists(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("location doesn't exist")

# try:
#     with open("text.tx") as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("file was not found!")

# text = "have a nice day!"
#
# with open("text.txt","a") as file:
#     file.write(text)

# import shutil
#
# shutil.copyfile("text.txt","copy.txt")

import os
#
#
# source ="revathi.txt "
# destination = "C:\\Users\\Abcom\\Desktop\\revathi.txt"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file")
#     else:
#         os.replace(source, destination)
#         print(source,"was moved")
#
# except FileNotFoundError:
#     print(source,"not found")

# source ="revathi.txt"
# destination = "C:\\Users\\Abcom\\Desktop\\revathi.txt"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file")
#     else:
#         os.replace(source, destination)
#         print(source,"was moved")
#
# except FileNotFoundError:
#     print(source,"not found")

# import shutil
#
# path = "folder"
#
# try:
    # os.remove(path) #delete a file
    # os.rmdir(path) #delete empty directory
#     shutil.rmtree(path) #delete a directory containing files
# except FileNotFoundError:
#     print("File doesn't exist")
# except PermissionError:
#     print("you don't have permission to do that")
# except OSError:
#     print("you cannot delete that using that function")
# else:
#     print(path,"was deleted")


#============= modules =================

# import messages as msg
# from messages import hello,bye


# hello()
# bye()

# help("modules")

# ============ object oriented programming ===============

# from car import Car
#
# car_1 = Car("chevy","corvette",2021,"blue")
#
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
#
# car_1.drive()
# car_1.stop()


# car_1 = Car("chevy","corvette",2021,"blue")
# car_2 = Car("toyota","corvette",2021,"red")
#
# Car.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)


# =================== inheritance ==================

# class Animals:
#
#     alive = True
#
#     def eat(self):
#         print("this animal is eating")
#
#     def sleep(self):
#         print("this animal is sleeping")
#
#
# class Rabbit(Animals):
#     def run(self):
#         print("this rabbit is running")
#
# class Fish(Animals):
#     def swim(self):
#         print("this fish is swimming")
#
# class Hawk(Animals):
#     def fly(self):
#         print("this hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
#
# hawk.fly()
# rabbit.run()
# fish.swim()


#================== multi-level inheritance ==============

# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("this animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("this dog is barking")
#
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

#==================== multiple inheritance ====================

# class prey:
#
#     def flee(self):
#         print("this animal flees")
#
# class predator:
#
#     def hunt(self):
#         print("this animal hunts")
#
#
# class Rabbit(prey):
#     pass
#
# class Hawk(predator):
#     pass
#
# class Fish(prey, predator):
#     pass
#
# rabit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

#=============== method overriding ===============

# class Animal:
#
#     def eat(self):
#         print("this animal is eating")
#
# class Rabbit(Animal):
#     def eat(self):
#         print("this rabbit is eating a carrot")
#
# rabbit = Rabbit()
# rabbit.eat()


#=============== method chaining ========================

# class Car:
#
#     def turn_on(self):
#         print("you start the engine")
#         return self
#
#     def drive(self):
#         print("you drive the car")
#         return self
#
#     def brake(self):
#         print("you step on the break")
#         return self
#
#     def turn_off(self):
#         print("you turn off the engine")
#         return self
#
# car = Car()

# car.turn_on().drive()

# car.brake().turn_off()

# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

#===================== super function ==================

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length * self.width
#
#
#
# class Cube(Rectangle):
#
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
# square = Square(3,3)
# cube = Cube(3,3,3)
#
# print(square.area())
# print(cube.volume())

# ===================== abstract class ==================

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#
#     @abstractmethod
#
#     def go(self):
#         pass
#
# class Car(Vehicle):
#
#     def go(self):
#         print("you drive the car")
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("you drive the motorcycle")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# vehicle.go()
# car.go()
# motorcycle.go()


#================== objects as arguments ===========

# class Car:
#
#     color = None
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# def change_color(vehile, color):
#
#     vehile.color = color
#
#
#
#
# change_color(car_1, "red")
# change_color(car_2, "blue")
# change_color(car_3, "green")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)


# ====================== duck typing ==============

# class Duck:
#
#     def walk(self):
#         print("this duck is walking")
#
#     def talk(self):
#         print("this duck is qwuaking")
#
# class Chicken:
#
#     def walk(self):
#         print("this chicken is walking")
#
#     def talk(self):
#         print("this chicken is clucking")
#
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("you caught thr critter")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)


# ================== walrus operator ================

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#     food = input("enter what food you like? : ")
#     if food != "quit":
#        foods.append(food)
#     else:
#         break

#
# foods = list()
# while food := input("enter what food do you like? : ") != "quit":
#     foods.append(food)


# ======================== functions to variables (alisa) ================

# def hello():
#     print("Hello World")
#
#
# hi = hello
# hello()
# hi()


# say = print
# say("hello")

# ================ higher order functions ============

# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))


# =============  lamda function ===============

# def double(x):
#     return x*2
#
# print(double(5))

# double = lambda x : x*2
# multiply = lambda x, y : x*y
# add = lambda x, y, z : x+y+z
# full_name = lambda first_name, last_name : first_name+" "+last_name
# age_check = lambda age : True if age >= 18 else False
#
# print(double(5))
# print(multiply(5,6))
# print(add(5,6,7))
# print(full_name("bro","code"))
# print(age_check(16))

# ================ sort ==================

# students = ("revathi","jannu","bhargavi","priya")
#
# # students.sort(reverse= True)
# sorted_students = sorted(students, reverse= False)
#
# for i in sorted_students:
#     print(i)


# students = [("revathi","f",21),
#             ("sandy","a",20),
#             ("jannu","b",24)]
#
# age = lambda ages : ages[2]
# students.sort(key = age)
#
# for i in students:
#     print(i)

# students = (("revathi","f",21),
#             ("sandy","a",20),
#             ("jannu","b",24))
#
# age = lambda ages : ages[2]
# sorted_students = sorted(students,key = age)
#
#
# for i in sorted_students:
#      print(i)


# ============= map function ==================

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jackets",50.00)]
#
# to_euros = lambda data : (data[0],data[1]*0.82)
# to_dollors = lambda data : (data[0],data[1]/0.82)
#
# # store_euros = list( map(to_euros, store))
# #
# # for i in store_euros:
# #     print(i)
#
# store_dollors = list( map(to_dollors, store))
#
# for item in store_dollors:
#     print(item)


#================= filter ================

# friends = [("revathi",21),
#            ("jannu",24),
#            ("bhargavi",18),
#            ("purushotam",15)]
#
# age = lambda data: data[1] >= 18
#
# drinking_buddies = list(filter(age, friends))
#
# for i in drinking_buddies:
#     print(i)

# ================= reduce function ===========

# import functools
#
# # letters = ["h","e","l","l","o"]
# # word = functools.reduce(lambda x,y:x + y, letters)
# # print(word)
#
# factotial = [5,4,3,2,1]
# result = functools.reduce(lambda x,y: x*y, factotial)
# print(result)


# =============== list comprehension =========================


# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)
#
# squares = [i*i for i in range(1,11)]
# print(squares)


# students = [100,90,80,70,60,50,40,30,0]

# passed_students = list (filter(lambda x: x >= 60, students))

# passed_students = [i  for i in students if i >= 60 ]

# passed_students = [i if i >= 60 else "failed" for i in students]
#
# print(passed_students)


# ================== dictionary comprehension ===============

# dictionary = {key : expression for (key,value) in iterable}

# cities_in_f = {"new york":32,"boston":75,"los angeles":100,"chicago":50}
#
# cities_in_c = {key : round((value - 32)*(5/9)) for (key,value) in cities_in_f.items() }
# print(cities_in_c)

# weather = {'new york':'snowing','bostan':'sunny','los angels':'sunny','chicago':'cloudy'}
# sunny_weather = {key : value for key,value in weather.items() if value == "sunny"}
# print(sunny_weather)

# cities_in_f = {"new york":32,"boston":75,"los angeles":100,"chicago":50}
# desc_cities = {key : ("warm" if value >= 40 else "cold")   for key,value in cities_in_f.items()}
# print(desc_cities)

# def check_temp(value):
#     if value >= 70:
#         return "hot"
#     elif  69 >= value >= 40:
#         return "warm"
#     else:
#         return "cold"
#
#
#
# cities_in_f = {"new york":32,"boston":75,"los angeles":100,"chicago":50}
# desc_cities = {key : check_temp(value) for key,value in cities_in_f.items()}
# print(desc_cities)


# ====================== zip function ========================

# user_name = ["dude","bro","code"]
# password = ("password","123ab","abcd")
#
# users = dict(zip(user_name,password))
#
# print(type(users))
#
# for key,value in users.items():
#     print(key,":",value)

# user_name = ["dude","bro","code"]
# password = ("password","123ab","abcd")
# login_date =["1/2/2021","2/3/2022","3/4/2022"]
#
# users = zip(user_name,password,login_date)
#
# for i in users:
#     print(i)


# ======================== if __name__ == '__main__'

# import module
#
# print(__name__)
# print(module.__name__)


# def hello():
#     print("Hello World")
#
# if __name__ == '__main__':
#     hello()


# if __name__ == '__main__':
#     print("running this module directly")
#
# else:
#     print("running this module from another module")


# =================== time module ====================

import time

# print(time.ctime(0))
#
# print(time.time())
#
# print(time.ctime(time.time()))

# time_object  = time.localtime()
# time_object = time.gmtime()
#
# print(time_object)
#
# local_time = time.strftime("%B %d %y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 april 2020"
# time_object= time.strptime(time_string,"%d %B %Y")
# print(time_object)

# time_tuple = (2020,4,20,4,20,0,0,0,0)
# time_string = time.asctime(time_tuple)
# print(time_string)
#
# time_tuple = (2020,4,20,4,20,0,0,0,0)
# time_string = time.mktime(time_tuple)
# print(time_string)


# ============= threading =================

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat break fast")

def frink_coffe():
    time.sleep(4)
    print("you drink coffee")

def study():
    time.sleep(5)
    print("you finish studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=frink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# frink_coffe()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())











