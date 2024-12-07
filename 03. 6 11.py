# Input current and previous product price
current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))

# Price decrease
price_decrease = ((previous_price - current_price) / previous_price) * 100

# Check if the price decreased by at least 10%
if price_decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(price_decrease)}%")
else:
    print("The price has not decreased enough to recommend buying.")
