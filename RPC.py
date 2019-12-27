

import random
moves = ['rock', 'paper', 'scissors']

my_move = 0
their_move = 0

class Player:
    def move(self):
        return 'rock'
    def learn(self, my_move, their_move):
        return my_move, their_move
    def beats(self, one, two):
            p1_score = 0
            p2_score = 0
        if one == two:
            print("It's a tie!")
        elif ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
            print("Player one won this round")
            p1s += 1
            print(p1s, p2s)
            return p1s, p2s
        else:
            print("Player two won this round")
            p2s += 1
            print(p1s, p2s)
            return p2s, p2s
        return p1s, p2s
class Human(Player):
    def move(self):
        my_move = input("What is your Play?").lower()
        while my_move not in moves:
            my_move = input("Your move has to be either rock, paper or scissors.")
        return my_move
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player): 
    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move

class CyclerPlayer(Player):
    def move(self):
        if my_move == "rock":
            return "paper"
        elif my_move == "papaer":
            return "scissors"
        elif my_move == "scissors":
            return "rock"
        else:
            return "rock"
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # global p1s, p2s
        self.p1s = 0
        self.p2s = 0
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.p1.beats(move1, move2)
    def play_game(self):
        print("Game start!")
        rounds = int(input("Do you feel luck? How many rounds do you want to play?"))
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"The score is {self.p1s} to {self.p2s}")
        if self.p1s > self.p2s:
            print("Player 1 one the game, congratulations!!")
        elif self.p1s < self.p2s:
            print("Player 2 one the game, congratulations!!")
        else:
            print("It's a draw...")

    print ("Player: " + str(my_move))
    print ("Computer: " + str(their_move))
            
if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.play_game()
