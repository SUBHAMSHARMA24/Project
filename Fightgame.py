import pygame
import random

pygame.init()  # initialisation of pygame

SIZE = WIDTH, HEIGHT = 1000, 690
SCREEN = pygame.display.set_mode(SIZE)

# RGB color code
WHITE = 255, 255, 255
RED = 255, 0, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

bulletsound = pygame.mixer.Sound("D:/Game/assets/images/Shoot.wav")
enemysound = pygame.mixer.Sound("D:/Game/assets/images/Shoot1.wav")


def homeScreen():
    font = pygame.font.Font("D:/Game/assets/Font/HALO____.ttf", 40)
    text = font.render("Welcome to Space Shooter", True, WHITE)

    font_2 = pygame.font.SysFont("None", 90)
    text_2 = font_2.render("Press SPACE to Start Game", True, WHITE)

    while True:
        eventList = pygame.event.get()
        for event in eventList:
            # print(event)
            if event.type == pygame.QUIT:
                # Quit pygame
                pygame.quit()
                # QuitPython
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        SCREEN.blit(text, (100, 250))
        SCREEN.blit(text_2, (100, 350))
        pygame.display.flip()


def playerhealth(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Health: {count}", True, BLACK)
    SCREEN.blit(text, (10, 500))


def gameOver():
    font = pygame.font.SysFont(None, 100)
    text_1 = font.render("Game Over", True, RED)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
            # print(event)
            if event.type == pygame.QUIT:
                # Quit pygame
                pygame.quit()
                # QuitPython
                quit()

        SCREEN.blit(text_1, (300, 300))
        pygame.display.flip()


def main():
    SCREEN.fill(WHITE)
    move_x = 0

    ship = pygame.image.load("D:/Game/assets/images/hero ship.png")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH // 2 - ship_w // 2
    ship_y = HEIGHT - ship_h

    enemyship = pygame.image.load("D:/Game/assets/images/enemy ship.png")
    eship_w = enemyship.get_width()
    eship_h = enemyship.get_height()

    enemyList = []
    nrows = 3
    ncols = WIDTH // eship_w

    # Bullet Code
    bullet_y = ship_y
    bullet_w = 5
    bullet_h = 10
    moveBullet = 0

    for i in range(nrows):
        for j in range(ncols):
            enmX = eship_w * j
            enmY = eship_h * i
            enemyRect = pygame.Rect(enmX, enmY, eship_w, eship_h)
            enemyList.append(enemyRect)
            # enemyList.append([enmX, enmY])

    random_enemy = random.choice(enemyList)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_x = random_enemy.x + eship_w // 2
    enemy_bullet_y = random_enemy.bottom - 10

    playerHealthcount = 100

    while True:
        bullet_x = ship_x + ship_w // 2 - 2  # // to get integer value
        eventList = pygame.event.get()
        for event in eventList:
            # print(event)
            if event.type == pygame.QUIT:
                # Quit pygame
                pygame.quit()
                # QuitPython
                quit()

            # KEYDOWN -  Pressing a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 6
                elif event.key == pygame.K_LEFT:
                    move_x = -6
                elif event.key == pygame.K_SPACE:
                    moveBullet = -10
                    bulletsound.play()

            else:
                move_x = 0

        SCREEN.fill(WHITE)

        bullet_rect = pygame.draw.rect(SCREEN, RED, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += moveBullet
        SCREEN.blit(ship, (ship_x, ship_y))
        ship_x += move_x

        ship_rect = pygame.Rect(ship_x, ship_y, ship_w, ship_h)

        enemyBullet = pygame.draw.rect(SCREEN, BLUE, [enemy_bullet_x, enemy_bullet_y, enemy_bullet_w, enemy_bullet_h])
        enemy_bullet_y += 20
        for i in range(len(enemyList)):
            SCREEN.blit(enemyship, (enemyList[i].x, enemyList[i].y))

        for i in range(len(enemyList)):
            if bullet_rect.colliderect(enemyList[i]):
                del enemyList[i]
                bullet_y = ship_y
                moveBullet = 0
                break

        if bullet_y < 0:
            bullet_y = ship_y
            moveBullet = 0

        if enemy_bullet_y > HEIGHT:
            random_enemy = random.choice(enemyList)
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemy_bullet_y = random_enemy.bottom - 10
            enemysound.play()

        if enemyBullet.colliderect(ship_rect):
            playerHealthcount -= 1

        if playerHealthcount == 0:
            gameOver()

        playerhealth(playerHealthcount)
        # updates the Screen
        pygame.display.flip()


homeScreen()
