from entities.Entity import Entity


class Tile(Entity):
    def __init__(self, game, pos, image_name):
        super().__init__(game, pos, image_name)
        self.contains_entity = False
