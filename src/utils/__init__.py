"""
Game constants and configuration values.
"""

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game settings
FPS = 60
GAME_TITLE = "Python AI Pygame Game"

# Colors (RGB tuples)
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "GRAY": (128, 128, 128),
    "DARK_GRAY": (64, 64, 64),
    "LIGHT_GRAY": (192, 192, 192),
}

# Player settings
PLAYER_SPEED = 200.0
PLAYER_SIZE = 32

# Enemy settings
ENEMY_SPEED = 100.0
ENEMY_SIZE = 24

# AI settings
AI_UPDATE_FREQUENCY = 60  # Updates per second
FLOCKING_RADIUS = 100.0
SEPARATION_WEIGHT = 1.5
ALIGNMENT_WEIGHT = 1.0
COHESION_WEIGHT = 1.0

# Input key mappings
MOVEMENT_KEYS = {
    "UP": ["K_UP", "K_w"],
    "DOWN": ["K_DOWN", "K_s"],
    "LEFT": ["K_LEFT", "K_a"],
    "RIGHT": ["K_RIGHT", "K_d"],
}

# Game states
GAME_STATES = {
    "MENU": 0,
    "PLAYING": 1,
    "PAUSED": 2,
    "GAME_OVER": 3,
}

# Asset paths
ASSETS_DIR = "assets"
IMAGES_DIR = f"{ASSETS_DIR}/images"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"
FONTS_DIR = f"{ASSETS_DIR}/fonts"
