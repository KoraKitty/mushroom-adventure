from engine.interface.Box import Box

import pygame


class TextBox(Box):
    def __init__(self, game, width, height, root, text_as_string):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        super().__init__(game, width, height, root, text_as_string)

    def create_surface(self, string):
        return self.font.render(string, True, (0, 255, 0))
