from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import (
    DEFAULT_TYPE,
    SEED,
    )


class Seed(PowerUp):
    def __init__(self):
        self.image = SEED
        self.type = DEFAULT_TYPE
        self.is_used = False
        super().__init__(self.image, self.type)