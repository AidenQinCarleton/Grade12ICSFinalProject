import pygame
import random


class LittleDevil(pygame.sprite.Sprite):
    shooting_separate_parameter = 50
    shooting_separate_variable = 0
    hit_variable = 0
    hit_parameter = 1  # how long will take damage again
    name = 'Little_Devil'
    health = 400
    plot_position = 'left'
    in_game_image = None

    def __init__(self, x, y):
        super().__init__()
        pygame.display.init()
        self.in_game_image = pygame.image.load('graphics/character/littleDevil/littleDevilInGame.png').convert_alpha()
        self.rect = pygame.Rect(x, y, 50, 100)

    def draw(self, screen):
        little_devil_rect = self.in_game_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        screen.blit(self.in_game_image, little_devil_rect)
        # pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def move(self, vertical, horizontal):
        # parameters
        speed = random.randint(1, 5)
        dx = 0
        dy = 0

        if vertical:
            dy -= speed
        else:
            dy += speed
        if horizontal:
            dx -= speed
        else:
            dx += speed
        self.rect.move_ip(dx, dy)

    def destroy(self):
        if self.health <= 0:
            self.kill()
