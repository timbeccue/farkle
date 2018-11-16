from random import shuffle, randint
import unittest
import time

PRINT = False

def cprint(to_print):
    if PRINT == True: print(to_print)

class Game:

    GAME_END = 100000

    def __init__(self, players = []):
        shuffle(players)
        self.players = players
        self.number_of_players = len(players)
        self.scores = [0 for player in players]
        self.current_player = 0
        self.prev_score = 0
        self.prev_dice_left = 6
        self.turn_number = 0

    def play_game(self):

        while True:
            player = self.players[self.current_player]
            self.play_turn(player)
            if self.is_game_over(): break
            self.current_player = self.next_player()
        ranking = self.calculate_ranking()
        return self.scores

    def play_turn(self, player):
        cprint(f"******************* NEW TURN: *******************")
        turn_score = 0
        turn_dice = 6
        player.update_state(self.players, self.scores, self.current_player, Game.GAME_END)
        turn_start = player.turn_start(self.prev_score, self.prev_dice_left)
        if turn_start == 1:
            turn_score = self.prev_score
            turn_dice = self.prev_dice_left

        roll = self.roll_dice(turn_dice)
        player.see_the_roll(roll)

        while True:
            # If a roll is a farkle, update state and end turn.
            if self.farkle(roll):
                cprint("farkle!")
                turn_score = 0
                turn_dice = 6
                self.update_gamestate(turn_score,turn_dice)
                break

            move = player.decide_move(turn_score, roll)

            # Continue turn: score the selected dice and roll the rest.
            selected_dice = [a*b for a,b in zip(roll, move)]
            while 0 in selected_dice: selected_dice.remove(0)
            cprint(f"{len(selected_dice)} Dice selected: {selected_dice}.")

            score_dice = self.get_score(selected_dice)
            if score_dice[0] == 0:
                cprint("farkle!")
                turn_score = 0
                turn_dice = 6
                self.update_gamestate(turn_score,turn_dice)
                break

            turn_score += score_dice[0]
            turn_dice -= score_dice[1]
            cprint(f"Current turn score is {turn_score} with {turn_dice} dice remaining.")

            # Check if player decides to end turn.
            stop_or_continue = int(player.stop_or_continue())
            if stop_or_continue == 0:
                #score_dice = self.get_score(roll)
                #turn_score += score_dice[0]
                #turn_dice -= score_dice[1]
                self.update_gamestate(turn_score,turn_dice)
                cprint(f"PLAYER ENDS TURN with {turn_score} points and {turn_dice} dice remaining.")
                break


            # If all dice score, restart with 6 fresh dice
            if turn_dice==0: turn_dice += 6;
            roll = self.roll_dice(turn_dice)
            player.see_the_roll(roll)

        cprint(f"Turn #{self.turn_number}: scores are {self.scores}.")

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
        cprint(f"Turn score: {turn_score}.")
        cprint(f"Dice left: {turn_dice}.")
        self.scores[self.current_player] += turn_score
        self.prev_score = turn_score
        self.prev_dice_left = turn_dice if turn_dice != 0 else 6
        self.turn_number += 1

    def calculate_ranking(self):
        # Like numpy.argsort
        def sort(list):
            return sorted(range(len(list)), key=list.__getitem__, reverse = True)
        ranking = sort(self.scores)
        cprint(f"Player {ranking[0]} is the winner with {self.scores[ranking[0]]} points!")
        return ranking

    def is_game_over(self):
        if self.scores[self.next_player()] >= Game.GAME_END:
            return True
        else:
            return False

def main():
    # Start Game
    from players import ExamplePlayer, HumanPlayer
    p1 = ExamplePlayer()
    p2 = ExamplePlayer()
    players = [p1, p2]
    def play_n_games(n):
        start = time.time()
        results = [0 for i in range(n)]
        for i in range(n):
            game = Game(players)
            results[i] = game.play_game()
        print(results)
        print(f'Total time: {round(time.time()-start, 2)} seconds')

    play_n_games(10)

if __name__=='__main__':
    main()
