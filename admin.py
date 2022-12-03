import json
import csv
from menuDB import MenuDB

# object of class MenuDB
all_menu = []
menu = MenuDB("")
for i in menu.read_menu():
    product = MenuDB(i)  # create an object of class MenuDB
    product.read_menu()
    product.detail_menu()
    all_menu.append(product)


class Admin:
    def __init__(self, username, password, all_menu):
        self.__username = username
        self.__password = password
        self.__data_admin = []
        self.all_menu = all_menu
        self.data_menu = MenuDB.read_menu(self)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            print("< Invalid input. Password must be a STRING. >")
        if len(new_password) < 8:
            print("< Invalid input. Password must be at least 8 characters. >")
        self.__password = new_password

    @property
    def data_admin(self):
        return self.__data_admin

    @data_admin.setter
    def data_admin(self, new_data_admin):
        self.__data_admin = new_data_admin

    def read_data_admin(self):
        with open('data_admin.csv', 'r') as admin_file:
            rows = csv.DictReader(admin_file)
            for items in rows:
                self.__data_admin.append(items)
        return self.__data_admin

    def is_admin(self):
        # check if username and password are correct with the data in data_admin.csv
        self.read_data_admin()
        for items in self.__data_admin:
            if self.username == items['username'] and self.password == items['password']:
                return True

    def check_stock(self):
        # see the stock of each menu
        print("-------------------------------------------------------------------------------------------------------")
        print("             MENU NAME                QUANTITY      PRICE (Baht)      RECOMMEND           STATUS       ")
        print("-------------------------------------------------------------------------------------------------------")
        self.all_menu.sort(key=lambda x: x.name)  # sort the menu by name
        for items in self.all_menu:
            print(f" {items.name:^33} {items.quantity:^14} {items.price:^16.2f} {items.recommend:^16} {items.status:^20}")
        print("-------------------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------")

    def update_detail(self, menu_name):  # admin can change the price, quantity, recommend, and status of each menu
        def update_information():  # update the information of the menu
            with open("data_menu.json", "w") as menu_file:
                json.dump(self.data_menu, menu_file, indent=4)

        def auto_update_status():  # Auto update the status of the menu
            if int(self.data_menu[(menu_name[0].upper() + menu_name[1:len(menu_name) + 1])]['quantity']) == 0:
                self.data_menu[(menu_name[0].upper() + menu_name[1:len(menu_name) + 1])]['status'] = "out of stock"
                update_information()
            elif int(self.data_menu[(menu_name[0].upper() + menu_name[1:len(menu_name) + 1])]['quantity']) > 0:
                self.data_menu[(menu_name[0].upper() + menu_name[1:len(menu_name) + 1])]['status'] = "available"
                update_information()

        def input_choice():
            print("\n>> What do you want to change in this menu?")
            choice = input("1. Price\n2. Quantity\n3. Recommend\n4. Status\n5. Quit\nPlease select choice: ")
            return choice

        def print_current():
            print(f"\nCURRENT information of '{menu_name}':")
            print(
                "-------------------------------------------------------------------------------------------------------")
            print(
                "             MENU NAME                QUANTITY      PRICE (Baht)      RECOMMEND           STATUS       ")
            print(
                "-------------------------------------------------------------------------------------------------------")
            print(f" {items:^33} {self.data_menu[items]['quantity']:^14} {self.data_menu[items]['price']:^16.2f}  "
                  f"{self.data_menu[items]['recommend']:^14} {self.data_menu[items]['status']:^22} ")
            print(
                "-------------------------------------------------------------------------------------------------------")
            print(
                "-------------------------------------------------------------------------------------------------------")

        if str(menu_name).lower() not in str(self.data_menu).lower():  # Check if the menu name is in the menu list
            print(f"< Sorry, '{menu_name}' doesn't exist in the menu. >")
        else:
            for items in self.data_menu:
                if menu_name.lower() == items.lower():  # if menu name exists, show only the menu that the admin wants to change
                    print_current()
                    choice = input_choice()
                    while True:
                        if choice == "1":
                            new_price = input("Enter new price: ")
                            while not new_price.isdigit():
                                print("< Invalid input. Menu price must be a NUMBER. >")
                                new_price = input("Enter new price: ")
                            self.data_menu[items]['price'] = float(new_price)
                            print("Price has been changed successfully!")
                            update_information()
                            print_current()
                        elif choice == "2":
                            new_quantity = input("Enter new quantity: ")
                            while not isinstance(new_quantity, int):
                                print("< Invalid input. Menu quantity must be a INTEGER. >")
                                new_quantity = input("Enter new quantity: ")
                            self.data_menu[items]['quantity'] = int(new_quantity)
                            print("Quantity has been changed successfully!")
                            auto_update_status()
                            update_information()
                            print_current()
                        elif choice == "3":
                            new_recommend = input("Enter new recommend (y/n): ").lower()
                            while new_recommend not in ["y", "n", "Y", "N", "No", "Yes", "no", "yes", "NO", "YES"]:
                                print("< Invalid input. Please choose only 'YES' or 'NO'. >")
                                new_recommend = input("Enter new recommend (y/n): ").lower()
                            if new_recommend in ["y", "Y", "yes", "Yes", "YES"]:
                                self.data_menu[items]['recommend'] = "yes"
                            elif new_recommend in ["n", "N", "no", "No", "NO"]:
                                self.data_menu[items]['recommend'] = "no"
                            update_information()
                            print("Recommend has been changed successfully!")
                            print_current()
                        elif choice == "4":
                            # Available: today's menu
                            # Out of stock: menu that is not available today or the quantity is 0
                            new_status = input("Enter new status (A)vailable/(O)ut of stock: ").lower()
                            while new_status not in ["a", "o", "A", "O", "Available", "Out of stock", "available",
                                                     "out of stock", "AVAILABLE", "OUT OF STOCK"]:
                                print("< Invalid input. Please choose only 'AVAILABLE' or 'OUT OF STOCK'. >")
                                new_status = input("Enter new status (A)vailable/(O)ut of stock: ").lower()
                            if new_status in ["a", "A", "available", "Available", "AVAILABLE"]:
                                if int(self.data_menu[items]['quantity']) == 0:
                                    print("< Sorry, the quantity is 0. Please change the quantity first. >")
                                    # out the if statement and go back to the while loop
                                    choice = input_choice()
                                    continue
                                else:
                                    self.data_menu[items]['status'] = "available"
                            elif new_status in ["o", "O", "out of stock", "Out of stock", "OUT OF STOCK"]:
                                self.data_menu[items]['status'] = "out of stock"
                            print("Status has been changed successfully!")
                            update_information()
                            print_current()
                        elif choice == "5":
                            print("< Quit >")
                            break
                        else:
                            print("< Invalid input, please try again. >")
                        choice = input_choice()
