import pygame


class Marisa(pygame.sprite.Sprite):
    shooting_separate_parameter = 8  # use to determine how fast can the player shot
    shooting_separate_variable = 0
    hit_variable = 0
    hit_parameter = 60 * 5  # how long will player take damage again
    name = 'Marisa'
    health = 5
    plot_position = 'right'
    in_game_image = None

    def __init__(self, x, y):
        super().__init__()
        pygame.display.init()
        self.in_game_image = pygame.image.load('graphics/character/marisa/marisaInGame.png').convert_alpha()
        self.rect = pygame.Rect(x, y, 15, 15)

    def draw(self, screen):
        keys = pygame.key.get_pressed()
        marisa_rect = self.in_game_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        if keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:  # if shift is pressed, show hit point above image
            screen.blit(self.in_game_image, marisa_rect)
            pygame.draw.rect(screen, (255, 0, 0), self.rect)
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)
            screen.blit(self.in_game_image, marisa_rect)

    def move(self, screen_width, screen_height):
        # parameters
        speed = 10
        accurate_speed = 4
        dx = 0
        dy = 0

        # keys detection
        keys = pygame.key.get_pressed()

        # Shift detection
        if keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:

            # Accurate movement
            if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:
                dx -= accurate_speed
            if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:
                dx += accurate_speed
            if keys[pygame.K_UP] and keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:
                dy -= accurate_speed
            if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:
                dy += accurate_speed

        else:

            # movement
            if keys[pygame.K_LEFT]:
                dx -= speed
            if keys[pygame.K_RIGHT]:
                dx += speed
            if keys[pygame.K_UP]:
                dy -= speed
            if keys[pygame.K_DOWN]:
                dy += speed

        # border detection
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.top + dy < 0:
            dy = -self.rect.top
        if self.rect.bottom + dy > screen_height:
            dy = screen_height - self.rect.bottom

        # update position
        self.rect.move_ip(dx, dy)
