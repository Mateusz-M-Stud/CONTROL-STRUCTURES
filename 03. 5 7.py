###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time
words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

# Take input for countdown time
countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown <= 5:
        print(words[countdown]) # Adding words to last 5 sec
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)

print("Time's up!")
