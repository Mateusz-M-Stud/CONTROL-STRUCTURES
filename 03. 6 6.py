hours_parked = int(input("Enter the number of hours the car was parked: "))


if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0  # If less than 1 hour, no fee

print(f"The parking fee is: {fee} PLN")
