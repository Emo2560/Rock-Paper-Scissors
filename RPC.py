

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
    def beats(self, one, two):
        p1s = 0
        p2s = 0
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
        my_move = input("What is your rock, paper, or scissors?").lower()
        while my_move not in moves:
            my_move = input("Your move has to be either rock, paper or scissors.")
        return my_move
                
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None
     
    def play(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move
class Cycle(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        index = moves.index(self.my_move) + 1
        if index % len(moves) == 0:
            index = 0
        return moves[index]
    def learn(self, my_move, their_move):
        self.my_move = my_move

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

    def game_selection(self):
        while True:
                select = int(input("Select the strategy "
                "you want to play against:  "
                "1 - Rock Player "
                "2 - Random Player "
                "3 - Cycle Player "
                "4 - Reflect Player: "))
                if select == 1:
                    selection = "Player()"
                elif select == 2:
                    selection == "RandomPlayer()"
                elif select == 3:
                    selection = "CyclePlayer()"
                else:
                    selection = "ReflectPlayer()"
 
                print("!!!", selection)
                if select not in range (1,4):
                    print("Error - Please select a # 1-4.")
 
                    continue
                return selection
                



            
if __name__ == '__main__':
    d = {
         1: Player(),
         2: RandomPlayer(),
         3: Human(),
         4: Cycle()
    }
    chooseplayer = int(input("Choose your player: 1, 2, 3 or 4\n"))
    opponent = d[chooseplayer]
    you = Human()


   
    game = Game(Human(), RandomPlayer())
    game.play_game()
