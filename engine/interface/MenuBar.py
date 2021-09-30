from engine.interface.Box import Box
from engine.interface.ButtonActions import increment_strength


class MenuBar(Box):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)
        self.stats_box = self.generate_stats_box(offset=(15, 7), height=85, width=85)
        self.strength_ibox = self.generate_box(offset=(115, 7), height=85, width=85, surface="strength_icon.png",
                                               button_func=increment_strength)
        self.draw_box_tree()

    def generate_stats_box(self, offset, height, width):
        stats_box = self.generate_box(offset=offset, height=height, width=width, surface="stone_tile.png")
        stats = self.game.player.stats
        for index, stat in enumerate(stats):
            child_height = stats_box.height / len(stats)
            child_offset = (5, (child_height * index) + 5)
            stat_string = f"{stat}: {stats[stat]}"
            stats_box.generate_box(offset=child_offset, height=height, width=width, surface=stat_string)

        return stats_box

    def update_stats_box(self):
        self.stats_box = self.generate_stats_box((15,7), self.stats_box.height, self.stats_box.width)

    def check_if_button(self, pos):
        buttons = [box for box in self.contains_box if box.button_func]
        for button in buttons:
            if pos[0] in range(button.root[0], button.root[0] + button.width):
                if pos[1] in range(button.root[1], button.root[1] + button.height):
                    return button
        return False

