"""
In script.py, we have made a function for you called sing_song. Call this function once to see what it prints out.
Now call sing_song a second time.
"""


def sing_song():
    print("You may say I'm a dreamer")
    print("But I'm not the only one")
    print("I hope some day you'll join us")
    print("And the world will be as one")


# call sing_song() below:
sing_song()
sing_song()

"""
Write a function called loading_screen that prints "This page is loading..." to the console.
Outside of the function body (unindented), call loading_screen().
"""


def loading_screen():
    print("This page is loading...")


loading_screen()

"""
Remove the indent on the second print statement. Run the file. Now what’s printed?
"""


def about_this_computer():
    print("This computer is running on version Everest Puma")


print("This is your desktop")

about_this_computer()

"""
Call calculate_age with values 2049 (current_year) and 1953 (birth_year) and save the value to a variable called 
dads_age. Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is 
and dads_age where the Y is. 
"""


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")

"""
Write a function called get_boundaries() that takes in two parameters, a number called target and a number called 
margin. It should create two variables: low_limit: target minus the margin high_limit: margin added to target Return 
both low_limit and high_limit from the function, in that order. Call the function on the target 100 with a margin of 
20. Save the returned values to variables called low and high. 
"""


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit


low, high = get_boundaries(100, 20)

"""
functions review
"""


def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats


things_one = repeat_stuff("Row ", 3)
things_two = "Your Boat. "

lyrics = things_one + things_two

song = repeat_stuff(lyrics)

print(song)

"""Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power."""


# Write your tenth_power function here:
def tenth_power(num):
    return num ** 10


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

"""Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num."""


# Write your square_root function here:
def square_root(num):
    return num ** 0.5


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


"""Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers."""


# Write your win_percentage function here:
def win_percentage(wins, losses):
    total = wins + losses
    return (100 * wins) / total


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

"""Write a function named average() that has two parameters named num1 and num2.

The function should return the average of these two numbers."""


# Write your average function here:
def average(num1, num2):
    return (num1 + num2) / 2


# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

"""Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2."""


# Write your remainder function here:
def remainder(num1, num2):
    return (2 * num1) % (num2 / 2)


# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

"""Write a function named first_three_multiples() that has one parameter named num.

This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21."""


# Write your first_three_multiples function here
def first_three_multiples(num):
    for i in range(1, 4):
        print(num * i)
    return num * i


first_three_multiples(7)

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
"""Create a function called tip() that has two parameters named total and percentage.

This function should return the amount you should tip given a total and the percentage you want to tip.
"""


# Write your tip function here:
def tip(total, percentage):
    return total * percentage / 100


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

"""Write a function named introduction() that has two parameters named first_name and last_name.

The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name."""


# Write your introduction function here:
def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name


# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

"""Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. 
Write a function named dog_years() that has two parameters named name and age."""


# Write your dog_years function here:
def dog_years(name, age):
    dog_age = age * 7
    return name + ", you are " + str(dog_age) + " years old in dog years"


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

"""Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. 
The function should print 3 lines and return 1 value.
First, print the sum of a and b.
Second, print d subtracted from c.
Third, print the first number printed, multiplied by the second number printed.
Finally, return the third number printed mod a."""


# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
    operation1 = a + b
    operation2 = d - c
    operation3 = operation1 * operation2
    print(operation1)
    print(operation2)
    print(operation3)
    return operation3 % a


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
