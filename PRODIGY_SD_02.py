'''
    Create a guessing game:
    Build a program that generates a random number and challenges the user to guess it. 
    The program should prompt the user to input their guess, compare it to the generated number, 
    and provide feedback if the guess is too high or too low. It should continue until the user 
    correctly guesses the number and then display the number of attempts it took to win the game.
'''
import random

def main():
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    guess = 0
    attempts = 0

    while guess != random_number:
        attempts += 1
        print(f"\nRound No. {attempts}")
        guess = int(input("Enter your guess (between 1 and 100): "))

        if guess < random_number:
            print("The number you entered is too low compared to the random number. Try again.")
            print("Let's move on to the next round.")
        elif guess > random_number:
            print("The number you entered is too high compared to the random number. Try again.")
            print("Let's move on to the next round.")
        else:
            print("Congratulations! You've guessed the number.")
            print(f"It took you {attempts} attempts.")

if __name__ == "__main__":
    main()

