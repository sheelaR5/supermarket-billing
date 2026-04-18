from flask import Flask, render_template

app = Flask(__name__)

class Customer:
    def __init__(self, id, name, phone):
        self.name = name

class Product:
    def __init__(self, id, name, price):
        self.name = name
        self.price = price

class Bill:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_amount = product.price * quantity

@app.route("/")
def home():
    customer = Customer(1, "Sheela", "9876543210")
    product = Product(1, "Rice", 50)
    bill = Bill(customer, product, 2)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    

    return render_template("index.html", bill=bill)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
