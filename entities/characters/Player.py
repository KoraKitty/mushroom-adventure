from entities.characters.Character import Character

class Player(Character):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name, level)

    def attack(self):
        # TODO: Update sprite to 'attack' position
        for i in range(self.contains_entity.range):
            check_pos = ((self.pos[0] + (i + 1)), self.pos[1])
            tile = self.game.board.get_tile(check_pos)
            if tile.contains_entity:
                loot = tile.contains_entity.take_damage(self.contains_entity.base_damage * self.stats['strength'])
                if loot:
                    self.update_loot(loot)

    def update_loot(self, loot):
        for item in loot:
            if item == "gold":
                self.stats['gold'] += loot[item]
                self.game.menu_bar.update_stats_tbox()

