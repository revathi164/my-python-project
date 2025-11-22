def library_record():
    print("\nLibrary Record.")
    taken_list = []
    book_list = {1: "python", 2: "java", 3: "c++", 4: "c#", 5: "java script"}

    while True:
        print("\nAvailable Books:")
        for no, name in book_list.items():
            print(f"{no}. {name}")

        try:
            book_no = int(input("\nEnter book number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if book_no not in book_list:
            print("\nBook not found")
        else:
            book_name = book_list[book_no]
            if book_name in taken_list:
                print(f"\n'{book_name}' is already taken")
            else:
                print(f"\nBook = {book_name}")
                input("Press enter to take the book...")
                taken_list.append(book_name)
                print("Completed! You can take the book.")

        print("\nBooks taken so far:", taken_list)
        input("\nPress enter to continue...\n")

library_record()


