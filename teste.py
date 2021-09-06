import pygame
from pygame.locals import *
import sys
from root import MAIN_DIR

pygame.init()

# Classes
class Screen:
    screenWidth = int(1140 - 1140 / 5) 
    screenHeight = int(724 - 724 / 5)
    screen = pygame.display.set_mode((screenWidth, screenHeight))

class Player(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY):
        print('inciciou')
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        for c in range(5):
            imageLocal =  f'{MAIN_DIR}/images/heroi/character{c}.png'
            self.sprites.append(pygame.image.load(imageLocal))

        self.defaultMove = 'left'

        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.playerX = playerX
        self.playerY = playerY

        self.rect = self.image.get_rect()
        self.rect.topleft = self.playerX, self.playerY #100, 456

    def changeSide(self, side):
        if side == 'left':
            self.defaultMove = side
            self.sprites = []
            for c in range(5):
                imageLocal = pygame.image.load(imagesFolder + '/heroi/character'+ str(c) +'.png')

                self.sprites.append(pygame.transform.flip(imageLocal, True, False))

        if side == 'right':
            self.defaultMove = side
            self.sprites = []
            for c in range(5):
                imageLocal = pygame.image.load('./images/heroi/character'+ str(c) +'.png')
                self.sprites.append(imageLocal)



    def stopped(self):
        if self.playerY < 456:
            self.playerY += 10
            if self.currentSprite != 8:
                self.currentSprite = 8
        else:
            if self.currentSprite > 0:
                self.currentSprite = 0

        self.image = self.sprites[int(self.currentSprite)]
        self.rect.topleft = self.playerX, self.playerY #100, 456
        self.currentSprite += 0.2


    def walk(self, type):
        self.changeSide(type)
        if type == 'right':
            self.playerX += 10
        if type == 'left':
            self.playerX -= 10

        if self.currentSprite > 4 or self.currentSprite < 1:
            self.currentSprite = 1

        self.image = self.sprites[int(self.currentSprite)]
        self.rect.topleft = self.playerX, self.playerY #100, 456
        self.currentSprite += 0.5
    
    def climb(self):
        if self.playerX > 100:
            self.playerY -= 10
            if self.currentSprite < 6 or self.currentSprite > 7:
                self.currentSprite = 6
            
            self.image = self.sprites[int(self.currentSprite)]
            self.rect.topleft = self.playerX, self.playerY
            self.currentSprite += 0.3



# ======| Variables |====== #
bg = pygame.image.load('./images/cenario02.png')
backgroundImage = pygame.transform.smoothscale(bg, (Screen.screenWidth, Screen.screenHeight))

playerSprites = pygame.sprite.Group()
player = Player(100, 456)
playerSprites.add(player)

# Functions

def movePlayer():
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.walk('right')
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        player.walk('left')
    elif pygame.key.get_pressed()[pygame.K_UP]:
        player.climb()
    else:
        player.stopped()

while True:
    Screen.screen.blit(backgroundImage, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    playerSprites.draw(Screen.screen)

    movePlayer()

    pygame.display.flip()

pygame.quit()