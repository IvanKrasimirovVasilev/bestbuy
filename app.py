from flask import Flask, render_template, request, redirect

import products
import store


app = Flask(__name__)

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)

cart = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def show_products():
    return render_template(
        "products.html",
        products=best_buy.get_all_products()
    )


@app.route("/product/<int:product_id>")
def show_product(product_id):
    active_products = best_buy.get_all_products()

    if product_id < 0 or product_id >= len(active_products):
        return "Product not found", 404

    selected_product = active_products[product_id]

    return render_template(
        "product.html",
        product=selected_product
    )


@app.route("/buy", methods=["POST"])
def buy():
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])

    for product in best_buy.get_all_products():
        if product.name == product_name:
            product.buy(quantity)
            cart.append((product, quantity))
            break

    return redirect("/cart")

@app.route("/cart")
def show_cart():
    total_price = 0

    for product, quantity in cart:
        total_price += product.price * quantity

    return render_template(
        "cart.html",
        cart=cart,
        total_price=total_price
    )


if __name__ == "__main__":
    app.run(debug=True)