"""In script.py, we have made a function for you called sing_song. Call this function once to see what it prints out.

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

"""Write a function called loading_screen that prints "This page is loading..." to the console.
Outside of the function body (unindented), call loading_screen()."""


def loading_screen():
    print("This page is loading...")


loading_screen()

"""Remove the indent on the second print statement. Run the file. Now what’s printed?"""


def about_this_computer():
    print("This computer is running on version Everest Puma")


print("This is your desktop")

about_this_computer()

"""Call calculate_age with values 2049 (current_year) and 1953 (birth_year) and save the value to a variable called 
dads_age. Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is 
and dads_age where the Y is. """


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")

"""Write a function called get_boundaries() that takes in two parameters, a number called target and a number called 
margin. It should create two variables: low_limit: target minus the margin high_limit: margin added to target Return 
both low_limit and high_limit from the function, in that order. Call the function on the target 100 with a margin of 
20. Save the returned values to variables called low and high. """


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit


low, high = get_boundaries(100, 20)
