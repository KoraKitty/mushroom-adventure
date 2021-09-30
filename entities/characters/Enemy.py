import pygame.time

from entities.Entity import Entity
from entities.characters.Character import Character

class Enemy(Character):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name, level)
        self.step_cooldown_ms = 1500
        self.last_step_time = pygame.time.get_ticks()
        self.game.enemies.append(self)

    def attack(self):
        # TODO: Update sprite to 'attack' position
        for i in range(self.contains_entity.range):
            check_pos = ((self.pos[0] + (i + 1)), self.pos[1])
            tile = self.game.board.get_tile(check_pos)
            if tile.contains_entity:
                raise NotImplementedError("LOL I haven't implemented this yet oops")

    def die(self):
        self.tile.receive_entity(False)
        print(f"{self} has died")
        self.game.enemies.remove(self)

    def try_to_move(self):
        ticks = pygame.time.get_ticks()
        if (ticks - self.last_step_time) > self.step_cooldown_ms:
            self.move((-1, 0))
            self.last_step_time = ticks


