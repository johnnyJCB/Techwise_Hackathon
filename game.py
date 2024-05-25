from config import *
import pygame
from pygame.locals import *

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

    def draw_paddle(self):
        paddle_rect = pygame.Rect(self.paddle_x, self.paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        pygame.draw.rect(self.surface, BLACK, paddle_rect)

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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("The up key has been pressed down")

            self.handle_input()

            self.surface.blit(self.background, (0, 0))  # Draw the background image
            self.draw_paddle()  # Draw the paddle

            pygame.display.update()
            self.timer.tick(60)  # Cap the frame rate to 60 FPS

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

