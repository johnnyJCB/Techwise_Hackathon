import pygame


class Block:
    def __init__(self, pos: tuple[int, int], max_hp: int = 1, color: tuple[int, int, int] = (255, 255, 255), width: int = 50, height: int = 25):
        self.pos = pos
        self.max_hp = max_hp
        self.hp = max_hp
        self.alive = True
        self.width = width
        self.height = height
        self.rect = pygame.Rect(*self.pos, self.width, self.height)
        self.color = color

    def is_alive(self) -> bool:
        return self.hp > 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def hit(self):
        self.hp -= 1