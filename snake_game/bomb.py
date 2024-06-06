
from food import Food
class Bomb(Food):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.refresh()