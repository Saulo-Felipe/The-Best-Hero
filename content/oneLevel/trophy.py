import pygame
from root import MAIN_DIR

imageTrophy = pygame.image.load(MAIN_DIR + "/images/levels/trophy.png")


class Trophy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.positionX = 10000
        self.positionY = 484

        self.frame = []
        for c in range(4):
            cutImage = imageTrophy.subsurface((c*125, 0), (125, 161))
            self.frame.append(cutImage.convert_alpha())
        
        self.index = 0
        self.image = self.frame[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.positionX, self.positionY)
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self, isMoving):
        
        if self.index > 3.9:
            self.index = 0

        self.index += 0.05

        if isMoving == "right":
            self.positionX -= 6
        elif isMoving == "left":
            self.positionX += 6
        
        self.image = self.frame[int(self.index)]
        self.rect.topleft = (self.positionX, self.positionY)
        

            

