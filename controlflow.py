"""Write a function called greater_than that takes two integer inputs, x and y and
returns the value that is greater. If x and y are equal, return the string"""


def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


"""The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate. 
Write a function called graduation_reqs that takes an input credits and checks if the student has enough credits to graduate."""


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


"""
Call graduation_reqs with an input of 120 credits and print the result to the terminal. 
Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?"""
print(graduation_reqs(120))
