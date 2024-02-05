#Nathan Hopkins
#Module 2 Loops and Conditionals
#Jan 25,2023

import requirements.txt

# 4.1
# Choose a number between 1 and 10 and assign it to the variable secret
secret = 7

# Select another number between 1 and 10 and assign it to the variable guess
guess = 5

# Write the conditional tests
if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
else:
    print('Just right')


# 4.2
# Assign True or False to variables
small = True
green = True

# Fruits or vegetables
fruit_or_vegetable = "pea"

# Check if the fruit or vegetable is small and green
if fruit_or_vegetable == "pea":
    small = True
    green = True
elif fruit_or_vegetable == "cherry":
    small = True
    green = False
elif fruit_or_vegetable == "watermelon":
    small = False
    green = True
elif fruit_or_vegetable == "pumpkin":
    small = False
    green = False

# Print the results
print(f"{fruit_or_vegetable.capitalize()} is {'small' if small else 'not small'} and {'green' if green else 'not green'}.")

# 6.1
for value in [3, 2, 1, 0]:
    print(value)

# 6.2
guess_me = 7
number = 1

while number <= guess_me:
    if number < guess_me:
        print('Too low')
    elif number == guess_me:
        print('Found it!')
        break
    else:
        print('Oops')
        break
    number += 1

# 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('Too low')
    elif number == guess_me:
        print('Found it!')
        break
    else:
        print('Oops')
        break
