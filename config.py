import pygame

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Time
SLEEP_TIME = 5

# Window size
WINDOW_WIDTH, WINDOW_HEIGHT = 780, 600

# Brick settings
BRICK_WIDTH, BRICK_HEIGHT = 50, 20
BRICKS_PER_ROW = 14
ROWS_OF_BRICKS = 10
BRICK_Y_OFFSET = 50  
BRICK_GUTTER_WIDTH = 5  

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 80, BRICK_HEIGHT

# Ball settings
BALL_RADIUS = 10
BALL_Y_VELOCITY = 3.0
BALL_X_VELOCITY = 1.0

# Initialize Pygame + load background image
pygame.init()
background = pygame.image.load('background.png')
