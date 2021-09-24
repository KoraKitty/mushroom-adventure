import pygame, os

class Entity(object):
    def __init__(self,  game, pos, size, image_name):
        self.game = game
        self.pos = pos
        self.size = size
        self.image = self.load_image(image_name)
        self.root = self.update_root()

    def update_pos(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if self.game.board.is_valid_pos(new_pos):
            self.game.board.atlas[self.pos[1]][self.pos[0]].contains_entity = False
            self.pos = new_pos
            self.game.board.atlas[new_pos[1]][new_pos[0]].contains_entity = self
            self.root = self.update_root()

    def load_image(self, image_path):
        image = pygame.image.load(os.path.join("assets", "images", image_path))
        sprite = pygame.transform.scale(image, (self.size, self.size))
        return sprite.convert()


    def update_root(self):
        if self.size < self.game.tile_size:
            return self.pos[0] * self.game.tile_size + self.size / 2, self.pos[1] * self.game.tile_size + self.size / 2
        else:
            return self.pos[0] * self.size, self.pos[1] * self.size

    def draw_entity(self):
        self.game.window.blit(self.image, self.root)
        pygame.display.update()