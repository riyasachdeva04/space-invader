import pygame
import random
import math

pygame.init() #initialize

screen = pygame.display.set_mode((800, 600)) #create screen

running = True

#tile and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#initial score

score_value = 0 
font = pygame.font.Font('freesansbold.ttf', 64)

testX = 10
testY = 10

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))
#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

#bg
background = pygame.image.load('green-space-universe-background.jpg')

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2) + math.pow((enemyY-bulletY), 2))
    if distance < 27:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#game loop
while running:

    screen.fill((0, 70, 0)) #green
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.KEYDOWN:
            print('A key pressed')
            if event.key == pygame.K_LEFT:
                print('Left arrow')
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print('Right arrow')
                playerX_change = 0.3

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                print("Key released")
                playerX_change = 0


    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    #enemy movement
    for i in range(num_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'


    show_score(testX, testY)
    player(playerX, playerY)
    pygame.display.update()
