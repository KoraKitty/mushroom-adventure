import pygame
import os


class Box:
    def __init__(self, game, width, height, root, surface_string):
        self.game = game
        self.width = width
        self.height = height
        self.font = pygame.font.Font('freesansbold.ttf', 14)
        self.surface = self.create_surface(surface_string)
        self.root = root
        self.contains_box = []
        self.parent_box = []
        self.button_func = False
        self.draw_box()

    def create_surface(self, string):
        if ".png" in string:
            image = pygame.image.load(os.path.join("assets", "images", string))
            sprite = pygame.transform.scale(image, (self.width, self.height))
            return sprite.convert()
        else:
            return self.font.render(string, True, (255, 0, 255))

    def find_parent_box(self):
        if self.parent_box:
            self.find_parent_box(self.parent_box)
        else:
            return self

    def draw_box_tree(self):
        self.draw_box()
        for box in self.contains_box:
            box.draw_box_tree()

    def draw_box(self):
        self.game.window.blit(self.surface, self.root)
        pygame.display.update()

    def generate_box(self, offset, height, width, surface, button_func=False):
        root = (self.root[0] + offset[0], self.root[1] + offset[1])
        box = Box(self.game, height, width,
                       root, surface)
        if button_func:
            box.button_func = button_func
        self.receive_box(box)
        return box

    def receive_box(self, box):
        self.contains_box.append(box)
        box.parent_box = self
