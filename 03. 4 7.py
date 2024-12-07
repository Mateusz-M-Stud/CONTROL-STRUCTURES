###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1, 10):
    if i % 2 != 0:  # Check if the number is odd
        continue
    sum += i  # Adding even numbers to the sum var

print(f'Sum of even numbers in the range <1,10> is {sum}')
