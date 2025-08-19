import random

import pygame
from pygame import mixer
import pygame_menu

from bullet import Bullet
from littleDevil import LittleDevil
from marisa import Marisa
from patchouli import Patchouli
from normalEnemy import NormalEnemy

pygame.init()
mixer.init()

# parameters of game environment
# display settings
screen_width = 1920
screen_height = 1080
fps = 60
fps_clock = pygame.time.Clock()
text_size = 50

# VIP list
VIP_list = ["Marisa", "Little_Devil", "Patchouli"]  # use to store VIP character

screen = pygame.display.set_mode(
    (screen_width, screen_height),  # set screen size
    # pygame.FULLSCREEN  # full screen
)
pygame.display.set_caption('game')

# load BGM
BGM1 = pygame.mixer.Sound("audio/BGM/BGMStage1.mp3")
BGM2 = pygame.mixer.Sound("audio/BGM/BGMStage2.mp3")
BGM3 = pygame.mixer.Sound("audio/BGM/BGMStage3.mp3")
menu_BGM = pygame.mixer.Sound("audio/BGM/MainMenu.mp3")

# load Ending screen
bad_ending_image = pygame.image.load("graphics/Ending/BadEnding.png").convert_alpha()
end_stage1_image = pygame.image.load("graphics/Ending/EndStage1.png").convert_alpha()
end_stage2_image = pygame.image.load("graphics/Ending/EndStage2.png").convert_alpha()
end_stage3_image = pygame.image.load("graphics/Ending/EndStage3.png").convert_alpha()

# load background
# note convert_alpha() can significantly improve the performance
background1 = pygame.image.load("graphics/background/Background1.png").convert_alpha()
background1 = pygame.transform.scale(background1, (screen_width, screen_height))
background2 = pygame.image.load("graphics/background/Background2.png").convert_alpha()
background2 = pygame.transform.scale(background2, (screen_width, screen_height))
background3 = pygame.image.load('graphics/background/Background3.png').convert_alpha()
background3 = pygame.transform.scale(background3, (screen_width, screen_height))

# load copyright statement
copyright_statement = pygame.image.load('graphics/copyrightStatement.png').convert_alpha()

# load character images
# plot image
little_devil_plot_image = pygame.image.load(
    "graphics/character/littleDevil/littleDevilPlot.png").convert_alpha()
little_devil_plot_image = pygame.transform.scale(little_devil_plot_image,
                                                 (little_devil_plot_image.get_rect().width * 1.5,
                                                  little_devil_plot_image.get_rect().height * 1.5))

patchouli_plot_image = pygame.image.load(
    "graphics/character/patchouli/PatchouliPlot.png").convert_alpha()
# marisa
marisa_plot_image = pygame.image.load('graphics/character/marisa/marisaPlot.png').convert_alpha()
marisa_plot_image = pygame.transform.scale(marisa_plot_image, (marisa_plot_image.get_rect().width * 2,
                                                               marisa_plot_image.get_rect().height * 2))

# load font
pygame.font.init()
font = pygame.font.SysFont("Module3/Assignment/font/VPPixel-Simplified.otf", 50)

# text list
# game stage
game_text = None
text_rect = None

# Object list
# create player
player = Marisa(50, 540)

# create Little_Devil
little_devil = LittleDevil(1800, 540)

# create Patchouli
patchouli = Patchouli(1800, 540)

# create normal enemies
normal_enemy_list = []

# bullets
bullet_list_marisa = []
bullet_list_enemy = []
bullet_list = [bullet_list_marisa, bullet_list_enemy]

# little_devil direction
little_devil_vertical = True  # vertical direction
little_devil_horizontal = True  # horizontal direction

# patchouli direction
patchouli_vertical = True  # vertical direction
patchouli_horizontal = True  # horizontal direction


# Volume control
def volume_control(music_player):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                music_player.set_volume(music_player.get_volume() + 0.1)
            if event.key == pygame.K_F6:
                music_player.set_volume(music_player.get_volume() - 0.1)


