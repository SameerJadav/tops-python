more_operations = False


def update_more_operations():
    choice = input("\nDo you want to perform more operations (y/n): ").lower()
    global more_operations
    if choice == "y":
        more_operations = True
    else:
        more_operations = False


def manage(fruits):
    menu = """
Manager:
1) Add fruit
2) View fruit stock
3) Update fruit stock
"""
    print(menu)
    operation = int(input("What operation would you like to do: "))
    if operation == 1:
        name = input("Enter fruit name: ").lower()
        quantity = int(input("Enter quantity (in KG): "))
        price = int(input("Enter price: "))
        fruits[name] = {"quantity": quantity, "price": price}
        print("Fruit added!!!")
        update_more_operations()
        if more_operations:
            manage(fruits)
        return
    elif operation == 2:
        print(f"Fruits in stock: {fruits}")
        update_more_operations()
        if more_operations:
            manage(fruits)
        return
    elif operation == 3:
        name = input("Enter fruit name: ").lower()
        if name not in fruits:
            print("Fruit you want to update does not exists")
            update_more_operations()
            if more_operations:
                manage(fruits)
            return
        quantity = int(input("Enter quantity (in KG): "))
        price = int(input("Enter price: "))
        fruits[name] = {"quantity": quantity, "price": price}
        print("Fruit updated!!!")
        update_more_operations()
        if more_operations:
            manage(fruits)
        return
    else:
        print("Invalid operation")
        return
