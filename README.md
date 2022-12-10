# Cozy Bakery
A bakery is an establishment that produces and sells flour-based food baked in an oven such as bread, cookies, cakes, donuts, pastries, and pies. Some retail bakeries are also categorized as cafés, serving coffee and tea to customers who wish to consume the baked goods on the premises. Confectionery items are also made in most bakeries throughout the world.
credit: [Google](https://en.wikipedia.org/wiki/Bakery)

## 🍰 Overview and features
This program is used for managing systems within the bakery. The main program will ask you if you are an admin or a customer.
### 🥨 Admin Part
You will become an admin when your username and password match the information contained in the database.
**If you are Admin, You can**
* **_Check the stock_** : for seeing all details of each menu including the menu name, quantity, price and status.
* **_Update some detail of the menu_** : for changing some detail of each menu except the menu name and will change the status automatically when the quantity is 0.
* **_See sales report_** : for seeing the date and time, menu name, quantity, total price and payment method that this menu was sold.

### 🥨 Customer Part
**If you are Customer, You can**
* **_Search menu_** : for searching menus from keywords
* **_See all menu_** : for showing all menus in this bakery to customer
* **_See the menu recommend_** : for showing only the recommended menu to customer
* **_See your cart_** : for showing the menu and quantity that is added to the cart
* **_Add menu to your cart_** : for adding the menu into the cart as a cart’s list
* **_Remove menu from your cart_** : for removing the menu from the cart
* **_Clear your cart_** : for clearing all items from the cart
* **_Pay the bill_** : for showing the customer a bill and letting the customer choose a payment method.

## 🍰 Required libraries and tools
There are 3 Python modules are also used in this program.
* ```json``` : which is used for data menu.
* ```csv``` : which is used for data admin and data sales summary.
* ```datetime``` : which is used for data sales summary to record the time.

Using Python version 3.10.8

## 🍰 Program design
Here is UML class diagram of the program.

![Untitled Diagram drawio](https://user-images.githubusercontent.com/112929023/206861973-9163c87b-6ae7-4dd1-97b7-9a9d59c7cd9b.png)

**There are 5 classes in this project.**
* ```MenuDB``` : this class is used to read a json file and initialize the details of each menu which consist of name, price, quantity, recommend, and status.
* ```Menu``` : this class is for adding a new menu or deleting an existing one.
* ```Admin``` : this class is for the admin and admin can access and change the details of the menu, and can see the sales report
* ```Customer``` : this class is for customers and customer can choose to see all the products in the bakery, including the ability to buy or cancel the order.
* ```Bakery``` : this class includes all the previous classes. It is used for running the program, inputting and printing out to the user.

## 🍰 Code structure
This program consists of 5 python files, 2 csv files and 1 json file.

**Python Files**
* **_menuDB.py_** which contains the ```MenuDB``` class
* **_menu.py_** which contains the ```Menu``` class
* **_admin.py_** which contains the ```Admin``` class
* **_customer.py_** which contains the ```Customer``` class
* **_bakery.py_** which contains the ```Bakery``` class

**CSV Files**
* **_data_admin.csv_** which contains all the admins' usernames and passwords
* **_data_sales_summary.csv_** which contains the details of product sales

**JSON Files**
* **data_menu.json** which contains all the menu names and their details.



### Thanks for your attention
