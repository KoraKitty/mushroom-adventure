from entities.characters.Character import Character

class Player(Character):
    def __init__(self, game, pos, image_name, level):
        super().__init__(game, pos, image_name, level)

