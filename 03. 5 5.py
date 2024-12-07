# Sums numbers entered by user and calculates the arithmetic mean
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number
    count += 1  # Track of valid numbers (other than 0)

if count > 0:
    x = total_sum / count #total sum divided by number of count var
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {x}")
else:
    print("No numbers were entered.")
