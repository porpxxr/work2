class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name 
        self.description = description
        self.price = price
        self.online_shop = online_shop

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.orders = []

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []
    
    def additemtocart(self, customer , product, quantity):
        customer.cart.append({"product": product, "quantity": quantity})
    
    def checkout(self, customer):
        oreder_id = f"ORD-{len(customer.orders) + 1}"
        total = sum(item['product'].price * item['quantity'] for item in customer.cart)
        order = {
            "order_id": oreder_id,
            "items": customer.cart,
            "total": total
        }
        customer.orders.append(order)
        customer.cart.clear()
        print(f"Order {oreder_id} placed successfully! Total: ${total:.2f}")

    def ordertracking(self, customer, order_id):
        for order in customer.orders:
            if order['order_id'] == order_id:
                print(f"Order ID: {order['order_id']}")
                for item in order['items']:
                    print(f"{item['product'].name} - {item['quantity']} units")
                print(f"Total: ${order['total']:.2f}")
                return
        print("Order not found.")

shop = OnlineShop("My Online Shop", "www.myonlineshop.com")
customer = Customer("John Doe", "asdf@example.com", "123 Main St")
p1 = Product("Laptop", "High performance laptop", 1200.00, shop)
p2 = Product("Smartphone", "Latest model smartphone", 800.00, shop)
shop.additemtocart(customer, p1, 1)
shop.additemtocart(customer, p2, 2)
shop.checkout(customer)
shop.ordertracking(customer, "ORD-1")