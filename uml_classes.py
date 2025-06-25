class UserModel:
    def __init__(self):
        self.username = ""
        self.password = ""

class UserController:
    def __init__(self):
        self.model = UserModel()

    def login(self, username, password):
        return self.model.username == username and self.model.password == password

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemController:
    def __init__(self):
        self.items = []

    def create_item(self, name, price):
        item = Item(name, price)
        self.items.append(item)
        return item