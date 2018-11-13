from random import shuffle, randint
import unittest

class Game:

    GAME_END = 10000

    def __init__(self, players = []):
        print("hello")
        shuffle(players)
        self.players = players
        self.number_of_players = len(players)
        self.scores = [0 for player in players]
        self.current_player = 0
        self.prev_score = 0
        self.prev_dice_left = 0
        self.turn_number = 0

    def play_game(self):

        while True:
            player = self.players[self.current_player]
            self.play_turn(player)
            if self.is_game_over(): break
            self.current_player = self.next_player()
        ranking = self.calculate_ranking()

    def play_turn(self, player):
        turn_score = 0
        turn_dice = 6
        player.update_state(self.players, self.scores, self.current_player, Game.GAME_END)
        turn_start = player.turn_start(self.prev_score, self.prev_dice_left)
        if turn_start == 1:
            turn_score = self.prev_score
            turn_dice = self.prev_dice_left

        roll = self.roll_dice(turn_dice)

        while True:
            # If a roll is a farkle, update state and end turn.
            if self.farkle(roll):
                turn_score = 0
                turn_dice = 6
                break

            move = player.decide_move(turn_score, roll)

            # Check if player decides to end turn.
            if sum(move) == 0:
                score_dice = self.get_score(roll)
                turn_score += score_dice[0]
                turn_dice -= score_dice[1]
                break

            # Continue turn: score the selected dice and roll the rest.
            selected_dice = [a*b for a,b in zip(roll, move)]
            score_dice = self.get_score(selected_dice)
            turn_score += score_dice[0]
            turn_dice -= score_dice[1]


            # If all dice score, restart with 6 fresh dice
            if turn_dice==0: turn_dice += 6;
            roll = self.roll_dice(turn_dice)

        self.update_gamestate(turn_score,turn_dice)
        print(f"Turn \#{self.turn_number}: scores are {self.scores}.")

    def add_player(self, player):
        self.players.append(player)
        self.number_of_players += 1


    def next_player(self):
        return (self.current_player + 1) % self.number_of_players

    def roll_dice(self, number_of_dice):
        return [randint(1,6) for each_die in range(number_of_dice)]

    def farkle(self, roll):
        return True if self.get_score(roll)[0] == 0 else False

    # Calculate best possible score with some roll, returns [score, unscoring dice]
    def get_score(self, roll):
        #TODO: implement this!
        score = 0
        scoring_dice = 0
        dice_freq = [0 for i in range(6)]
        for die in roll: dice_freq[die-1] += 1

        # Check for 3 pairs or six-dice straight
        if len(set(dice_freq)) == 1 or set(dice_freq)=={0,2}:
            return [1000, scoring_dice]
        # Check 1s
        if dice_freq[0] >=3:
            score += 1000 * (2 ** (dice_freq[0] - 3))
            scoring_dice += dice_freq[0]
        else:
            score += 100 * dice_freq[0]
            scoring_dice += dice_freq[0]
        # Check for triples+
        for i in range(1,6):
            if dice_freq[i] >= 3:
                score += 100 * (i + 1) * (2 ** (dice_freq[i] - 3))
                scoring_dice += dice_freq[i]
        # Check 5s < 3
        if dice_freq[4] < 3:
            score += 50 * dice_freq[4]
            scoring_dice += dice_freq[4]

        return [score, scoring_dice]

    def update_gamestate(self, turn_score, turn_dice):
        self.prev_score = turn_score
        self.prev_dice_left = turn_dice
        self.turn_number += 1

    def calculate_ranking(self):
        # Like numpy.argsort
        def sort(list):
            return sorted(range(len(list)), key=list.__getitem__, reverse = True)
        ranking = sort(self.scores)
        print(f"Player {ranking[0]} is the winner with {self.scores[ranking[0]]} points!")
        return ranking

    def is_game_over(self):
        if self.scores[self.next_player()] >= Game.GAME_END:
            return True
        else:
            return False





# Start Game
from example_player import ExamplePlayer
p1 = ExamplePlayer()
p2 = ExamplePlayer()
players = [p1, p2]
game = Game(players)
game.play_game()
