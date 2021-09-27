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

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp == 0:
            self.die()
            loot_dict = {
                "gold": self.gold
            }
            return loot_dict
        return False

    def attack(self):
        # TODO: Update sprite to 'attack' position
        for i in range(self.contains_entity.range):
            check_pos = ((self.pos[0] + (i + 1)), self.pos[1])
            tile = self.game.board.get_tile(check_pos)
            if tile.contains_entity:
                loot = tile.contains_entity.take_damage(self.contains_entity.damage)
                if loot:
                    # TODO: make an update_loot() process to handle taking in loot and updating the UI
                    self.gold = self.gold + loot["gold"]
                    self.game.menu_bar.update_gold_textbox()

    def move(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if self.game.board.is_valid_pos(new_pos):
            self.traverse_tiles(new_pos)

    def die(self):
        self.tile.receive_entity(False)
        print(f"{self} has died")
        if "Enemy" in str(type(self)):
            self.game.enemies.remove(self)
