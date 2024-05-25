from config import *
import pygame
from pygame.locals import *

sound_boing = pygame.mixer.Sound('./boing.wav')
sound_boing.set_volume(0.4)


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()  # Optional, if you plan to use sound
        self.running = True
        pygame.display.set_caption("Breakout")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = background  # Use the background loaded in config.py
        self.timer = pygame.time.Clock()
        # Paddle properties
        self.paddle_x = (WINDOW_WIDTH - PADDLE_WIDTH) // 2
        self.paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT - 10  # 10 pixels from bottom
        self.paddle_speed = 10
        # Ball properties
        self.ball_x = WINDOW_WIDTH // 2
        self.ball_y = WINDOW_HEIGHT // 2
        self.ball_x_velocity = BALL_X_VELOCITY
        self.ball_y_velocity = BALL_Y_VELOCITY
        # Lives and font
        self.lives = 5
        self.font = pygame.font.Font(None, 36)  # Use default font
        # Blocks
        self.blocks = self.create_blocks()

    def create_blocks(self):
        blocks = []
        for row in range(ROWS_OF_BRICKS):
            for col in range(BRICKS_PER_ROW):
                x = col * (BRICK_WIDTH + BRICK_GUTTER_WIDTH) + BRICK_GUTTER_WIDTH
                y = row * (BRICK_HEIGHT + BRICK_GUTTER_WIDTH) + BRICK_Y_OFFSET
                blocks.append(pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT))
        return blocks

    def draw_paddle(self):
        paddle_rect = pygame.Rect(self.paddle_x, self.paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        pygame.draw.rect(self.surface, BLACK, paddle_rect)  # Change paddle color to black

    def draw_ball(self):
        pygame.draw.circle(self.surface, RED, (self.ball_x, self.ball_y), BALL_RADIUS)

    def draw_lives(self):
        lives_text = self.font.render(f"Lives: {self.lives}", True, RED)
        self.surface.blit(lives_text, (10, 10))  # Position the text at the top-left corner

    def draw_blocks(self):
        for block in self.blocks:
            pygame.draw.rect(self.surface, BLUE, block)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.paddle_x -= self.paddle_speed
            if self.paddle_x < 0:
                self.paddle_x = 0
        if keys[K_RIGHT]:
            self.paddle_x += self.paddle_speed
            if self.paddle_x > WINDOW_WIDTH - PADDLE_WIDTH:
                self.paddle_x = WINDOW_WIDTH - PADDLE_WIDTH

    def move_ball(self):
        self.ball_x += self.ball_x_velocity
        self.ball_y += self.ball_y_velocity
        # Ball collision with left and right walls
        if self.ball_x - BALL_RADIUS < 0 or self.ball_x + BALL_RADIUS > WINDOW_WIDTH:
            self.ball_x_velocity = -self.ball_x_velocity
            sound_boing.play()
        # Ball collision with top wall
        if self.ball_y - BALL_RADIUS < 0:
            self.ball_y_velocity = -self.ball_y_velocity
            sound_boing.play()
        # Ball collision with paddle
        if (self.paddle_y < self.ball_y + BALL_RADIUS < self.paddle_y + PADDLE_HEIGHT and
                self.paddle_x < self.ball_x < self.paddle_x + PADDLE_WIDTH):
            self.ball_y_velocity = -self.ball_y_velocity
            sound_boing.play()
        # Ball collision with blocks
        for block in self.blocks[:]:
            if block.colliderect(pygame.Rect(self.ball_x - BALL_RADIUS, self.ball_y - BALL_RADIUS, BALL_RADIUS * 2,
                                             BALL_RADIUS * 2)):
                self.blocks.remove(block)
                self.ball_y_velocity = -self.ball_y_velocity
                sound_boing.play()
        # Ball goes out of bottom
        if self.ball_y + BALL_RADIUS > WINDOW_HEIGHT:
            self.lives -= 1
            self.ball_x, self.ball_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
            self.ball_x_velocity, self.ball_y_velocity = BALL_X_VELOCITY, BALL_Y_VELOCITY
            if self.lives <= 0:
                self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("The up key has been pressed down")
            self.handle_input()
            self.move_ball()
            self.surface.blit(self.background, (0, 0))  # Draw the background image
            self.draw_paddle()  # Draw the paddle
            self.draw_ball()  # Draw the ball
            self.draw_lives()  # Draw the lives
            self.draw_blocks()  # Draw the blocks
            pygame.display.update()
            self.timer.tick(60) 
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()