# create bullets
def create_bullet(creator):
    if creator.name == "Marisa":
        bullet1 = Bullet(creator.rect.centerx, creator.rect.centery, creator, screen)
        bullet_list_marisa.append(bullet1)
        for character in VIP_list:
            if character == creator.name:
                bullet2 = Bullet(creator.rect.centerx, creator.rect.centery - 100, creator, screen)
                bullet_list_marisa.append(bullet2)
                bullet3 = Bullet(creator.rect.centerx, creator.rect.centery + 100, creator, screen)
                bullet_list_marisa.append(bullet3)
    else:
        bullet1 = Bullet(creator.rect.centerx, creator.rect.centery, creator, screen)
        bullet_list_enemy.append(bullet1)
        for character in VIP_list:
            if character == creator.name:
                bullet2 = Bullet(creator.rect.centerx, creator.rect.centery - 100, creator, screen)
                bullet_list_enemy.append(bullet2)
                bullet3 = Bullet(creator.rect.centerx, creator.rect.centery + 100, creator, screen)
                bullet_list_enemy.append(bullet3)


# create normal enemies
def create_normal_enemy():
    create_flag = random.randint(1, 50)  # use to determine if normal enemy should be created
    create_type = random.randint(1, 3)  # use to determine type of normal enemy
    x_coordinate = random.randint(1500, screen_width)  # use to determine x coordinate of normal enemy
    y_flag = random.randint(0, 1)  # use to determine if normal enemy should be created at top or bottom
    if y_flag == 0:
        y_coordinate = 0
    else:
        y_coordinate = screen_height
    if create_flag == 1:
        normal_enemy_list.append(
            NormalEnemy(x_coordinate, y_coordinate, create_type, screen_width, screen_height))


# move bullets
def move_bullets(all_bullets):
    for bullets in all_bullets:
        for bullet in bullets:
            bullet.move()
            bullet.destroy()
            bullet.draw()


# hit detection
def hit_detection(detect_character, bullets):
    for bullet in bullets:
        if bullet.rect.colliderect(detect_character.rect):
            detect_character.health -= 1
            bullet.kill()
            return True
    return False


# enemy attack
def enemy_attack(current_character):
    if current_character.shooting_separate_variable == 0:
        create_bullet(current_character)
        current_character.shooting_separate_variable = 1
    if current_character.shooting_separate_variable > 0:
        current_character.shooting_separate_variable += 1
    if current_character.shooting_separate_variable >= little_devil.shooting_separate_parameter:
        current_character.shooting_separate_variable = 0


# show plot
def show_plot(current_stage):
    if current_stage == 1:
        screen.blit(marisa_plot_image, (0, 0))


