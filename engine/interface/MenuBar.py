from engine.interface.ImageBox import ImageBox
from engine.interface.StatsBox import StatsBox
from engine.interface.ButtonActions import increment_strength


class MenuBar(ImageBox):
    def __init__(self, game, width, height, root, image_name):
        super().__init__(game, width, height, root, image_name)
        self.stats_tbox = self.generate_box(offset=(15, 15), box_type=StatsBox,
                                            surface="butt")
        self.strength_ibox = self.generate_box(offset=(115, 15), box_type=ImageBox,
                                               surface="strength_icon.png", button_func=increment_strength)
        self.draw_box_tree()

    def generate_box(self, offset, box_type, surface, button_func=False):
        root = (self.root[0] + offset[0], self.root[1] + offset[1])
        box = box_type(self.game, self.game.tile_size, self.game.tile_size,
                       root, surface)
        if button_func:
            box.button_func = button_func
        self.receive_box(box)
        return box

    def create_stats_surface_and_root(self):
        surface_list, root_list = [], []
        for index, stat in enumerate(self.game.player.stats):
            stat_string = f"{stat}: {self.game.player.stats[stat]}"
            surface = self.stats_tbox.create_surface(stat_string)
            surface_list.append(surface)
            root = (self.root[0] + 20, self.root[1] + 10 + (self.height / len(self.game.player.stats) * index))
            root_list.append(root)
        return surface_list, root_list

    def update_stats_tbox(self):
        self.stats_tbox.surface, self.stats_tbox.root = self.create_stats_surface_and_root()
        self.draw_box_tree()

    def check_if_button(self, pos):
        buttons = [box for box in self.contains_box if box.button_func]
        for button in buttons:
            if pos[0] in range(button.root[0], button.root[0] + button.width):
                if pos[1] in range(button.root[1], button.root[1] + button.height):
                    return button
        return False

