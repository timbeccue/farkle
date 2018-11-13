
# Farkle

The classic dice game, recreated in python. This game logic is designed to help me practice creating players using learning algorithms.

## Usage

Play a game by running `game.py`. Players, defined in `players.py`, are currently either random bots or human players with inputs given in the command prompt. Specify the number/type of players and number of games inside the main() function in `game.py`.

## Player Design

Players that work with the game require 5 functions with specific names, arguments, and outputs:

1. update_state(self, players, scores, current_player, end_score)
  * `players` is an array of the players in the game.
  * `scores` is an array of scores. The index of a player is the same index of their corresponding score.
  * `current_player` is the index of the current player.
  * `end_score` is the score that, when reached, begins the final round of turns.

  * ``

2. see_the_roll(self, roll)
  * `roll` is an array of integers in [1,6] representing the latest roll.
