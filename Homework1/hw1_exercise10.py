'''
4. Random Number Guessing Game
Write a program that generates a random number in the range of 1 through 100, and asks the
user to guess what the number is. If the user’s guess is higher than the random number, the
program should display “Too high, try again.” If the user’s guess is lower than the random
number, the program should display “Too low, try again.” If the user guesses the number, the
application should congratulate the user and generate a new random number so the game can
start over.

Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
user makes. When the user correctly guesses the random number, the program should display
the number of guesses.

>> python hw1_exercise10.py
Enter number between 1 to 100: hello_world
Enter number between 1 to 100: 50
Too low, try again.
Enter number between 1 to 100: 80
Congratulations you did it in  2  try
Do you want to continue (y/n): y
Enter number between 1 to 100: 50
Too high, try again.
Enter number between 1 to 100: 30
Too high, try again.
Enter number between 1 to 100: 10
Too low, try again.
Enter number between 1 to 100: 20
Too high, try again.
Enter number between 1 to 100: 15
Congratulations you did it in  5  try
Do you want to continue (y/n): n
'''
import random

class GuessingGame:
    __min = 1
    __max = 100

    def __init__(self):
        self.guess_number = random.randint(self.__min, self.__max)
        self.user_number = 0
        self.count = 0

    def guessNumber(self):
        while (self.guess_number != self.user_number):
            try:
                self.user_number = int(input("Enter number between {} to {}: ".format(self.__min, self.__max)))
                self.count += 1
                if (self.user_number > self.guess_number):
                    print("Too high, try again.")
                elif (self.user_number < self.guess_number):
                    print("Too low, try again.")
            except Exception:
                continue

def main():
    while True:
        g = GuessingGame()
        g.guessNumber()
        print("Congratulations you did it in ", g.count, " try")
        if input("Do you want to continue (y/n): ") != "y":
            break

if __name__ == "__main__":
    main()
