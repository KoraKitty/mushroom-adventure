from entities.Entity import Entity

class Weapon(Entity):
    def __init__(self, game, pos, image_name, character):
        super().__init__(game, pos, image_name)
        self.character = character
        self.character.receive_entity(self)
        self.damage = self.character.level
        self.range = 1

