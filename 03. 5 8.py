# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

def check_pin():
    # Function to check if entered PIN is correct
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print(f"Your PIN is {pin}")
    else:
        print("Incorrect PIN. Please try again.")

def change_pin():
    # Function to change the PIN
    global pin  # Use the global pin variable
    old_pin = input("Enter your current PIN: ")
    if old_pin == pin:
        new_pin = input("Enter a new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            pin = new_pin
            print("Your PIN has been changed successfully.")
        else:
            print("Invalid PIN format. The PIN should be a 4-digit number.")
    else:
        print("Incorrect current PIN. Cannot change PIN.")

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    if choice == "4":
        check_pin()
    if choice == "5":
        change_pin()   
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
        
    else:
        print("Invalid option. Please try again.")