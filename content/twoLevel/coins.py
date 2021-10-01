import pygame
from root import MAIN_DIR

class CoinImage:
    coin = pygame.image.load(MAIN_DIR + "/images/levels/coin.png")

class animationCoin:
    position = "Top"


class Coins(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)

        self.X = X # Fixa
        self.Y = Y
        self.coinX = X #Dinâmica
        self.coinY = Y

        self.image = CoinImage.coin
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (self.X, self.Y)
    
    def update(self, isMoving):
        if isMoving == "right":
            self.coinX -= 6

        elif isMoving == "left":
            self.coinX += 6
        
        if self.coinY == self.Y:
            animationCoin.position = "Top"
        elif self.coinY == self.Y - 30:
            animationCoin.position = "Bottom"

        if animationCoin.position == "Top":
            self.coinY -= 1
        elif animationCoin.position == "Bottom":
            self.coinY += 1


        self.rect.topleft = (self.coinX, self.coinY)

