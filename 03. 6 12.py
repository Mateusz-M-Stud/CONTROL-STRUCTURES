num_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the product price: "))

# Total cost before discount
total_cost = num_products * product_price

# 25% discount if more than two products are purchased
if num_products > 2:
    total_cost *= 0.75

print(f"Amount to pay: {total_cost:.2f}")
