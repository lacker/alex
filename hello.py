# This is a Number game.
import random

guessesTaken = 0

print("Hello! What is your name?")
myName = input()

top = 100
number = random.randint(1, top)
print(f"Well, {myName}, I am thinking of a number between 1 and {top}.")

for guessesTaken in range(10000):
    print("Take a guess.")  # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")  # There are eight spaces in front of print.

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(
        "Good job, "
        + myName
        + "! You guessed my number in "
        + guessesTaken
        + " guesses!"
    )

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")
