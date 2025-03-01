import pygame 
import os


# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUS = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_S = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpSuperman1.0.png"))
JUMPING_1 = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpFase1.png"))
JUMPING_D = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpFaseD.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_N = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

FREZER = [
    pygame.image.load(os.path.join(IMG_DIR, "patada/patadavoladoraninja.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Patada/frezer1.png"))
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
CLOUD_D = pygame.image.load(os.path.join(IMG_DIR, 'Other/nubevoladora.png'))
LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/vida.png'))
SEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/semilla.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

FONT_STYLE = "freesansbold.ttf"

COLORS = {
    'Black': (0,0,0),
    'White': (255,255,255),
    'Blue': (0,102,255),
    'Cyan': (0,255,255),
    'Yellow': (255,255,0),
    'Green': (0,128,0),
    'Red': (255,0,0),
    'Light green': (153,255,0),
    'Lead': (181,178,178),
    'Golden': (218, 165, 32)
}

DRAGON_MENU = [pygame.image.load(os.path.join(IMG_DIR, 'Other/dino_ball_bg.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'Other/gokuchildren.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'Other/dinosaurmenu.png'))
               ]

SHENG_LONG = pygame.image.load(os.path.join(IMG_DIR, 'Other/shenlongscreen.png'))

ESFERA_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/esfera1.png'))
ESFERA_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/esfera2.png'))
ESFERA_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/esfera3.png'))