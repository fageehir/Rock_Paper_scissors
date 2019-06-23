# Rock Paper Scissors Game Project.
# Written by: Ibrahim Al-Fageeh.

import random

moves = ["rock", "paper", "scissors"]


class player():
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass


class RockPlayer(player):  # rock only move class.
    def move(self):
        play = moves[0]
        return (play)


class randomplay(player):  # random move class.
    def move(self):
        play = random.choice(moves)
        return (play)


class mimic(player):  # starts with rock then mimics players moves
    def __init__(self):
        player.__init__(self)
        self.learn_moves = moves[0]

    def move(self):
        if self.learn_moves is None:
            play = moves[0]
        else:
            play = self.learn_moves
            return (play)

    def learn(self, learn_moves):
        self.learn_moves = learn_moves


class predicted_play(player):  # this class playin predicted sequence
    def __init__(self):
        player.__init__(self)
        self.step = 0

    def move(self):
        play = None
        if self.step == 0:
            play = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            play = moves[1]
            self.step = self.step + 1
        else:
            play = moves[2]
            self.step = self.step + 1
        return play


class human_player(player):
    def move(self):
        play = input("rock, paper or scissors ? >").lower()

        while play != "rock" and play != "paper" and play != "scissors":
            print("wrong input! Try Again")
            play = input("rock, paper or scissors ? >").lower()

        return (play)


class game():
    def __init__(self, p2):
        self.p1 = human_player()
        self.p2 = p2

    def play_game(self):
        print("Rock, paper scissorrs, GO!")
        for round in range(3):
            print(f"Round{round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("player 1 win!!")
        elif self.p1.score < self.p2.score:
            print("Player 2 win!!")
        else:
            print("Tie")
        print("The final score is " + str(self.p1.score) + " to " +
              str(self.p2.score))

    def play_single(self):  # Single Round Class
        print("rock Paper Scissors, Go!")
        print(f"round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print("player 1 wins")
        elif self.p1.score < self.p2.score:
            print("Player 2 wins")
        else:
            print("Tie")
        print("The Final Score is " + str(self.p1.score) + " to " +
              str(self.p2.score))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play(self, move1, move2):
        print(f"you played {move1}")
        print(f"opponent played {move2}")
        if beats(move1, move2):
            print("******__Player One Wins__******")
            print(f"Score: Player 1: {move1} Player 2: {move2}\n\n")
            self.p1.score += 1
            return 1
        elif beats(move2, move1):
            print("******__Player Two Wins__******")
            print(f"score: Player 1: {move1} Player 2: {move2}\n\n")
            self.p2.score += 1
            return 2
        else:
            print("Game Tie")
            print(f"score: Player 1: {move1} Player 2: {move2}\n\n")
            return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == "__main__":
    answer = [RockPlayer(), randomplay(), mimic(), predicted_play()]
    p2 = input("Select the RPS game you would like to play or hit any\
        key then enter for random game: [1]Rock, [2]Random,\
            [3]Reflective, or [4]Cycles: >")

    if p2 == "1":
        p2 = RockPlayer()
    elif p2 == "2":
        p2 = randomplay()
    elif p2 == "3":
        p2 = mimic()
    elif p2 == "4":
        p2 = predicted_play()
    else:
        p2 = randomplay()

    rounds = input("Select game mode, [s]inglegame or [f]ull game: >").lower()
    game = game(p2)
    while True:
        if rounds == "s":
            game.play_single()
            break
        elif rounds == "f":
            game.play_game()
            break
        else:
            print("wrong input! Try Again")
            rounds = input(" Enter [s] for a single\
                game or [f] for a full game: >")
