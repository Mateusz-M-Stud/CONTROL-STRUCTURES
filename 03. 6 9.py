# Program to check if a name is a Polish female name

# Input the name
name = input('Enter name: ')

# Check if the name ends with "a"
if name[-1].lower() == 'a' or name == "Beatrycze":
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a Polish female name')
