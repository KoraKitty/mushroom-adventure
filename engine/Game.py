import pygame
from entities.players.Player import Player
from entities.Enemy import Enemy
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
        self.window_height = self.board_columns * self.tile_size
        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        self.board = Board(self, settings.BOARD_WIDTH, settings.BOARD_HEIGHT)
        self.player = self.generate_player()
        self.generate_enemy()
        self.fps = 100

    def generate_player(self, pos=(0, 0), image='player.png'):
        player = Player(self, pos, image)
        tile = player.get_tile()
        tile.contains_entity = player
        tile.draw_entity()
        return player

    def generate_enemy(self, pos=(1, 1), image='lvl1_dino.png', level=1):
        # TODO: Set default to bottom right pos in an elegant way
        enemy = Enemy(self, pos, image, level)
        tile = enemy.get_tile()
        tile.contains_entity = enemy
        tile.draw_entity()
        return enemy

