import pygame


class NormalEnemy(pygame.sprite.Sprite):
    normal_enemy_shooting_separate_parameter = 0
    normal_enemy_shooting_separate_variable = 0
    hit_variable = 0
    hit_parameter = 60 * 0.5  # how long will take damage again
    name = 'Normal_Enemy'
    in_game_image = None
    type = 0
    health = 0
    size_x = 60
    size_y = 60
    init_x = 0
    init_y = 0

    # game environment
    screen_width = 0
    screen_height = 0

    def __init__(self, x, y, create_type, screen_width, screen_height):
        super().__init__()
        pygame.display.init()
        self.rect = pygame.Rect(x, y, self.size_x, self.size_y)
        self.init_x = x
        self.init_y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.type = create_type
        if create_type == 1:
            self.name = 'Practice_Maid'
            self.normal_enemy_shooting_separate_parameter = 500
            self.health = 3
            self.in_game_image = pygame.image.load('graphics/character/normalEnemy/Fairy1.png').convert_alpha()
            self.in_game_image = pygame.transform.scale(self.in_game_image, (self.size_x, self.size_y))
        elif create_type == 2:
            self.name = 'Normal_Maid'
            self.normal_enemy_shooting_separate_parameter = 400
            self.health = 6
            self.in_game_image = pygame.image.load('graphics/character/normalEnemy/Fairy2.png').convert_alpha()
            self.in_game_image = pygame.transform.scale(self.in_game_image, (self.size_x, self.size_y))
        else:
            self.name = 'Leader_Maid'
            self.normal_enemy_shooting_separate_parameter = 300
            self.health = 9
            self.in_game_image = pygame.image.load('graphics/character/normalEnemy/Fairy3.png').convert_alpha()
            self.in_game_image = pygame.transform.scale(self.in_game_image, (self.size_x, self.size_y))

    def draw(self, screen):
        normal_enemy_rect = self.in_game_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        screen.blit(self.in_game_image, normal_enemy_rect)
        # pygame.draw.rect(screen, (0, 255, 0), self.rect)

    def move(self, horizontal):
        # parameters
        if self.type == 1:
            speed = 1
        elif self.type == 2:
            speed = 2
        else:
            speed = 3
        dx = 0
        dy = 0

        if self.init_y == self.screen_height:
            dy -= speed * 2
        else:
            dy += speed * 2
        if horizontal:
            dx -= speed
        else:
            dx += speed
        self.rect.move_ip(dx, dy)

    def destroy(self):
        if self.rect.x < -100 or \
                self.rect.x > self.screen_width + 100 or \
                self.rect.y < -100 or \
                self.rect.y > self.screen_height + 100 or \
                self.health <= 0:
            self.kill()

    def kill(self):
        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(0, 0, -100, -100)
        super().kill()

    def update(self, horizontal, screen):
        self.move(horizontal)
        self.draw(screen)
        self.destroy()
