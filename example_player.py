import random


class ExamplePlayer:

    def __init__(self):
        pass

    def update_state(self, players, scores, current_player, end_score):
        pass

    def turn_start(self, prev_score, prev_dice_left):
        #last_score = prev_turn[0]
        #number_of_dice = prev_turn[1]

        return random.getrandbits(1);

    def decide_move(self, turn_score, prev_roll_array):
        num_dice = len(prev_roll_array)
        if random.getrandbits(1):
            return [random.getrandbits(1) for i in range(num_dice)]
        else:
            return [0 for i in range(num_dice)]
