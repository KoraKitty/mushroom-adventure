import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)
from random import sample
from entities import Entity
from entities.players import Player
from engine.Game import Game
import settings

def setup():
    pygame.init()
    game = Game(settings)
    pygame.display.set_caption("Game Development?")
    return game

def spawn_enemy(game):
    pass

def input_update(pressed_keys):
    movement_keys = {
        K_DOWN: "K_DOWN",
        K_UP: "K_UP",
        K_LEFT: "K_LEFT",
        K_RIGHT: "K_RIGHT"
    }
    move_values = {
        K_DOWN: (0, 1),
        K_UP: (0, -1),
        K_LEFT: (-1, 0),
        K_RIGHT: (1, 0)
    }
    for key in movement_keys:
        if pressed_keys[key]:
            print(movement_keys[key])
            move = move_values[key]
            return move
    return False

def start():
    game = setup()
    spawn_enemy(game)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(game.fps)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                move = input_update(pressed_keys)
                if move:
                    game.player.update_pos(move)

            if event.type == QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    start()