import json


class MenuDB:
    def __init__(self, name):
        self.__name = name
        self.__price = None
        self.__quantity = None
        self.__recommend = None
        self.__status = None
        # Out of stock: menu that is not available today or the quantity is 0
        # if the quantity = 0, the status will be changed to "out of stock"
        self.data_menu = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def recommend(self):
        return self.__recommend

    @recommend.setter
    def recommend(self, new_recommend):
        self.__recommend = new_recommend

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def read_menu(self):  # read menu from data_menu.json
        with open("data_menu.json", "r") as menu_file:
            self.data_menu = json.load(menu_file)
        return self.data_menu

    def detail_menu(self):  # get the detail of the menu
        for i in sorted(self.data_menu):
            if self.name == i:
                self.price = self.data_menu[i]["price"]
                self.quantity = self.data_menu[i]["quantity"]
                self.recommend = self.data_menu[i]["recommend"]
                self.status = self.data_menu[i]["status"]
