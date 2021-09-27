import pygame
from random import randint
from entities.characters.Player import Player
from entities.characters.Enemy import Enemy
from entities.Weapon import Weapon
from engine.MenuBar import MenuBar
from boards.Board import Board


class Game:
    def __init__(self, settings):
        self.tile_size = settings.TILE_SIZE_IN_PIXELS
        self.board_rows = settings.BOARD_HEIGHT
        self.board_columns = settings.BOARD_WIDTH
        self.window_width = self.board_columns * self.tile_size
        self.window_height = self.board_rows * self.tile_size + self.tile_size
        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        self.board = Board(self)
        self.player = self.generate_player()
        self.menu_bar = self.generate_menu_bar()
        self.enemies = []
        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_rate_ms = 1250
        self.spawn_boundary = ((self.board_columns - 1, 0), (self.board_columns - 1, self.board_rows - 1))

    def generate_player(self, pos=(0, 0), image='player.png', level=1):
        return Player(self, pos, image, level)

    def generate_enemy(self, pos=(1, 1), image='lvl1_dino.png', level=1):
        # TODO: Set default to bottom right pos in an elegant way
        return Enemy(self, pos, image, level)

    def generate_weapon(self, character, image="lvl1_melee.png"):
        return Weapon(self, character.pos, image, character)

    def generate_menu_bar(self):
        return MenuBar(self, (self.tile_size * self.board_columns), self.tile_size,
                       (0, self.board_rows * self.tile_size), "menu_bar.png")

    def generate_spawn_pos(self):
        return (randint(self.spawn_boundary[0][0], self.spawn_boundary[1][0]),
                randint(self.spawn_boundary[0][1], self.spawn_boundary[1][1]))

    def take_actions(self):
        self.try_to_spawn()
        self.take_enemy_actions()

    def take_enemy_actions(self):
        for enemy in self.enemies:
            enemy.try_to_move()

    def try_to_spawn(self):
        if (pygame.time.get_ticks() - self.last_spawn_time) > self.spawn_rate_ms:
            spawn_pos = self.generate_spawn_pos()
            if self.board.is_valid_pos(spawn_pos):
                self.generate_enemy(pos=spawn_pos)
                self.last_spawn_time = pygame.time.get_ticks()
