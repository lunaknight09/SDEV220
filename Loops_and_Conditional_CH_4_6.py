#Nathan Hopkins
#Module 2 Loops and Conditionals
#Jan 25,2023

# 4.1
secret = 7  # You can choose any number between 1 and 10
guess = 4   # You can choose any number between 1 and 10

if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
else:
    print('Just right')

# 4.2
small = True   # Assign True or False
green = False  # Assign True or False

if small and green:
    print('Match: pea')
elif small and not green:
    print('Match: cherry')
elif not small and green:
    print('Match: watermelon')
else:
    print('Match: pumpkin')

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
