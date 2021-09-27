from engine.Box import Box
import pygame
import os


class ImageBox(Box):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)


    def create_surface(self, image_path):
        # TODO: Fix image_path name, break if loop out into higher level of abstraction orfigure out a bette rway to pass in text
        image = pygame.image.load(os.path.join("assets", "images", image_path))
        sprite = pygame.transform.scale(image, (self.width, self.height))
        return sprite.convert()
