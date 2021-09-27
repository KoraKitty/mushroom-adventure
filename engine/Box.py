import pygame
import os

class Box:
    # TODO: Split into text box and image box maybe?
    def __init__(self, game, width, height, root, surface_as_string):
        self.game = game
        self.width = width
        self.height = height
        self.root = root
        self.contains_box = False
        self.parent_box = False
        self.surface = self.create_surface(surface_as_string)
        self.draw_box()

    def update_surface(self, surface_as_string):
        self.surface = self.create_surface(str(surface_as_string))
        self.draw_box()

    def draw_box(self):
        if self.parent_box:
            self.parent_box.draw_box()
        self.game.window.blit(self.surface, self.root)
        pygame.display.update()

    def receive_box(self, box):
        if self.contains_box:
            self.contains_box = [*self.contains_box, box]
        else:
            self.contains_box = [box]
        box.parent_box = self


