from engine.interface.Box import Box
import pygame
import os


class ImageBox(Box):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)

    def create_surface(self, image_name):
        image = pygame.image.load(os.path.join("assets", "images", image_name))
        sprite = pygame.transform.scale(image, (self.width, self.height))
        return sprite.convert()

