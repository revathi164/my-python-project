# student_details = []
# with  open("student_file.txt", "w") as file:
#
#     while True:
#         file.write("""
#     Student management system
#
#     1.Add student details
#     2.Record marks
#     3.Log attendance
#     4.Assign tasks
#     5.View reports
#     6.Exit""")
#         option = input("Enter option: ")
#         if option == "1":
#             print("Add student details")
#             number = int(input("enter number of students to add = "))
#             for i in range(number):
#                 roll_no = input("Enter roll no: ")
#
#             with open("student_file.txt", "a") as file:
#                 student_details.append(roll_no + "\n")
#                 file.writelines(student_details)

import csv
with  open("student_file.csv", "w") as file:
    writer = csv.writer(file)
student_details = []

while True:
    print("""
Student Management System
1. Add student details
2. Exit
""")
    option = input("Enter option: ")

    if option == "1":
        number = int(input("Enter number of students to add: "))
        for i in range(number):

            roll_no = input(f"Enter roll no for student {i + 1}: ")
            name = input("Enter student name: ")
            course = input("Enter course name: ")
            batch_number = input("Enter batch number: ")



            # student_details.append(roll_no + "\n")


            with open("student_file.csv", "a") as file:
                file.write("roll number = " + roll_no + " ")
                file.write("name = " + name + " ")
                file.write("course = " + course + " ")
                file.write("batch_number = " + batch_number+"\n" )

        print("Students added successfully!\n")

    elif option == "2":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Try again.\n")
