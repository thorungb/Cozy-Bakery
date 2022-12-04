import json
from menuDB import MenuDB

# object of class MenuDB
all_menu = []
menu = MenuDB("")
for i in menu.read_menu():
    product = MenuDB(i)  # create an object of class MenuDB
    product.read_menu()
    product.detail_menu()
    all_menu.append(product)


class Customer:
    def __init__(self, all_menu):
        self.__cart = []
        self.all_menu = all_menu
        self.data_menu = MenuDB.read_menu(self)

    @property
    def cart(self):
        return self.__cart

    def search_menu(self, menu_name):
        if not isinstance(menu_name, str):
            print("< Invalid input. Menu name must be a STRING. >")

        if menu_name.lower() not in str(self.data_menu).lower():  # Check if the menu name is in the menu
            print(f"< Sorry, we don't have '{menu_name}' in our menu >")  # If the menu name is not in the menu
        else:  # If the menu name is in the menu
            print("---------------------------------------------------------------------------------------")
            print("             MENU NAME               REMAINING QUANTITY      PRICE (Baht per piece)    ")
            print("---------------------------------------------------------------------------------------")
            for items in self.data_menu:  # Search for the menu name
                if menu_name.lower() in items.lower():
                    print(f" {items:^33} {self.data_menu[items]['quantity']:^22} {self.data_menu[items]['price']:^28.2f} ")
            print("---------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------")

    def show_all_menu(self):
        print("\nHere is our menu: ")
        print("---------------------------------------------------------------------------------------")
        print("             MENU NAME               REMAINING QUANTITY      PRICE (Baht per piece)    ")
        print("---------------------------------------------------------------------------------------")
        self.all_menu.sort(key=lambda x: x.name)  # sort the menu by name
        for items in self.all_menu:
            print(f" {items.name:^33} {items.quantity:^22} {items.price:^28.2f} ")
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")

    def show_menu_recommend(self):
        print("\nHere are some menu recommendations for you: ")
        print("---------------------------------------------------------------------------------------")
        print("             MENU NAME               REMAINING QUANTITY      PRICE (Baht per piece)    ")
        print("---------------------------------------------------------------------------------------")
        self.data_menu = dict(sorted(self.data_menu.items()))  # Sort the dictionary by key
        for items in self.data_menu:
            if self.data_menu[items]['recommend'] in ["Yes", "yes", "y", "Y"]:
                print(f" {items:^33} {self.data_menu[items]['quantity']:^22} {self.data_menu[items]['price']:^28.2f} ")
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")

    def show_cart(self):
        if len(self.__cart) == 0:
            print("< Your cart is EMPTY now. Please add some menu to your cart. >")
        else:
            print("\nIn your cart:")
            print("-------------------------------------------------------------------------------")
            print("             MENU NAME                  QUANTITY         TOTAL PRICE (Baht)    ")
            print("-------------------------------------------------------------------------------")
            for items in sorted(self.__cart):
                print(f" {str(items[0][0]).upper() + str(items[0][1:len(items[0]) + 1]).lower():^33} "
                      f"{items[1]:^18} {self.data_menu[items[0]]['price'] * items[1]:^24.2f} ")
            print("-------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------")

    def add_to_cart(self, menu_name, amount):
        if not isinstance(menu_name, str):
            print("< Invalid input. Menu name must be a STRING. >")
        if not isinstance(amount, int):
            print("< Invalid input. Menu quantity must be a INTEGER. >")

        if menu_name.lower() not in str(self.data_menu).lower():  # Check if the menu name is in the menu
            print(f"< Sorry, we don't have '{menu_name}' in our menu. >")
        else:  # If the menu name is in the menu
            if amount > self.data_menu[menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()]['quantity']:
                # Check if the quantity is more than the remaining quantity
                print("< Sorry, we don't have enough quantity. >")

            # Check if the menu is already in your cart
            elif (menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()) in [items[0] for items in self.__cart]:
                # i[0] is the menu name in the cart
                print("< You already have this menu in your cart. Please choose another menu or change the quantity. >")
                choice = input("Do you want to change the quantity? (Y/N): ").upper()
                if choice == "Y":  # If the user wants to change the quantity
                    for items in self.__cart:
                        if menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower() == items[0]:
                            self.__cart.remove(items)  # Remove the menu from the cart
                            self.__cart.append((menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower(), amount))
                            print("Changed the quantity successfully!\n")
                if choice == "N":  # If the user doesn't want to change the quantity
                    pass  # Do nothing

            else:  # If the menu name is not in your cart and the quantity is less than the remaining quantity
                self.__cart.append((menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower(), amount))
                # Add the name menu and the price to the basket
                with open("data_menu.json", "r") as menu_file:
                    self.data_menu = json.load(menu_file)
                    self.data_menu.update({menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower(): dict(
                        price=self.data_menu[menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()]['price'],
                        quantity=self.data_menu[menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()][
                                     'quantity'] - amount,
                        recommend=self.data_menu[menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()][
                            'recommend'],
                        status=self.data_menu[menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower()]['status'])
                    })  # Update only the remaining quantity in the menu
                with open("data_menu.json", "w") as menu_file:  # Write the updated menu to the file
                    json.dump(self.data_menu, menu_file, indent=4)
                    print(f"Added '{menu_name}' to cart successfully!\n")

    def remove_from_cart(self, menu_name):
        if not isinstance(menu_name, str):
            print("< Invalid input. Menu name must be a STRING. >")

        if len(self.__cart) == 0:  # Check if the cart is empty
            print("< Your cart is EMPTY now. Please add some menu to your cart. >")
        elif len(self.__cart) > 0:  # If the cart is not empty
            if menu_name.lower() not in str(self.__cart).lower():
                print(f"< Sorry, you don't have '{menu_name}' in your cart. >")
            else:  # If the menu name is in your cart
                for items in self.__cart:
                    if menu_name[0].upper() + menu_name[1:len(menu_name) + 1].lower() == items[0]:
                        self.__cart.remove(items)
                        print(f"Removed '{menu_name}' from cart successfully!\n")
                        Customer.show_cart(self)

    def clear_cart(self):
        self.__cart.clear()

    def pay_bill(self):
        if len(self.__cart) == 0:  # If the cart is empty
            print("< Your cart is EMPTY now. Please add some menu to your cart. >")
        else:  # If the cart is not empty
            print("\nThis is your bill: ")
            print("-------------------------------------------------------------------------------")
            print("             MENU NAME                  QUANTITY            PRICE (Baht)       ")
            print("-------------------------------------------------------------------------------")
            for items in sorted(self.__cart):
                print(f" {str(items[0][0]).upper() + str(items[0][1:len(items[0]) + 1]).lower():^33} "
                      f"{items[1]:^18} {self.data_menu[items[0]]['price'] * items[1]:^24} ")
            print("-------------------------------------------------------------------------------")
            print(
                f"Total price:    {sum([int(self.data_menu[items[0]]['price']) * items[1] for items in self.__cart]):.2f} Baht")
            pay_method = input("\nPlease choose your payment method (Cash or Credit): ").lower()
            while pay_method not in ["cash", "credit"]:  # if the payment method is not cash or credit
                print("< Invalid input. Please choose 'Cash' or 'Credit'. >")
                pay_method = input("Please choose your payment method (Cash or Credit): ").lower()
            if pay_method == "cash":  # If the payment method is cash
                cash = float(input("Please enter the amount of cash: "))
                if cash < sum([float(self.data_menu[items[0]]['price']) * items[1] for items in self.__cart]):
                    print("< Sorry, you don't have enough cash. >")
                else:
                    print(f"\nYour change is {cash - sum([float(self.data_menu[items[0]]['price']) * items[1] for items in self.__cart]):.2f} Baht")
                    print("************************* Thank you for your payment **************************")
                    self.clear_cart()  # Clear the cart after paying the bill
            elif pay_method == "credit":  # If the payment method is credit
                print("************************* Thank you for your payment **************************")
                self.clear_cart()  # Clear the cart after paying the bill
