import pygame, os

class Entity(object):
    def __init__(self,  game, pos, image_name):
        self.game = game
        self.pos = pos
        self.size = self.game.tile_size
        self.image = self.load_image(image_name)
        self.root = self.update_root()
        self.contains_entity = False

    def update_pos(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if self.game.board.is_valid_pos(new_pos):
            self.traverse_tiles(new_pos)

    def get_tile(self):
        return self.game.board.atlas[self.pos[1]][self.pos[0]]

    def traverse_tiles(self, new_pos):
        old_tile = self.get_tile()
        self.pos = new_pos
        new_tile = self.get_tile()

        old_tile.contains_entity = False
        old_tile.draw_entity()

        new_tile.contains_entity = self
        self.root = self.update_root()
        new_tile.draw_entity()

    def load_image(self, image_path):
        image = pygame.image.load(os.path.join("assets", "images", image_path))
        sprite = pygame.transform.scale(image, (int(self.size), int(self.size)))
        return sprite.convert()


    def update_root(self):
        return self.pos[0] * self.size, self.pos[1] * self.size

    def draw_entity(self):
        self.game.window.blit(self.image, self.root)
        if self.contains_entity:
            self.contains_entity.draw_entity()
        pygame.display.update()