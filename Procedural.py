product_list = []

def add_product(product_list, name, quantity):
    product = {"name": name, "quantity": quantity}
    product_list.append(product)

def show_product(product_list):
    print("\nProduct list:")
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. {product['name']} - {product['quantity']} units")

add_product(product_list, "snacks", 10)
add_product(product_list, "drinks", 5)
add_product(product_list, "fruits", 20)
add_product(product_list, "vegetables", 15)
show_product(product_list)