###
# Credit card payment
#
account_balance = 500
total_payment = int(input('Enter the total value of purchases: '))

if total_payment <= account_balance:  # Check if the payment can be covered by the account balance
    print('Payment completed')
else:
    print('No funds')
