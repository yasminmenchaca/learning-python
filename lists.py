names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(list(names_and_dogs_names))

orders = ['daisies', 'periwinkle']
orders.append('tulips')
orders.append('roses')

print(orders)

orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac', 'iris']
# Fix the command by inserting brackets ([ and ]) so that it will run without errors.
broken_prices = [5, 3, 4, 5, 4] + [4]

# Modify list1 so that it is a range containing numbers starting at 0 and up to, but not including, 9.
list1 = range(9)

# Create a range called list2 with the numbers 0 through 7.
list2 = range(8)

"""
Modify the range function that created list1 such that it:
Starts at 5
Has a difference of 3 between each item
Ends before 15 (start, ends before, difference)
"""
list1 = range(5, 15, 3)

"""
Create a range object called list2 that:

Starts at 0
Has a difference of 5 between each item
Ends before 40 (start, ends before, difference)
"""
list2 = range(0, 40, 5)

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
# Create an empty list called age.
age = []
# Depak’s age is 42. Use .append() to add 42 to age.
age.append(42)
# Create a new list called all_ages that adds age with the following list, containing the ages for Ainsley, Ben,
# and Chani
all_ages = [32, 41, 29] + age
# Create a new variable called name_and_age that combines first_names and all_ages using zip
name_and_age = zip(first_names, all_ages)
# Create a range object called ids with an id number for each customer. Since there are 4 customers, so id values
# should go from 0 to 3
ids = range(4)
