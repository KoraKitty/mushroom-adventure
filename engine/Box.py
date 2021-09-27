import pygame


class Box:
    def __init__(self, game, width, height, root, surface_as_string):
        self.game = game
        self.width = width
        self.height = height
        self.root = root
        self.contains_box = False
        self.parent_box = False
        self.surface = self.create_surface(surface_as_string)
        self.draw_box()

    def create_surface(self, surface_as_string):
        raise NotImplementedError("ERROR: create_surface() called on base class instance of Box, which is invalid."
                                  f"Check the creation of this box: {self}, invoke as either TextBox or ImageBox)")

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
