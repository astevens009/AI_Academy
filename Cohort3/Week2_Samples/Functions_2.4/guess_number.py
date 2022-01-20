import random

# NOTE: Generating random numbers between 1-10. Using a constant for the upper limit in case we want to change it later

UPPER_LIMIT = 10

num = random.randrange(1, UPPER_LIMIT)

print("\nTEST: num = {}".format(num))

while True:
    guess = int(input("Greetings! Guess a number between 1 and {}\n(Enter -1 to end): ".format(UPPER_LIMIT)))
    if guess == -1:
        print("Good bye...")
        break
    elif guess == num:
        print("GOOD JOB! You guess it!\n")
        break
    elif guess < num:
        print("Too low. Try again.\n")
    elif guess > num:
        print("Too high. Try again.\n")
    