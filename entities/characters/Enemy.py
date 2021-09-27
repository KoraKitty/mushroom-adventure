import pygame.time

from entities.Entity import Entity
from entities.characters.Character import Character

class Enemy(Character):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name, level)
        self.step_cooldown_ms = 1500
        self.last_step_time = pygame.time.get_ticks()
        self.game.enemies.append(self)

    def try_to_move(self):
        ticks = pygame.time.get_ticks()
        if (ticks - self.last_step_time) > self.step_cooldown_ms:
            self.move((-1, 0))
            self.last_step_time = ticks
