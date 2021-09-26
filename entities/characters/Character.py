from entities.Entity import Entity

class Character(Entity):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name)
        self.level = level
        self.hp = level
        self.gold = 5
        self.tile = self.game.board.atlas[self.pos[1]][self.pos[0]]
        self.tile.receive_entity(self)

    def traverse_tiles(self, new_pos):
        self.tile.receive_entity(False)
        self.update_pos(new_pos)
        self.tile = self.game.board.get_tile(self.pos)
        self.tile.receive_entity(self)

    def attack(self):
        # TODO: Update sprite to 'attack' position
        for i in range(self.contains_entity.range):
            check_pos = ((self.pos[0] + (i + 1)), self.pos[1])
            tile = self.game.board.get_tile(check_pos)
            if tile.contains_entity:
                enemy = tile.contains_entity
                enemy.hp = enemy.hp - self.contains_entity.damage
                # TODO: Does it make sense for Character to handle the below, or would it make more sense for it to be calced by board
                if enemy.hp == 0:
                    enemy.die()
                    self.gold = self.gold + enemy.gold
                    self.game.menu_bar.gold_box.update_text()

    def move(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if self.game.board.is_valid_pos(new_pos):
            self.traverse_tiles(new_pos)

    def die(self):
        self.tile.receive_entity(False)