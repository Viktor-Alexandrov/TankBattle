from game_locals import load_image


class CreateTanks:
    # Базовый класс для всех видов танков.

    def __init__(self):
        self.is_alpha = None
        self.direction = None
        self.path = None

    def create_tank(self, is_alpha, direction):
        pass


class CreatePlayerTank(CreateTanks):
    # Класс для создания танка игрока.

    def __init__(self):
        super().__init__()
        self.collection_player_tanks = [
            'assets/sprites/T34_up.png',
            'assets/sprites/T34_left.png',
            'assets/sprites/T34_bottom.png',
            'assets/sprites/T34_right.png'
        ]

    def create_tank(self, is_alpha, direction):

        self.direction = direction
        self.is_alpha = is_alpha

        if self.direction == 'up':
            self.path = self.collection_player_tanks[0]
        elif self.direction == 'left':
            self.path = self.collection_player_tanks[1]
        elif self.direction == 'bottom':
            self.path = self.collection_player_tanks[2]
        elif self.direction == 'right':
            self.path = self.collection_player_tanks[3]

        return load_image(self.path, is_alpha)
