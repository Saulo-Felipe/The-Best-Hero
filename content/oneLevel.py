import pygame
import os
from root import MAIN_DIR

def oneLevel(screen):

    playerRightLeft = pygame.image.load(MAIN_DIR + '/images/heroi/character-right-left.png').convert_alpha()

    class MoveBackground:
        x = 0
        y = 0

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.allSpriteSheet = []

            for i in range(5):
                self.allSpriteSheet.append(playerRightLeft.subsurface((38*i, 0), (38, 70)))
            
            self.currentIndex = 0
            self.image = self.allSpriteSheet[int(self.currentIndex)]
            self.rect = self.image.get_rect(center=(100, 610))

            self.currentPosition = 'stopped'

        def update(self, movimentType):
            if int(self.currentIndex) == 4:
                self.currentIndex = 0
            
            if movimentType == 'stopped' and self.currentPosition != movimentType:
                self.image = self.allSpriteSheet[0]
            elif movimentType != "stopped":
                if movimentType == 'left' and movimentType != self.currentPosition:
                    for e in range(len(self.allSpriteSheet)):
                        loopSprite = playerRightLeft.subsurface((38*e, 0), (38, 70))
                        self.allSpriteSheet[e] = pygame.transform.flip(loopSprite, True, False)
                        
                elif movimentType == 'right' and movimentType != self.currentPosition:
                    for i in range(5):
                        self.allSpriteSheet[i] = playerRightLeft.subsurface((38*i, 0), (38, 70))

                self.currentIndex += 0.4
                self.image = self.allSpriteSheet[int(self.currentIndex)]

            self.currentPosition = movimentType

    def movePlayer():
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            MoveBackground.x += 10
            allSprites.update('left')
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            MoveBackground.x -= 10
            allSprites.update('right')
        elif pygame.key.get_pressed()[pygame.K_UP]:
            print('Para cima')
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            print('Para baixo')
        else:
            allSprites.update('stopped')
    
    # ======| Variables |====== #
    allSprites = pygame.sprite.Group()
    player = Player()
    allSprites.add(player)

    background = pygame.image.load(MAIN_DIR + '/images/levels/level01-background.png')
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        movePlayer()
        screen.blit(background, (MoveBackground.x, MoveBackground.y))

        allSprites.draw(screen)

        pygame.display.flip()
    
    return