import customer
import manager

fruits = {
    "apple": {"quantity": 5, "price": 20},
    "mango": {"quantity": 1, "price": 30},
}

stop = False


def update_stop():
    choice = input("\nDo you want to continue (y/n): ").lower()
    global stop
    if choice != "y":
        stop = True


while not stop:
    menu = """
Welcome to The Fruit Market!

Roles:
1) Manager
2) Customer
"""
    print(menu)
    role = int(input("Select your role: "))
    if role == 1:
        manager.manage(fruits)
        update_stop()
    elif role == 2:
        customer.shop(fruits)
    else:
        print("Role does not exist")
        update_stop()
