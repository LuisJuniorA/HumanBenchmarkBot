from script.gameBase import GameBase
from script.sequence import Sequence
from script.wpm import WPM

class GameFactory:

    @staticmethod
    def get_game(game_index: int) -> GameBase:
        games = {
            1: WPM,
            2: Sequence,
        }

        game_class = games.get(game_index)
        if not game_class:
            raise ValueError(f"Unknown index: {game_index}")
        return game_class()
