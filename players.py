import random

class ExamplePlayer:

    def update_state(self, players, scores, current_player, end_score):
        pass

    def see_the_roll(self, roll):
        print(f"Bot rolled {roll} on {len(roll)} dice.")

    def turn_start(self, prev_score, prev_dice_left):
        #last_score = prev_turn[0]
        #number_of_dice = prev_turn[1]
        return random.getrandbits(1)

    def decide_move(self, turn_score, prev_roll_array):
        num_dice = len(prev_roll_array)
        print(f"In a turn: {prev_roll_array}")
        while True:
            return [random.getrandbits(1) for i in range(num_dice)]

    def stop_or_continue(self):
        return random.getrandbits(1)


class HumanPlayer:

    def update_state(self, players, scores, current_player, end_score):
        print(f"Scores: {scores}.")

    def see_the_roll(self, roll):
        print(f"Your roll of {len(roll)} dice is {roll}.")

    def turn_start(self, prev_score, prev_dice_left):
        response = ''
        while True:
            response = input(f"Continue with {prev_dice_left} dice on {prev_score} points? (y/n): ")
            if response.lower() in ['y','n']: break
        if response.lower() == 'y': return 1
        if response.lower() == 'n': return 0
        print('invalid input in function turn_start.')
        return -1

    def decide_move(self, turn_score, prev_roll_array):
        num_dice = len(prev_roll_array)
        keepers_raw = input(f"Enter 1 or 0 to select dice to keep (binary number with number of digits == number of dice.")
        keepers = [int(i) for i in str(keepers_raw)]
        return keepers

    def stop_or_continue(self):
        answer = input(f"Continue? (enter 1 or 0)")
        return answer
