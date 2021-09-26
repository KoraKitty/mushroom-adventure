from engine.Box import Box
import pygame

class MenuBar(Box):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)
        self.gold_box = self.generate_gold_box()

    def generate_gold_box(self):
        # TODO: Make this less bad
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"Gold: {self.game.player.gold}", True, (255, 0, 0))
        gold_display_box = Box(self.game, self.height, self.height, self.root, text)
        gold_display_box.font = font
        return gold_display_box

