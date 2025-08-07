class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class store:
    def __init__(self):
        self.product_list = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.product_list.append(product)

    def show_products(self):
        print("\nProduct list:")
        for i, product in enumerate(self.product_list, start=1):
            print(f"{i}. {product.name} - {product.quantity} units")

my_store = store()
my_store.add_product("snacks", 10)
my_store.add_product("drinks", 5)
my_store.add_product("fruits", 20)
my_store.add_product("vegetables", 15)
my_store.show_products()