import pygame, os

class Entity(object):
    # TODO: look at initialization of all Entity subclasses and see if it can be made better (kwargs?)
    def __init__(self,  game, pos, image_name):
        self.game = game
        self.pos = pos
        self.size = self.game.tile_size
        self.image = self.load_image(image_name)
        self.root = self.update_root()
        self.contains_entity = False

    def load_image(self, image_path):
        image = pygame.image.load(os.path.join("assets", "images", image_path))
        sprite = pygame.transform.scale(image, (int(self.size), int(self.size)))
        return sprite.convert()

    def receive_entity(self, entity):
        self.contains_entity = entity
        self.draw_entity()

    def update_root(self):
        # TODO: make root better? Maybe root always operates off pos so no attribute is needed
        return self.pos[0] * self.size, self.pos[1] * self.size

    def update_pos(self, pos):
        self.pos = pos
        self.root = self.update_root()
        if self.contains_entity:
            self.contains_entity.update_pos(self.pos)

    def draw_entity(self):
        self.game.window.blit(self.image, self.root)
        if self.contains_entity:
            self.contains_entity.draw_entity()
        pygame.display.update()