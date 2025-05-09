more_operations = False


def update_more_operations():
    choice = input("\nDo you want to perform more operations (y/n): ").lower()
    global more_operations
    if choice == "y":
        more_operations = True
    else:
        more_operations = False


def shop(fruits):
    menu = """
Customer:
1) Shop fruit
2) View fruit
"""
    print(menu)
    operation = int(input("What operation would you like to do: "))
    if operation == 1:
        name = input("Enter fruit name: ").lower()
        if name not in fruits:
            print("Fruit you want to update does not exists")
            update_more_operations()
            if more_operations:
                shop(fruits)
            return
        quantity = int(input("Enter quantity (in KG): "))
        if fruits[name]["quantity"] < quantity:
            print("Not enough fruit in stock")
            update_more_operations()
            if more_operations:
                shop(fruits)
            return
        print(f"{name} {quantity}KG = {quantity * fruits[name]['price']}")
        buy = input(f"Do you want to buy {name} (y/n): ").lower()
        if buy == "y":
            if fruits[name]["quantity"] == quantity:
                fruits.pop(name)
            else:
                fruits[name]["quantity"] -= quantity
    elif operation == 2:
        print(f"Fruits in stock: {fruits}")
        update_more_operations()
        if more_operations:
            shop(fruits)
        return
    else:
        print("Invalid operation")
        return
