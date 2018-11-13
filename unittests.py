
import unittest
from v2 import Game

class GameTests(unittest.TestCase):

    #def test_Add_player(self):
        #game = Game()
        #game.add_player(0)
        #self.assertTrue(game.number_of_players == 1)

    def test_Next_player(self):
        game1 = Game()
        self.assertFalse(game == game1)
        game1.add_player(0)
        game1.add_player(0)
        self.assertTrue(game1.next_player() == 1)
        game1.current_player = game1.next_player()
        self.assertTrue(game1.next_player() == 0)

    #def test_is_game_over(self):
        #game = Game()
        #game.scores = [0,20000]
        #game.GAME_END = 10000
        #game.next_player =
        #self.assert_()



if __name__ == '__main__':
    unittest.main()