# Show ending
def show_ending(current_stage, defeat_flag):
    pygame.time.set_timer(pygame.USEREVENT + 3, 3000)
    show_flag = True
    while show_flag:
        if current_stage == 1:
            if defeat_flag:
                screen.blit(bad_ending_image, (0, 0))
            else:
                screen.blit(end_stage1_image, (0, 0))
        elif current_stage == 2:
            if defeat_flag:
                screen.blit(bad_ending_image, (0, 0))
            else:
                screen.blit(end_stage2_image, (0, 0))
        elif current_stage == 3:
            if defeat_flag:
                screen.blit(bad_ending_image, (0, 0))
            else:
                screen.blit(end_stage3_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 3:
                show_flag = False
        pygame.display.update()


# draw background
def draw_background(current_stage):
    if current_stage == 1:
        screen.blit(background1, (0, 0))
    elif current_stage == 2:
        screen.blit(background2, (0, 0))
    elif current_stage == 3:
        screen.blit(background3, (0, 0))


# draw basic information
def draw_basic_information(current_character, display_screen, current_stage):
    # draw player's health
    player_health_text = font.render("Player: " + str(current_character.health), True, (255, 0, 0))
    health_text_rect = player_health_text.get_rect(center=(text_size + 50, text_size))
    display_screen.blit(player_health_text, health_text_rect)
    # draw current stage
    current_stage_text = font.render("Stage: " + str(current_stage), True, (255, 0, 0))
    current_stage_text_rect = current_stage_text.get_rect(center=(text_size + 50, 50 + text_size))
    display_screen.blit(current_stage_text, current_stage_text_rect)


def draw_basic_information_type2(current_character, display_screen, current_stage, count_down):
    # draw player's health
    player_health_text = font.render("Player: " + str(current_character.health), True, (255, 0, 0))
    health_text_rect = player_health_text.get_rect(center=(text_size + 50, text_size))
    display_screen.blit(player_health_text, health_text_rect)
    # draw current stage
    current_stage_text = font.render("Stage: " + str(current_stage), True, (255, 0, 0))
    current_stage_text_rect = current_stage_text.get_rect(center=(text_size + 50, 50 + text_size))
    display_screen.blit(current_stage_text, current_stage_text_rect)
    # draw count down
    count_down_text = font.render("Hold: " + str(count_down), True, (255, 0, 0))
    count_down_text_rect = count_down_text.get_rect(center=(text_size + 100, 100 + text_size))
    display_screen.blit(count_down_text, count_down_text_rect)


# boss information
def draw_boss_information(current_character, display_screen):
    health_rect = pygame.Rect(50, 150, current_character.health, 50)
    pygame.draw.rect(display_screen, (255, 0, 0), health_rect)
    # boss_health_text = font.render("Boss: " + str(current_character.health), True, (0, 0, 0))
    # health_text_rect = boss_health_text.get_rect(center=(screen_width / 2, 100 + text_size))
    # display_screen.blit(boss_health_text, health_text_rect)


# draw copyright statement
def draw_copyright_statement(display_screen):
    display_screen.blit(copyright_statement, (0, screen_height - copyright_statement.get_rect().height))
    pygame.display.update()


# stage1 plot
def stage1_plot():
    # background
    draw_background(stage)
    pygame.display.update()


# show boss image, temporary function
def show_boss_image(stage):
    if stage == 2:
        screen.blit(little_devil_plot_image, (screen_width / 2 - little_devil_plot_image.get_rect().width / 2,
                                              screen_height / 2 - little_devil_plot_image.get_rect().height / 2))
        pygame.display.update()
    elif stage == 3:
        screen.blit(patchouli_plot_image, (screen_width / 2 - patchouli_plot_image.get_rect().width / 2,
                                           screen_height / 2 - patchouli_plot_image.get_rect().height / 2))
        pygame.display.update()


# main_menu section
def start_game():
    main_menu.disable()
    global player
    player = Marisa(50, 540)
    global stage
    stage = 1


# main menu
main_menu = pygame_menu.Menu('Marisa stole something important', 960, 540,
                             theme=pygame_menu.themes.THEME_DEFAULT)
main_menu.add.button('Start', start_game)
main_menu.add.button('Quit', pygame_menu.events.EXIT)
main_menu.center_content()

# game loop variable
game_run = True
stage1_run = False
plot1 = False
stage2_run = False
plot2 = False
stage3_run = False
plot3 = False
copyright_flag = False

# stage
stage = 0

# copyright statement
pygame.time.set_timer(pygame.USEREVENT, 5000)
copyright_flag = True
while copyright_flag:
    draw_copyright_statement(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            copyright_flag = False
            stage1_run = False
            stage2_run = False
            stage3_run = False
            game_run = False
        if event.type == pygame.USEREVENT:
            copyright_flag = False

while game_run:

    # main_menu
    if stage == 0:
        main_menu.enable()
        menu_BGM.play()
        main_menu.mainloop(screen)
        menu_BGM.stop()

    if stage == 1:

        stage1_run = True

        # count down
        count_down_time = 6000

        # BGM
        BGM1.play(-1)

        show_plot1 = False

        while stage1_run:

            # volume control
            volume_control(BGM1)

            # draw background1
            draw_background(stage)

            # information render
            draw_basic_information_type2(player, screen, stage, int(count_down_time / 100))

            # count down
            count_down_time -= 1

            # plot
            if show_plot1:
                show_plot(stage)

            # move player
            player.move(screen_width, screen_height)

            # draw player
            player.draw(screen)

            # create normal enemies
            create_normal_enemy()

            # enemy move
            for enemy in normal_enemy_list:
                direction_flag = random.randint(0, 1)  # use to determine if normal enemy should move to left or right
                enemy.update(direction_flag, screen)

            # player attack
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_z]:
                if player.shooting_separate_variable == 0:
                    create_bullet(player)
                    player.shooting_separate_variable = 1
            if player.shooting_separate_variable > 0:
                player.shooting_separate_variable += 1
            if player.shooting_separate_variable >= player.shooting_separate_parameter:
                player.shooting_separate_variable = 0

            # enemy attack
            for enemy in normal_enemy_list:
                if enemy.normal_enemy_shooting_separate_variable == 0:
                    create_bullet(enemy)
                    enemy.normal_enemy_shooting_separate_variable = random.randint(10, 100)
                if enemy.normal_enemy_shooting_separate_variable > 0:
                    enemy.normal_enemy_shooting_separate_variable += 4
                if enemy.normal_enemy_shooting_separate_variable >= enemy.normal_enemy_shooting_separate_parameter:
                    enemy.normal_enemy_shooting_separate_variable = 0

            # move bullets
            move_bullets(bullet_list)

            # hit detection
            # player
            if player.hit_variable == 0:
                hit_flag = hit_detection(player, bullet_list_enemy)
                if hit_flag:
                    player.hit_variable = 1
            if player.hit_variable > 0:
                player.hit_variable += 1
            if player.hit_variable >= player.hit_parameter:
                player.hit_variable = 0
            # enemy
            for enemy in normal_enemy_list:
                hit_flag = hit_detection(enemy, bullet_list_marisa)
                if hit_flag:
                    enemy.hit_variable = 1
                if enemy.hit_variable > 0:
                    enemy.hit_variable += 1
                if enemy.hit_variable >= enemy.hit_parameter:
                    enemy.hit_variable = 0

            # end detection
            if player.health <= 0:
                show_ending(stage, True)
                stage1_run = False
                stage = 0
            if count_down_time <= 0:
                show_ending(stage, False)
                stage1_run = False
                stage = 2

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage1_run = False
                    game_run = False

            # display update
            pygame.display.update()

        BGM1.stop()

    elif stage == 2:

        # ensure boss have health
        if little_devil.health <= 0:
            little_devil = LittleDevil(1800, 540)

        stage2_run = True

        # BGM
        BGM2.play(-1)

        # Boss image
        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
        boss_image_flag = True
        while boss_image_flag:
            # volume control
            volume_control(BGM2)

            # draw background
            draw_background(stage)
            show_boss_image(stage)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    boss_image_flag = False
                    stage1_run = False
                    stage2_run = False
                    stage3_run = False
                    game_run = False
                if event.type == pygame.USEREVENT + 1:
                    boss_image_flag = False

        while stage2_run:

            # volume control
            volume_control(BGM2)

            # draw background
            draw_background(stage)

            # information render
            draw_basic_information(player, screen, stage)
            draw_boss_information(little_devil, screen)

            # move player
            player.move(screen_width, screen_height)

            # draw player
            player.draw(screen)

            # draw Little_Devil
            little_devil.draw(screen)

            # move Little_Devil
            little_devil.move(little_devil_vertical, little_devil_horizontal)
            if little_devil.rect.x < 1200:
                little_devil_horizontal = False
            if little_devil.rect.x > 1800:
                little_devil_horizontal = True
            if little_devil.rect.y < 100:
                little_devil_vertical = False
            if little_devil.rect.y > 900:
                little_devil_vertical = True

            # player attack
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_z]:
                if player.shooting_separate_variable == 0:
                    create_bullet(player)
                    player.shooting_separate_variable = 1
            if player.shooting_separate_variable > 0:
                player.shooting_separate_variable += 1
            if player.shooting_separate_variable >= player.shooting_separate_parameter:
                player.shooting_separate_variable = 0

            # Little_Devil attack
            enemy_attack(little_devil)

            # move bullets
            move_bullets(bullet_list)

            # hit detection
            # player
            if player.hit_variable == 0:
                hit_flag = hit_detection(player, bullet_list_enemy)
                if hit_flag:
                    player.hit_variable = 1
            if player.hit_variable > 0:
                player.hit_variable += 1
            if player.hit_variable >= player.hit_parameter:
                player.hit_variable = 0
            # little_devil
            if little_devil.hit_variable == 0:
                hit_flag = hit_detection(little_devil, bullet_list_marisa)
                if hit_flag:
                    little_devil.hit_variable = 1
            if little_devil.hit_variable > 0:
                little_devil.hit_variable += 1
            if little_devil.hit_variable >= little_devil.hit_parameter:
                little_devil.hit_variable = 0

            # end detection
            if player.health <= 0:
                show_ending(stage, True)
                stage2_run = False
                stage = 0
            if little_devil.health <= 0:
                show_ending(stage, False)
                stage2_run = False
                stage = 3

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage2_run = False
                    game_run = False

            # display update
            pygame.display.update()

        BGM2.stop()

    elif stage == 3:

        # ensure boss have health
        if patchouli.health <= 0:
            patchouli = Patchouli(1800, 540)

        stage3_run = True
        # BGM
        BGM3.play(-1)

        # Boss image
        pygame.time.set_timer(pygame.USEREVENT + 2, 3000)
        boss_image_flag = True
        while boss_image_flag:
            # volume control
            volume_control(BGM2)

            # draw background
            draw_background(stage)
            show_boss_image(stage)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    boss_image_flag = False
                    stage1_run = False
                    stage2_run = False
                    stage3_run = False
                    game_run = False
                if event.type == pygame.USEREVENT + 2:
                    boss_image_flag = False

        while stage3_run:

            # volume control
            volume_control(BGM3)

            # draw background
            draw_background(stage)

            # information render
            draw_basic_information(player, screen, stage)
            draw_boss_information(patchouli, screen)

            # move player
            player.move(screen_width, screen_height)

            # draw player
            player.draw(screen)

            # draw patchouli
            patchouli.draw(screen)

            # move patchouli
            patchouli.move(patchouli_vertical, patchouli_horizontal)
            if patchouli.rect.x < 1200:
                patchouli_horizontal = False
            if patchouli.rect.x > 1800:
                patchouli_horizontal = True
            if patchouli.rect.y < 100:
                patchouli_vertical = False
            if patchouli.rect.y > 900:
                patchouli_vertical = True

            # player attack
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_z]:
                if player.shooting_separate_variable == 0:
                    create_bullet(player)
                    player.shooting_separate_variable = 1
            if player.shooting_separate_variable > 0:
                player.shooting_separate_variable += 1
            if player.shooting_separate_variable >= player.shooting_separate_parameter:
                player.shooting_separate_variable = 0

            # patchouli attack
            enemy_attack(patchouli)

            # move bullets
            move_bullets(bullet_list)

            # hit detection
            # player
            if player.hit_variable == 0:
                hit_flag = hit_detection(player, bullet_list_enemy)
                if hit_flag:
                    player.hit_variable = 1
            if player.hit_variable > 0:
                player.hit_variable += 1
            if player.hit_variable >= player.hit_parameter:
                player.hit_variable = 0
            # patchouli
            if patchouli.hit_variable == 0:
                hit_flag = hit_detection(patchouli, bullet_list_marisa)
                if hit_flag:
                    patchouli.hit_variable = 1
            if patchouli.hit_variable > 0:
                patchouli.hit_variable += 1
            if patchouli.hit_variable >= patchouli.hit_parameter:
                patchouli.hit_variable = 0

            # end detection
            if player.health <= 0:
                show_ending(stage, True)
                stage3_run = False
                stage = 0
            if patchouli.health <= 0:
                show_ending(stage, False)
                stage3_run = False
                stage = 0

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage3_run = False
                    game_run = False

            # display update
            pygame.display.update()

        BGM3.stop()

# quit pygame
pygame.quit()
