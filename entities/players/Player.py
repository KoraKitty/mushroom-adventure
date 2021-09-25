import pygame
from entities.Entity import Entity


class Player(Entity):
    def __init__(self, game, pos, image_name):
        super().__init__(game, pos, image_name)