import pygame
from entities.characters.Player import Player
from entities.characters.Enemy import Enemy
from entities.Weapon import Weapon
from engine.MenuBar import MenuBar
from boards.Board import Board
from configparser import ConfigParser

@staticmethod
def get_settings():
    config = ConfigParser()
    config.read('config.ini')
    return config.get('game')

class Game:
    def __init__(self, settings):
        self.tile_size = settings.TILE_SIZE_IN_PIXELS
        self.board_rows = settings.BOARD_WIDTH
        self.board_columns = settings.BOARD_HEIGHT
        self.window_width = self.board_rows * self.tile_size
        self.window_height = self.board_columns * self.tile_size + self.tile_size
        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        self.board = Board(self)
        self.player = self.generate_player()
        self.menu_bar = self.generate_menu_bar()
        self.fps = 100

    def generate_player(self, pos=(0, 0), image='player.png', level=1):
        return Player(self, pos, image, level)

    def generate_enemy(self, pos=(1, 1), image='lvl1_dino.png', level=1):
        # TODO: Set default to bottom right pos in an elegant way
        return Enemy(self, pos, image, level)

    def generate_weapon(self, character, image="lvl1_melee.png"):
        return Weapon(self, character.pos, image, character)

    def generate_menu_bar(self):
        menu_bar = MenuBar(self, (self.tile_size * self.board_columns), self.tile_size, (0, self.board_rows * self.tile_size), "menu_bar.png")
        return menu_bar