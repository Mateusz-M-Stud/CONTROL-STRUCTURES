ean_number = input("Enter EAN-13 article number: ")

# Check EAN number consists 13 digits
if len(ean_number) == 13 and ean_number.isdigit():
    print("Article number is correct")
    
    # Check if the product is manufactured in Poland (590)
    if ean_number.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid EAN-13 article number")
