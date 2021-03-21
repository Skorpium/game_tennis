
class Player:

    def __init__(self, player: str, points: float):
        self._points = points
        self._player = player

    def add_points(self):
        self._points += 1

    def get_points(self):
        return self._points

    def get_name(self) -> str:
        return self._player