import pygame
from entities.players.Player import Player
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
        self.window_width = settings.BOARD_WIDTH * self.tile_size
        self.window_height = settings.BOARD_HEIGHT * self.tile_size
        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        self.board = Board(self, settings.BOARD_WIDTH, settings.BOARD_HEIGHT)
        self.player = Player(self, (0, 0), "player.png")
        self.player.draw_entity()
        self.fps = 120

    def place_player(self, player):
        player.root = (player.pos[0]*100 + 25, player.pos[1]*100 + 25)
        self.window.blit(player.surf, player.root)
        pygame.display.update()