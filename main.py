import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KEYDOWN,
    QUIT,
)
from engine.Game import Game
import settings


def setup():
    pygame.init()
    game = Game(settings)
    pygame.display.set_caption("Game Development?")
    return game


def input_update(pressed_keys):
    action_keys = [K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE]
    # TODO: Order of action_keys matters, may want to revisit
    key_values = {
        K_DOWN: ("move", (0, 1)),
        K_UP: ("move", (0, -1)),
        K_LEFT: ("move", (-1, 0)),
        K_RIGHT: ("move", (1, 0)),
        K_SPACE: "attack"
    }
    for key in action_keys:
        if pressed_keys[key]:
            print(key_values[key])
            return key_values[key]
    return False


def start():
    game = setup()
    game.generate_enemy(pos=(game.board_columns - 1, game.board_rows - 1))
    game.generate_weapon(game.player, "lvl1_melee.png")
    running = True
    while running:
        game.take_actions()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                action = input_update(pressed_keys)
                if action:
                    if action[0] == "move":
                        game.player.move(action[1])
                    # TODO: action currently returns as string if only one object, need more generic or w/e
                    elif action == "attack":
                        game.player.attack()

            if event.type == QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    start()
