import pyxel

class Block:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (0,0,0,0,0)

    def brick(self, broken):
        pyxel.image(1).load(16, 16, "mario assets/bricks.png")
        if broken:
            pyxel.image(1).load(0, 0, "mario assets/bricks.png")

    def brick_coins(self, sprite):


    def question(self, sprite):

    def clear(self):
        """We have until here :)"""
