class Product:
    def __init__(self,title,price,category):
        self.title = title
        self.price = price
        self.category = category
    def show(self):
        print(f"{self.title}|{self.price}|{self.category}")
        