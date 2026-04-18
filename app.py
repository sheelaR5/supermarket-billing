from flask import Flask, render_template

app = Flask(__name__)


class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Bill:
    def __init__(self, bill_id, customer, product, quantity):
        self.bill_id = bill_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_amount = product.price * quantity

@app.route("/")
def home():
    customer = Customer(1, "Sheela", "9876543210")
    product = Product(1, "Rice", 50)
    bill = Bill(1, customer, product, 2)

    return render_template("index.html", bill=bill)


if __name__ == "__main__":
    app.run(debug=True)
