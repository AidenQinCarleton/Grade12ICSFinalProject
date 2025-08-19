import pygame


class Bullet(pygame.sprite.Sprite):
    creator = None
    speed = 0
    screen = None
    image = None

    def __init__(self, x, y, creator, screen):
        super().__init__()
        pygame.display.init()
        self.creator = creator
        self.screen = screen

        if creator.name == 'Marisa':
            self.speed = 40
            self.rect = pygame.Rect(x, y, 40, 20)
            self.image = pygame.image.load('graphics/bullet/MarisaBullet.png').convert_alpha()
        elif creator.name == 'Little_Devil':
            self.speed = -4
            self.rect = pygame.Rect(x, y, 40, 40)
            self.image = pygame.image.load('graphics/bullet/LittleDevilBullet.png').convert_alpha()
        elif creator.name == 'Patchouli':
            self.speed = -4
            self.rect = pygame.Rect(x, y, 40, 40)
            self.image = pygame.image.load('graphics/bullet/PatchouliBullet.png').convert_alpha()
        else:
            self.speed = -4
            self.rect = pygame.Rect(x, y, 40, 40)
            self.image = pygame.image.load('graphics/bullet/NormalBullet.png').convert_alpha()

    def draw(self):
        # pygame.draw.rect(self.screen, (0, 255, 0), self.rect)  # bullet hit box, will not be used since already have
        # imaged
        image_rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.screen.blit(self.image, image_rect)

    def move(self):
        self.rect.x += self.speed

    def destroy(self):
        if self.rect.x <= -100 or self.rect.x >= 2000:
            self.kill()

    def kill(self):
        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(0, 0, -100, -100)
        super().kill()
