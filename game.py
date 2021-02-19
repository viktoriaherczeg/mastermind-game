import random

COLORS = ["r", "b", "g", "y", "w", "p"]
TRIES = 8
FIELDS = 4

class Game():
    def __init__(self):
        self.solution = []
        self.tries = TRIES
        self.evaluation = {"color": 0, "position": 0}


    def initiate(self, level):
        ''' Creates the solution based on the chosen level. easy - only one of each colors, hard - one color can be chosen multiple times '''
        if level == "easy":
            color_set = COLORS.copy()
            for i in range(FIELDS):
                color = random.choice(color_set)
                color_set.remove(color)
                self.solution.append(color)
        else:
            for i in range(FIELDS):
                self.solution.append(random.choice(COLORS))

    
    def evaluate_guess(self, guess):
        ''' Counts how many colors are matching and how may of them are in the correct position. '''
        correct_color = 0
        correct_position = 0
        for i in range(FIELDS):
            if guess[i] == self.solution[i]:
                correct_position += 1

        solution_elements = self.solution.copy()
        for i in range(FIELDS):
            if guess[i] in solution_elements:
                correct_color +=1
                solution_elements.remove(guess[i])
        
        self.evaluation["color"] = correct_color
        self.evaluation["position"] = correct_position
        return self.evaluation

    def evaluate_game(self):
        ''' Returns true if all colors are matching and are at the correct position, if not returns false.'''
        self.tries -= 1
        
        if self.evaluation["color"] == FIELDS and self.evaluation["position"] == FIELDS:
            print("Good job, you have won the game!")
            return True
        elif self.tries == 0:
            print("You are out of guesses.")
            return True
        else:
            print("You have x guess(es) left.")
            return False