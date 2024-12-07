###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively.
#
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    print('Invalid driving mode')
    fuel_consumption = 0

total_consumption = (fuel_consumption / 100) * distance
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.2f} liters')
