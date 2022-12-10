import json
from menuDB import MenuDB


class Menu:
    def __init__(self):
        self.data_menu = MenuDB.read_menu(self)

    def add_new_menu(self):
        new_name = input("Please enter new menu name: ")
        if not isinstance(new_name, str):
            print("< Invalid input. Menu name must be a STRING. >")

        new_price = float(input("Please enter new menu price: "))
        if not isinstance(new_price, (int, float)):
            print("< Invalid input. Menu price must be a NUMBER. >")

        new_quantity = int(input("Please enter new menu quantity: "))
        if not isinstance(new_quantity, int):
            print("< Invalid input. Menu quantity must be a INTEGER. >")

        new_recommend = input("Please enter new menu recommend (Yes or No): ")
        if new_recommend in ["Yes", "yes", "y", "Y", "YES"]:
            new_recommend = "yes"
        elif new_recommend in ["No", "no", "n", "N", "NO"]:
            new_recommend = "no"
        else:
            print("< Invalid input. Please choose only 'YES' or 'NO'. >")

        new_status = input("Please enter new menu status (Available or Out of stock): ")
        if new_status in ["Available", "available", "AVAILABLE", "a", "A"]:
            new_status = "available"
        elif new_status in ["Out of stock", "out of stock", "OUT OF STOCK", "o", "O"]:
            new_status = "out of stock"
        else:
            print("< Invalid input. Please choose only 'AVAILABLE' or 'OUT OF STOCK'. >")

        # add new menu to data_menu.json
        new_data = {
            (str(new_name[0].upper()) + str(new_name[1:len(new_name) + 1]).lower()): {
                "price": new_price,
                "quantity": new_quantity,
                "recommend": new_recommend,
                "status": new_status
            }
        }
        if str(new_name).lower() in str(self.data_menu).lower():  # if menu name exists
            print(f"< Sorry, '{new_name}' already exists in menu. >")
        else:  # if menu name doesn't exist
            self.data_menu.update(new_data)
            with open("data_menu.json", "w") as menu_file:
                json.dump(self.data_menu, menu_file, indent=4)
            print(f"'{new_name}' has been ADDED to menu!")

    def delete_menu(self, menu_name):
        if str(menu_name).lower() in str(self.data_menu).lower():  # if menu name exists
            del self.data_menu[(str(menu_name[0].upper()) + str(menu_name[1:len(menu_name) + 1]).lower())]
            with open("data_menu.json", "w") as menu_file:  # update data_menu.json
                json.dump(self.data_menu, menu_file, indent=4)
            print(f"'{menu_name}' has been DELETED from menu!")
        else:  # if menu name doesn't exist
            print(f"< Sorry, '{menu_name}' doesn't exist in menu. >")
