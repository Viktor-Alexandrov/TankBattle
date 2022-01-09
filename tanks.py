from game_locals import load_image

collection_player_tank = [
    'assets/sprites/T34_up.png',
    'assets/sprites/T34_left.png',
    'assets/sprites/T34_bottom.png',
    'assets/sprites/T34_right.png'
]


class CreateTanks:

    def __init__(self):
        self.is_alpha = None
        self.path = None
        self.direction = None

    def create_tank(self, is_alpha, direction):

        self.direction = direction
        self.is_alpha = is_alpha

        if self.direction == 'up':
            self.path = collection_player_tank[0]
        elif self.direction == 'left':
            self.path = collection_player_tank[1]
        elif self.direction == 'bottom':
            self.path = collection_player_tank[2]
        elif self.direction == 'right':
            self.path = collection_player_tank[3]

        return load_image(self.path, is_alpha)
