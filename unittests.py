
import unittest
import sys

class GameTests(unittest.TestCase):

    def _make_Game(self, clear=False):
        if clear:
            try:
                del sys.modules['game']
            except KeyError:
                pass
        from game import Game
        return Game

    def test_Add_player(self):
        game = self._make_Game(clear=True)()
        game.add_player(0)
        self.assertTrue(game.number_of_players == 1)

    def test_Next_player(self):
        game = self._make_Game(clear=True)()
        game.add_player(0)
        game.add_player(0)
        self.assertTrue(game.next_player() == 1)
        game.current_player = game.next_player()
        self.assertTrue(game.next_player() == 0)

    def test_is_game_over(self):
        game = self._make_Game(clear=True)()
        game.scores = [0,20000]
        game.GAME_END = 10000
        game.number_of_players = 2
        game.cur_player = 1
        self.assertTrue(game.is_game_over())



if __name__ == '__main__':
    unittest.main()
