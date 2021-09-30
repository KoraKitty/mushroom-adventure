from entities.Entity import Entity


class Character(Entity):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name)
        self.stats = {
            "level": level,
            "strength": level,
            "hp": level * 3,
            "gold": 5
        }
        self.tile = self.game.board.atlas[self.pos[1]][self.pos[0]]
        self.tile.receive_entity(self)

    def traverse_tiles(self, new_pos):
        self.tile.receive_entity(False)
        self.update_pos(new_pos)
        self.tile = self.game.board.get_tile(self.pos)
        self.tile.receive_entity(self)

    def take_damage(self, damage):
        self.stats['hp'] = self.stats ['hp'] - damage
        if self.stats['hp']  <= 0:
            self.die()
            return self.stats
        return False

    def attack(self):
        raise NotImplementedError("Method Attack was called on the base Character class"
                                  "Characters should only be initialized as Enemy or Player sub-type")

    def move(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if self.game.board.is_valid_pos(new_pos):
            self.traverse_tiles(new_pos)
