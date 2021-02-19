import random
from game import Game

print("Welcome to the command line verison of the Mastermind game. There are 6 colors in total - r, g, b, y, w, p. On the easy level only one of each can be chosen, on the hard level they can be chosen multiple times.")

level = input("Please choose a level (easy/hard): ")

#initiate game
game_on = True

game = Game()

game.initiate(level)


#play game while player wins or runs out of tries
while game_on:
    print(game.solution)
    #TODO error handling for user input
    guess_text = input("Make a guess (eg. r-g-b-y): ")
    guess = guess_text.split("-")

    print(game.evaluate_guess(guess))

    game_on = not game.evaluate_game()