import random

secret_number = random.randint(1, 100)
tries = 5

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {tries} tries.")

for attempt in range(1, tries + 1):
    try:
       guess = int(input(f"Try {attempt}/{tries}: Enter your guess: "))
    except ValueError:
       print("pleas enter a NUMBER, not text. you didn't lose a try.")
       continue
    if guess == secret_number:
        print("You win! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")
else:
    print(f"You lose! The number was {secret_number}.")
