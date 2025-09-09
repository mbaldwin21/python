"""
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward


"""


age = int(input("How old are you? "))

# Determine whether they are old enough to do certain activites
if age >= 16:
    print("You are old enough to drive.")
elif age < 16:
    print("You are not old enough to drive.")
if age >= 18:
    print("You are old enough to vote.")
elif age < 18:
    print("You are not old enough to vote.")
if age >= 21:
    print("You are old enough to legally buy alcohol.")
elif age < 21:
    print("You are not old enough to buy alcohol.")
if age >= 60:
    print("You are old enough for a senior discount.")
elif age < 60:
    print("You are not old enough for a senior discount.")