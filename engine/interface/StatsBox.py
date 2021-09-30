from engine.interface.TextBox import TextBox


class StatsBox(TextBox):
    def __init__(self, game, width, height, root, text_as_string):
        super().__init__(game, width, height, root, text_as_string)
        self.root = self.generate_roots()
        self.surface = self.generate_surfaces()

    def generate_surfaces(self):
        # TODO: TextBox and ImageBox set self.surface during init using create_surface which returns a single object. StatsBox breaks this pattern, but as they all use the same underlying Box class, it is not an easy fix
        surface_list = []
        for stat in self.game.player.stats:
            stat_string = f"{stat}: {self.game.player.stats[stat]}"
            surface = self.create_surface(stat_string)
            surface_list.append(surface)
        return surface_list

    def generate_roots(self):
        root_list = []
        for index in range(len(self.game.player.stats)):
            root = (self.root[0], self.root[1] + (20 * index))
            root_list.append(root)
        return root_list