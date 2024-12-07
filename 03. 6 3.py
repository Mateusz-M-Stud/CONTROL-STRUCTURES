# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house

light_switch1 = False  # False - switch off, True - switch on
light_switch2 = False  # False - switch off, True - switch on
bulbs_on = 4

if light_switch1:
    bulbs_on += 1  # Switch 1 lights 1 bulb

if light_switch2:
    bulbs_on += 2  # Switch 2 lights 2 bulbs

print(f"Number of bulbs on: {bulbs_on}")
