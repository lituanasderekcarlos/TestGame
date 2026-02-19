import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertIsNotNone(self.game)

    def test_game_start(self):
        self.game.start()
        self.assertTrue(self.game.is_running)

    def test_game_over(self):
        self.game.start()
        self.game.game_over()
        self.assertFalse(self.game.is_running)

    def test_score_increment(self):
        initial_score = self.game.score
        self.game.increment_score()
        self.assertEqual(self.game.score, initial_score + 1)

if __name__ == '__main__':
    unittest.main()