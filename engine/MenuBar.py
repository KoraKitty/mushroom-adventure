from engine.ImageBox import ImageBox
from engine.TextBox import TextBox
import pygame

class MenuBar(ImageBox):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)
        self.gold_textbox = self.generate_gold_textbox(offset=(15, 15))

    def generate_gold_textbox(self, offset):
        root = (self.root[0] + offset[0], self.root[1] + offset[1])
        gold_textbox = TextBox(self.game, self.game.tile_size, self.game.tile_size, root, f"Gold: {self.game.player.gold}")
        self.receive_box(gold_textbox)
        return gold_textbox

    def update_gold_textbox(self):
        self.gold_textbox.update_surface(f"Gold: {self.game.player.gold}")


