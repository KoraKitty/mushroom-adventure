import pygame


class Box:
    def __init__(self, game, width, height, root, surface_as_string):
        self.game = game
        self.width = width
        self.height = height
        self.root = root
        self.contains_box = []
        self.parent_box = []
        self.surface = self.create_surface(surface_as_string)
        self.draw_box()
        self.button_func = False

    def create_surface(self, surface_as_string):
        raise NotImplementedError("ERROR: create_surface() called on base class instance of Box, which is invalid."
                                  f"Check the creation of this box: {self}, invoke as either TextBox or ImageBox)")

    def update_surface(self, surface_as_string):
        self.surface = self.create_surface(str(surface_as_string))

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
        if isinstance(self.surface, list):
            for surface, root in zip(self.surface, self.root):
                self.game.window.blit(surface, root)
        else:
            self.game.window.blit(self.surface, self.root)
        pygame.display.update()

    def receive_box(self, box):
        self.contains_box.append(box)
        box.parent_box = self
