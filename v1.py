import random

class Human:

    def __init__(self, player_num):
      self.player_num = player_num

    def play_turn(self, score, prev_turn):
      turn_score = 0
      stop = True

      while stop==False:
        print("Your score is %d and turn is %d." % (score[self.player_num], turn_score))
        #stop = decide_move()

      #print("Your score is %s and turn is %s." % (score[self.player_num], turn_score))
      addition = int(input("what score increment?"))
      turn_score += addition
      return [turn_score, 0]

class RandomPlayer:

    def move(self, game):
        return random.choice(game.available_actions())


class Game:

    END_SCORE = 10000
    NUM_PLAYERS = 4



    def __init__(self):
        print("initializing game")
        self.players, self.score = self.connect_players() # array of players, in turn order
        print("players: " + str(self.players))
        self.prev_turn = [] #array: [score, number of dice left]
        self.cur_player = 0
        self.game_over = False
        self.last_round = Game.NUM_PLAYERS
        self.play_game()


    def connect_players(self):
        players = []
        score = []
        for i in range(Game.NUM_PLAYERS):
            players.append(Human(i))
            score.append(0)
        return [players, score]

    def play_game(self):
        while self.game_over==False:
            self.play_turn(self.__current())
            #check endgame:
            if self.score[self.cur_player-1] >= Game.END_SCORE: self.game_over = True
            if self.game_over == True:
                # All players get one more chance
                while self.last_round > 1:
                    print("last rounds")
                    self.play_turn(self.__current())
                    self.last_round -= 1

        top_score = max(self.score)
        winner = [i for i, j in enumerate(self.score) if j == top_score]
        print("top score is %s" % top_score)
        print("winner is " + str(winner))

    def play_turn(self, player):
        id = player.player_num
        turn_done = False
        print("player %s starts" % id)
        while turn_done = False:
            self.send_available_moves()



        result = player.play_turn(self.score, self.prev_turn)
        self.score[self.cur_player] += result[0]
        self.prev_turn = result[1]
        print("player %d finished their turn with %d additional points." % (id, result[0]))
        print("current standings: " + str(self.score))
        self.__incr_player()

    def roll(self,num_dice):
        roll_result = [random.randint(1,6) for i in range(num_dice)]
        return (roll_result)
    def score_roll(self, dice):
        score = 0
        # find straight
        # find three pairs
        # find triples+
        # count 1s and 5s

        return score



    def __incr_player(self):
        self.cur_player = (self.cur_player + 1) % Game.NUM_PLAYERS
    def __current(self):
        return self.players[self.cur_player]



def main():
    print("in main")
    g = Game()

if __name__== "__main__":
    main()
