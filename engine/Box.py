import pygame
import os

class Box:
    # TODO: Split into text box and image box maybe?
    def __init__(self, game, width, height, root, image_name):
        self.game = game
        self.width = width
        self.height = height
        self.root = root
        self.image = self.load_image(image_name)
        self.draw_box()

    def load_image(self, image_path):
        # TODO: Fix image_path name, break if loop out into higher level of abstraction orfigure out a bette rway to pass in text
        if isinstance(image_path, str):
            # If it is a file, load the image
            image = pygame.image.load(os.path.join("assets", "images", image_path))
            sprite = pygame.transform.scale(image, (self.width, self.height))
            return sprite.convert()
        else:
            # If it is an object to be displayed, set that instead
            return image_path

    def draw_box(self):
        self.game.window.blit(self.image, self.root)
        pygame.display.update()

    def update_text(self):
        # TODO: Make sure Box / MenuBar get updated to work with all this right
        self.image = self.font.render(f"Gold: {self.game.player.gold}", True, (255, 0, 0))
        self.game.menu_bar.draw_box()
        self.draw_box()

