import pygame
from entities.Entity import Entity


class Player(Entity):
    def __init__(self, game, pos, size, image_name):
        super().__init__(game, pos, size, image_name)
        self.update_pos((0, 0))