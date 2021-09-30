from random import sample
from entities.Tile import Tile


class Board:
    def __init__(self, game):
        self.game = game
        self.rows = self.game.board_rows
        self.columns = self.game.board_columns
        self.atlas = self.generate_atlas()
        self.draw_board()

    def is_valid_pos(self, pos):
        if 0 <= pos[0] <= (len(self.atlas[0]) - 1) and 0 <= pos[1] <= (len(self.atlas) - 1):
            tile = self.atlas[pos[1]][pos[0]]
            if not tile.contains_entity:
                return True
        return False

    def draw_board(self):
        for row in range(self.rows):
            for tile in self.atlas[row]:
                tile.draw_entity()
                if tile.contains_entity:
                    tile.contains_entity.draw_entity()

    def generate_atlas(self):
        atlas = []
        for row in range(self.rows):
            temp_row = []
            for column in range(self.columns):
                tile = Tile(self.game, (column, row), "grass_tile_1.png")
                temp_row.append(tile)
            atlas.append(temp_row)

        return atlas

    def get_tile(self, pos):
        # TODO: if tile being obtained is out of bounds, the game crashes. Is this a feature? No. No it is not
        return self.atlas[pos[1]][pos[0]]
