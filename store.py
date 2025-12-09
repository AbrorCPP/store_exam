from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Product:
    def __init__(self, name, price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class User:
    def __init__(self, user_name, email, phone, password,balance):
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.password = password
        self.is_admin = False
        self.balance = balance
        self.korzinka = []
        self.history = []

class Manager:
    def __init__(self):
        self.users = []
        self.products = []

    def add_user(self):
        user_name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        phone = input("Please enter your phone: ")
        password = input("Please enter your password: ")
        balance = int(input("Please enter your balance: "))
        s1 = User(user_name, email, phone, password, balance)
        self.users.append(s1)

    def print_users(self):
        count = 0
        for user in self.users:
            if not user.is_admin:
                count += 1
                print(f"{count}. {user.user_name} {user.email} {user.phone} {user.password} {user.balance}")

    def add_product(self):
        product = input("Please enter your product: ")
        price = int(input("Please enter your price: "))
        amount = int(input("Please enter your amount: "))
        s1 = Product(product, price,amount)
        self.products.append(s1)

    def show_products(self):
        count = 0
        for product in self.products:
            count += 1
            print(f"{count}. {product.name}  {product.price}$   {product.amount}")

    def get_user(self,user_name1):
        for user1 in self.users:
            if user1.user_name == user_name1:
                return user1
        return None

    def remove_user(self):
        self.print_users()
        a = int(input("Which user do you want to remove?: "))-1
        try:
            self.users.pop(a)
        except:
            print("Sorry, the user doesn't exist")

    def remove_product(self):
        self.show_products()
        a = int(input("Which product do you want to delete?: "))-1
        try:
            self.products.pop(a)
        except:
            print("Sorry, the product doesn't exist")

    def add_korzinka(self, user_name, product_name, product_price, product_amount):
        for user in self.users:
            if user.user_name == user_name:
                for product in user.korzinka:
                    if product.name == product_name and product.price == product_price:
                        product.amount += product_amount
                        return
                new_p = Product(product_name, product_price,product_amount)
                user.korzinka.append(new_p)
                return

        print("User topilmadi!")

    def check_product_user(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                file_name = f"receipt_{user_name}.pdf"
                c = canvas.Canvas(file_name, pagesize=A4)
                width, height = A4
                y = height - 50
                c.setFont("Helvetica-Bold", 16)
                c.drawString(50, y, f"Receipt for {user.user_name}")
                y -= 30
                c.setFont("Helvetica", 12)
                c.drawString(50, y, f"Email: {user.email}   Phone: {user.phone}")
                y -= 20
                c.drawString(50, y, "-" * 70)
                y -= 20
                total = 0
                for i, product in enumerate(user.korzinka, 1):
                    line_total = product.price * product.amount
                    c.drawString(50, y, f"{i}. {product.name}  {product.price}$ x {product.amount} = {line_total}$")
                    total += line_total
                    y -= 20
                    if y < 60:
                        c.showPage()
                        y = height - 50
                c.drawString(50, y, "-" * 70)
                y -= 20
                c.setFont("Helvetica-Bold", 12)
                c.drawString(50, y, f"Total: {total}$")
                y -= 20
                c.drawString(50, y, f"Your balance: {user.balance}$")
                y -= 40
                c.drawString(50, y, "Thank you for shopping!")
                c.save()
                print(f"PDF successfully created: {file_name}")
                return


    def shopping(self,user_name):
        count = 0
        for pr in self.products:
            count += 1
            print(f"{count}. {pr.name} : {pr.price}$  {pr.amount} kg available")
        try:
            a = int(input("Please enter the product id: "))
            b = int(input("Please enter your amount: "))
            if b > self.products[a-1].amount:
                print("Sorry, the product amount is not available")
            else:
                s1 = Product(self.products[a-1].name, self.products[a-1].price,b)
                self.add_korzinka(user_name, s1.name, s1.price, s1.amount)
                print("Accepted")
        except:
            print("Sorry, the product doesn't exist")

    def view_korzinka(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                count = 0
                for pr in user.korzinka:
                    count += 1
                    print(f"{count}. {pr.name} : {pr.price} {pr.amount}")


    def change_user_admin(self):
        a = -1
        self.print_users()
        user_id = int(input("Please enter your id: "))
        try:
            a = self.users[user_id-1]
            a.user_name = input("Please enter your name: ")
            a.email = input("Please enter your email: ")
            a.phone = input("Please enter your phone: ")
            a.password = input("Please enter your password: ")
            a.balance = int(input("Please enter your balance: "))
        except:
            print("Wrong user id")


    def change_product_admin(self):
        self.show_products()
        product_id = int(input("Please enter your product id: "))
        b = self.products[product_id-1]
        b.name = input("Please enter your name: ")
        b.price = input("Please enter your price: ")
        b.amount = int(input("Please enter your amount: "))

    def clean_korzinka_user(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                user.korzinka.clear()
                print("Korzinka cleaned successfully!")

    def login(self,user_name,password):
        for user1 in self.users:
            if user1.user_name == user_name and user1.password == password:
                if not user1.is_admin:
                    return 2
                else:
                    return 1

        return 0

    def edit_profile_user(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                user.user_name = input("Please enter your new username: ")
                user.email = input("Please enter your new email: ")
                user.phone = input("Please enter your new phone: ")
                user.password = input("Please enter your new password: ")

    def sum(self,user_name):
        summa = 0
        for user in self.users:
            if user.user_name == user_name:
                for pr in user.korzinka:
                    summa += pr.amount * pr.price
        return summa

    def buy(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                print(f"Your balance is {user.balance}")
                print(f"Products cost total is {self.sum(user_name)}")
                if user.balance < self.sum(user_name):
                    print("Not enough balance")
                elif self.sum(user_name) == 0:
                    print("There is nothing to buy")
                else:
                    for pr in user.korzinka:
                        for prod in self.products:
                            if prod.name == pr.name:
                                if prod.amount < pr.amount:
                                    print("Not enough products!")
                                    return
                                prod.amount -= pr.amount
                    print("Purchase was successful")
                    user.balance = user.balance - self.sum(user_name)
                    print(f"Your balance is {user.balance}")
                    self.check_product_user(user_name)
                    a = f"{user_name} purchased successfully!"
                    for pr in user.korzinka:
                        a += f"{pr.name} {pr.amount} {pr.price}"
                        a += f" cost: {pr.amount*pr.price}"
                    a+= f"{self.sum(user_name)}"
                    user.history.append(a)
                    self.clean_korzinka_user(user_name)

    def insert_money_user(self,user_name):
        for user1 in self.users:
            if user1.user_name == user_name:
                add = int(input("Please enter how much money you want to add: "))
                user1.balance += add
                print(f"Your balance is {user1.balance}")

    def edit_product_user(self,user_name):
        for user in self.users:
            if user.user_name == user_name:
                self.show_products()
                a = int(input("Please enter your product id: "))
                try:
                    pr = user.korzinka[a-1]
                    while True:
                        print(pr.name, pr.price ,"$", pr.amount, "kg")
                        a = input(" 1.add\n 2.subtract\n 3.exit\n")
                        if a == "1":
                            pr.amount += 1
                        elif a == "2":
                            pr.amount -= 1
                        elif pr.amount == 0:
                            user.korzinka.clear()
                        else:
                            break
                except:
                    print("Wrong product id")

    def print_user_history(self):
        self.print_users()
        a = int(input("Please enter user id: "))
        user = self.users[a]
        for hs in user.history:
            print(f"user bought {hs}")


s = Manager()
admin = User('Admin','','123','1111',0)
admin.is_admin = True
s.users.append(admin)
user1 = User('User1','','123','1111',1000)
s.users.append(user1)
user2 = User('User2','','123','1111',1000)
s.users.append(user2)


def Main(m:Manager):
    while True:
        a = input(" 1.Login\n 2.Create new account\n--->")
        if a == "1":
            print("*"*30)
            print("Welcome to Korzinka!")
            user_name = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if m.login(user_name,password) == 1:  #admin ----------- menu
                while True:
                    print("="*30)
                    print("Welcome Admin!")
                    a = input(" 1.add menu\n 2.print menu\n 3.edit menu\n 4.delete menu\n 5.exit\n--->")
                    if a == "1":
                        while True:
                            b = input(" 1.add product\n 2.exit")
                            if b == "1":
                                m.add_product()
                            else:
                                break
                    elif a == "2":
                        while True:
                            b = input(" 1.print users\n 2.print products\n 3.print user history\n 3.exit\n--->")
                            if b == "1":
                                m.print_users()
                            elif b == "2":
                                m.show_products()
                            elif b == "3":
                                m.print_user_history()
                            else:
                                break
                    elif a == "3":
                        while True:
                            b = input(" 1.edit product\n 2.exit")
                            if b == "1":
                                m.change_product_admin()
                            else:
                                break
                    elif a == "4":
                        while True:
                            b = input(" 1.delete user\n 2.delete product\n 3.exit\n--->")
                            if b == "1":
                                m.remove_user()
                            elif b == "2":
                                m.remove_product()
                            else:
                                break
                    else:
                        break
            elif m.login(user_name, password) == 2:  #user-------menu
                while True:
                    print("-"*30)
                    print("Welcome User!")
                    a = input(" 1.Buy some products\n 2.View korzinka\n 3.Edit product\n 4.Buy \n 5.Clean korzinka\n 6.Edit profile\n 7.Insert money\n 8.Exit \n--->")
                    if a == "1":
                        m.shopping(user_name)
                    elif a == "2":
                        m.view_korzinka(user_name)
                    elif a == "3":
                        m.edit_product_user(user_name)
                    elif a == "4":
                        m.buy(user_name)
                    elif a == "5":
                        m.clean_korzinka_user(user_name)
                    elif a == "6":
                        m.edit_profile_user(user_name)
                    elif a == "7":
                        m.insert_money_user(user_name)
                    else:
                        break
            else:
                print("No user found !")
        elif a == "2":
            print(" Welcome to register program")
            m.add_user()

Main(s)
