"""Write a function called greater_than that takes two integer inputs, x and y and
returns the value that is greater. If x and y are equal, return the string"""


def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


"""The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 
credits to graduate. Write a function called graduation_reqs that takes an input credits and checks if the student 
has enough credits to graduate. """


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


"""
Call graduation_reqs with an input of 120 credits and print the result to the terminal. 
Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?"""
print(graduation_reqs(120))

"""Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need 
to have a GPA of 2.0 or higher. Rewrite the graduation_reqs function so it takes two inputs, gpa and credits, 
and checks to see if a student meets both requirements using an and statement. """

# def graduation_reqs(gpa, credits):
#     if (credits >= 120) and (gpa >= 2.0):
#         return "You meet the requirements to graduate!"

"""They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and 
not statements. """


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    if not (gpa >= 2.0) and not (credits >= 120):
        return "You do not meet either requirement to graduate!"


"""Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades over GPA numbers. They want 
you to write a function called grade_converter that converts an inputted GPA into the appropriate letter grade. Your 
function should be named grade_converter, take the input gpa, and convert the following GPAs: 

4.0 or higher should return "A"
3.0 or higher should return "B"
2.0 or higher should return "C"
1.0 or higher should return "D"
0.0 or higher should return "F"
You can do this by creating a variable called grade.

Then, you should use elif statements to set grade to the appropriate letter grade for the gpa entered.

At the end of the function, return grade."""


def grade_converter(gpa):
    grade = "F"

    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"

    return grade
