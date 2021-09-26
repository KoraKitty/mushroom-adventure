from entities.Entity import Entity

class Enemy(Entity):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name)
        self.level = level
