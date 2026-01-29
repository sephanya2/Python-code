lst = []

while True:
    print("\n----- LIST OPERATIONS MENU -----")
    print("1. Add element")
    print("2. Delete element")
    print("3. Display list")
    print("4. Search element")
    print("5. Sort list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to add: ")
        lst.append(element)
        print("Element added")

    elif choice == 2:
        element = input("Enter element to delete: ")
        if element in lst:
            lst.remove(element)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice == 3:
        print("List elements:", lst)

    elif choice == 4:
        element = input("Enter element to search: ")
        if element in lst:
            print("Element found at position", lst.index(element))
        else:
            print("Element not found")

    elif choice == 5:
        lst.sort()
        print("List sorted:", lst)

    elif choice == 6:
        print("Exiting program")
        break

    else:
        print("Invalid choice! Try again")
