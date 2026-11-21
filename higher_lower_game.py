
import random

print("Welcome to the Higher/Lower Game!")
print("I am thinking of a number between 1 and 10.")

play_again = "yes"

while play_again.lower() == "yes":

    secret_number = random.randint(1, 10)
    guess = 0

    while guess != secret_number:

        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                print("Congratulations! You guessed correctly!")
                print("Great job, Bella!")

        except ValueError:
            print("Please enter a whole number.")

    play_again = input("Would you like to play again? (yes/no): ")

print("Thanks for playing the Higher/Lower Game!")
