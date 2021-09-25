from random import sample
from entities.Tile import Tile


class Board:
    def __init__(self, game, width, height):
        self.game = game
        self.size = {
            "rows": height,
            "columns": width,
        }
        self.atlas = self.generate_atlas()
        self.draw_board()

    def is_valid_pos(self, pos):
        # TODO: This should be handled by the Board class
        if 0 <= pos[0] <= (len(self.atlas[0]) - 1) and 0 <= pos[1] <= (len(self.atlas) - 1):
            return True
        return False

    def draw_board(self):
        for row in range(self.size["rows"]):
            for tile in self.atlas[row]:
                tile.draw_entity()
                if tile.contains_entity:
                    tile.contains_entity.draw_entity()

    def generate_atlas(self):
        atlas = []
        for row in range(self.size["rows"]):
            temp_row = []
            for column in range(self.size["columns"]):
                tile = Tile(self.game, (column, row), "grass_tile_1.png")
                temp_row.append(tile)
            atlas.append(temp_row)

        return atlas