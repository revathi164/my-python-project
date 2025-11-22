
#--------------------File Handling---------------------
# Working with files
# Access modes
# 1.read only(r)
# 2.write only(w)
# 3.read and write(r+)
# 4.write and read(w+)
# 5.append only(a)
# 6.append and read(a+)

# -------------open file----------------
# syntax:
# open(filename, access mode)
#
# file = open("python", "w+")
#
#
# file.write("hello ")
# file.write("welcome")
# print(file.read())


# file = open("python", "w")
# file.write("hello world")

file = open("python","a+")
file.write(" lavanya")
file.close()





# file = open("revathi.txt","w")
# name = input("Enter your name: ")
# file.write(f"welcome {name} to google")
# friends = ["John","Jane","Jack"]
# file.writelines(friends)

# file = open("revath","w")
# file.write("revathi")
# file.close()

#--------------with statement--------------
# to write cleaner code

# syntax:
# with open("python","r") as file:
#      print(file.read())

with open("python","w") as f:
    f.write("thank you")

