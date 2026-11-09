def start_cart():
    cart = []
    def prod_cart(product_name, price):
        nonlocal cart
        cart.append({"name":product_name, "price":price})
        return cart
        
    def total_cost():
        nonlocal cart
        return sum(item["price"] for item in cart)
    return prod_cart, total_cost
        

prod_cart, total_cost = start_cart()
prod_cart("rice", 2000)
prod_cart("beans", 3000)

print("Total cost:#",total_cost(), sep="")

