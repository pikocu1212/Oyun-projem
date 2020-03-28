import pygame
import random

# Intiallize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship1.png")
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load("spaceship2.png")
playerX = 370
playerY = 480
playerX_change = 0
# Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 2.5
enemyY_change = 40

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


def fire_bullet(x,y):
    global  bullet_state
    bullet_state = "fire"
    screen.blit (bulletImg, (x , y ))

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2.5
        if event.key == pygame.K_RIGHT:
            playerX_change =  2.5
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready":
                # Get the current x cordinate of the spaceship
               bulletX = playerX
               fire_bullet(bulletX,bulletY)
               bulletY_change = -6.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change =  0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 +
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enmy Movemnt
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2.5
        enemyY += enemyY_change
    elif enemyX >= 736:
       enemyX_change = -2.5
       enemyY += enemyY_change


    # Bullet Movment
    if bulletY <=0 :
        bulletY =480
        bullet_state ="ready"


    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY += bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()