###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
jacket_time = 40 
underwear_time = 70
shoes_time = 20 

# Additional times for extra rinse and extra spin
rinse_time = 15
spin_time = 9

total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower() # Function lower to prevent errors withupper strings
extra_rinse = input('Extra rinse? (y/n): ').lower()
extra_spin = input('Extra spin? (y/n): ').lower()

# Determine washing time based on program selected
if program == 'j':
    total_washing_time += jacket_time
elif program == 'u':
    total_washing_time += underwear_time
elif program == 's':
    total_washing_time += shoes_time
else:
    print("Invalid program selected.")
    exit()

# Add additional times if applicable
if extra_rinse == 'y':
    total_washing_time += rinse_time
if extra_spin == 'y':
    total_washing_time += spin_time

print(f"Total washing time: {total_washing_time} minutes")
