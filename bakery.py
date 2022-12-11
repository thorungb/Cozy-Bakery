from admin import Admin
from customer import Customer
from menu import Menu
from menuDB import MenuDB

# object of class MenuDB
all_menu = []
menu = MenuDB("")
for i in menu.read_menu():
    product = MenuDB(i)   # create an object of class MenuDB
    product.read_menu()
    product.detail_menu()
    all_menu.append(product)


class Bakery:
    def __init__(self):
        self.admin_choice = None  # is the number choice that the admin choose
        self.customer_choice = None  # is the number choice that the customer choose
        self.data_menu = MenuDB.read_menu(self)  # is a dictionary from the class MenuDB

    def admin_action(self, admin):
        while True:
            print("\n------------------------- Welcome to Admin management system! -------------------------")
            print("1. Check stock \n2. Update detail \n3. Add new menu \n4. Delete menu \n5. Sales report \n6. Exit")
            try:
                self.admin_choice = int(input("Select your choice: "))
            except ValueError:
                print("< Choice must be a NUMBER. >")
            else:
                if self.admin_choice == 1:  # if the admin choose to check stock
                    print("\nThis is the current stock of all menu: ")
                    admin.check_stock()
                elif self.admin_choice == 2:  # if the admin choose to update detail
                    menu_name = input("Enter the full name of the menu correctly (e.g. Almond croissant): ")
                    admin.update_detail(menu_name)
                elif self.admin_choice == 3:  # if the admin choose to add new menu
                    print("You are adding a new menu...")
                    Menu.add_new_menu(self)
                elif self.admin_choice == 4:  # if the admin choose to delete menu
                    print("You are deleting a menu...")
                    menu_name = input("Enter the full name of the menu correctly (e.g. Almond croissant): ")
                    Menu.delete_menu(self, menu_name)
                elif self.admin_choice == 5:  # if the admin choose to see the sales report
                    admin.sales_report()
                elif self.admin_choice == 6:  # if the admin choose to exit
                    print("\n> Thank you for using the system, Have a nice day! (◕‿◕✿) <")
                    return self.admin_choice
                elif self.admin_choice not in [1, 2, 3, 4, 5, 6]:
                    print("< Please enter a number from 1 to 5 >")

    def customer_action(self, customer):
        while True:
            print("\n-------------------------- Hello CUSTOMER, tell me you want ---------------------------")
            print("1. Search menu \n2. View menu \n3. Shopping cart \n4. Pay the bill \n5. Exit")
            try:
                self.customer_choice = int(input("Select your choice: "))
            except ValueError:
                print("< Choice must be a NUMBER. >")
            else:
                if self.customer_choice == 1:  # if the customer wants to search the menu
                    menu_name = input("Enter the menu name: ")
                    while type(menu_name) != str:
                        print("< Menu name must be a STRING. >")
                        menu_name = input("Enter the menu name: ")
                    customer.search_menu(menu_name)
                elif self.customer_choice == 2:  # if the customer wants to view the menu
                    choice = input(
                        ">> Do you want to see all menu or recommended menu? (A)ll or (R)ecommended: ").upper()
                    if choice in ["A", "ALL"]:
                        customer.show_all_menu()
                    elif choice in ["R", "RECOMMENDED"]:
                        customer.show_menu_recommend()
                    else:
                        print("< Please enter A or R >")
                elif self.customer_choice == 3:  # if the customer wants to do with the shopping cart
                    print(
                        f"\n>> What do you want to do? \n1. Add to cart \n2. Remove from cart \n3. Clear cart \n4. View cart")
                    choice = int(input("Select your choice: "))
                    if choice == 1:  # if the customer wants to add to cart
                        menu_name = input("Enter the full name of the menu correctly (e.g. Almond croissant): ")
                        amount = int(input("How much do you want to add?: "))
                        customer.add_to_cart(menu_name, amount)
                    elif choice == 2:  # if the customer wants to remove from cart
                        menu_name = input("Enter the full name of the menu correctly (e.g. Almond croissant): ")
                        amount = int(input("How much do you want to remove?: "))
                        customer.remove_from_cart(menu_name, amount)
                    elif choice == 3:  # if the customer wants to clear the cart
                        customer.clear_cart()
                        print("Your cart is cleared successfully!\n")
                    elif choice == 4:  # if the customer wants to view the cart
                        customer.show_cart()
                elif self.customer_choice == 4:  # if the customer wants to pay the bill
                    customer.pay_bill()
                elif self.customer_choice == 5:  # if the customer wants to exit
                    print("\n> Thank you for using the system, Have a nice day! (◕‿◕✿) <")
                    return self.customer_choice
                elif self.customer_choice not in [1, 2, 3, 4, 5]:
                    print("< Please enter a number from 1 to 5 >")

    def main(self):
        while True:
            print("\n------------------------ Welcome to Cozy Bakery! °˖✧◝(⁰▿⁰)◜✧˖° -----------------------")
            role = input("Please select your role? (C)ustomer or (A)dmin: ").upper()
            if role in ["A", "ADMIN"]:
                for times in range(3):
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    admin = Admin(username, password, all_menu)
                    if admin.is_admin():  # if the username and password are correct
                        self.admin_action(admin)
                        break
                    else:
                        print("< Invalid username or password >")
                if self.admin_choice == 6:
                    break
                else:
                    print("< You have entered the wrong username or password 3 times. Please try again later >")
            elif role in ["C", "CUSTOMER"]:
                customer = Customer(all_menu)
                self.customer_action(customer)
                if self.customer_choice == 5:
                    break


if __name__ == "__main__":
    bakery = Bakery()
    bakery.main()
