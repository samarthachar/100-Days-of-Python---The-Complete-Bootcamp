import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

num = random.randint(1,101)

running = True
while running:
    print(f"you have {guesses} attempts remaining to guess the number")
    inp = int(input("Make a guess: "))
    if inp == num:
        print(f"You got it! the answer was {num}.")
        running = False
    elif inp > num:
        print("Too high.")
    elif inp < num:
        print("Too low.")

    guesses -= 1
    if guesses == 0:
        running = False
        print("You've run out of guesses. Refresh the page to run again.")
    elif guesses > 0:
        print("Guess again.")