import random

secret_number = random.randint(0,10)

guess = int(input("Guess the secret number:"))

if secret_number == guess:
    print("you guessed it right")
elif secret_number < guess:
    print("Too low")
else:
    print("haha loser")