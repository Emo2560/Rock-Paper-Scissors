

"""The Player class is the parent class for all of the Players
in this game"""

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
moves = ['rock', 'paper', 'scissors']

my_move = 0
their_move = 0

class Player:
    def move(self):
        return 'rock'
    def learn(self, my_move, their_move):
        return my_move, their_move
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
class Human(Player):
    def move(self):
        my_move = input("What is your Play rock, paper, scissors?").lower()
        while my_move not in moves:
            my_move = input("Your move has to be either rock, paper or scissors.")
        return my_move
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player): 
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move
        
class Cycler(Player):
    def __init__(self,):
        self.my_move = None
    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
            return self.my_move
        elif self.my_move == "rock":
            self.my_move = "paper"
            return self.my_move
        elif self.my_move == "paper":
            self.my_move = "scissors"
            return self.my_move
        else:
            self.my_move = "rock"
            return self.my_move 
        
    def learn(self, my_move, their_move):
        pass
        
                
class Game:
    p1_score = 0
    p2_score = 0
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
                
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        #self.p2.learn(move1,move2)
        #self.p2.learn(move2,move1)
        print(f"Player 1: {move1}")
        print(f"Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 won!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 won!")
        else:
            print("Tie!!!")
        print("Current scores: ")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")



        
    def play_game(self):
        print("Game start!")
        for round in [1, 2, 3]:
            print(f"Round{round}:")
            self.play_round()
        print("General scores:")
        print(f"Final score: Player 1: {self.p1_score}\tPlayer 2: {self.p2_score}")
        
        #print(f"Player 1: {self.p1_score}")
        #print(f"Player 2: {self.p2_score}")
        #if self.p1_score < self.p2_score:
            #print("Player 2 won ")
        #elif self.p1_score > self.p2_score:
            #print("Player 1 won")
        #else:
            #print("TIE")
        print("Game over")
        

    print ("Player: " + str(my_move))
    print ("Computer: " + str(their_move))
            
if __name__ == '__main__':
    game = Game(Human(), Cycler())
    game.play_game()

