#Nathan Hopkins
#Module 3 Lists and Functions Programming assignment

# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5 Capitalize the element in things that refers to a person and then print the list.
# Did it change the element in the list?
for i in range(len(things)):
    if "cinderella" in things[i]:
        things[i] = things[i].capitalize()
print(things)

# 7.6 Make the cheesy element of things all uppercase and then print the list.
for i in range(len(things)):
    if "mozzarella" in things[i]:
        things[i] = things[i].upper()
print(things)

# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
things = [item for item in things if "salmonella" not in item]
print(things)

# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.
def get_odds():
    for number in range(1, 10, 2):
        yield number

# Using a for loop to find and print the third value returned by the generator function
for count, value in enumerate(get_odds()):
    if count == 2:
        print("Third value returned by get_odds():", value)
        break
