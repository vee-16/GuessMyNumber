import random
import sys

def game(numToGuess, tries):
    print(numToGuess)
    while tries > 0:
        try:
            user = int(input("Your guess: "))
            if user not in range(1,100):
                user = int(input("Please enter number in range 1-100: "))
        
            if user == numToGuess:
                print("You guessed correctly! The number was %d." %(numToGuess))
                return
            elif user < numToGuess:
                tries -=1
                print("Guess higher. You have %d tries remaining." %(tries))
            elif user > numToGuess:
                tries -=1
                print("Guess lower. You have %d tries remaining." %(tries))
        except:
            print("Invalid. Enter a number between 1-100: ")


    print("Sorry you ran out of tries.")
                

if __name__ == '__main__':
    while True:    
        print(("Welcome to the 'Guess My Number' Game!").center(75))
        print("\nTry to guess the number I'm thinking of between 1 - 100")
        print("You have 5 tries.")
        game(random.randint(1,100), 5)

        play = input("Would you like to play again? (y or n): \n").lower()

        while play not in {'y', 'n'}:
            play = input("Please enter (y or n): ")

            if play == 'n':
                print("See you later!")
                sys.exit()

        
