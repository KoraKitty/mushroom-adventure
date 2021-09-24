import pygame
from entities.players.Player import Player
from boards.Board import Board


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode([width, height])
        self.tile_size = 50
        self.board = Board(self, width, height)
        self.player = Player(self, (0, 0), self.tile_size / 2, "player.png")
        self.player.draw_entity()
        self.fps = 120

    def place_player(self, player):
        player.root = (player.pos[0]*100 + 25, player.pos[1]*100 + 25)
        self.window.blit(player.surf, player.root)
        pygame.display.update()