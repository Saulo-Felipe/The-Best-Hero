# cutImage = monsterImages.allMonsters.subsurface((c*71, 0), (71, 52))
import pygame
from root import MAIN_DIR

monsterSpriteSheet = pygame.image.load(MAIN_DIR + "/images/monsters/allMonsters.png")
bigMonster = pygame.image.load(MAIN_DIR + "/images/monsters/gigant-monster-sprite.png")

class animationMonster:
    monster = "right"

class Monster(pygame.sprite.Sprite):
    def __init__(self, start, end, floor, Type):
        pygame.sprite.Sprite.__init__(self)
        
        y = 0
        x = 71
        altura = 52
        self.time = 4
        self.velocity = 0.1

        if Type == 0:
            y = 0
        elif Type == 1:
            y = 86
        elif Type == 2:
            y = 291
            x = 112
            altura = 57
            self.velocity = 0.15
        elif Type == 3:
            y = 0
            x = 140
            altura = 144
            self.time = 8
            self.velocity = 0.15



        self.start = start # Fixo
        self.end = end - 71
        self.monsterStart = start # Dinâmico
        self.monsterEnd = end
        self.floor = floor
        self.moveDistance = 0
        self.direction = "right"

        self.frame = []
        for c in range(self.time):
            if Type == 3:
                cutImage = bigMonster.subsurface((c*x, y), (x, altura))
            else:
                cutImage = monsterSpriteSheet.subsurface((c*x, y), (x, altura))
            self.frame.append(cutImage.convert_alpha())

        self.index = 0
        self.image = self.frame[self.index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (start, floor)
    
    def update(self, isMoving):

        # Movimentos do player
        if isMoving == "right":
            self.monsterStart -= 6
        elif isMoving == "left":
            self.monsterStart += 6
            
        # Movimentos automatico do monstro
        if self.direction == "right":
            self.moveDistance += 2
            self.monsterStart += 2
            self.image = self.image
            self.image = self.frame[int(self.index)]
            
        elif self.direction == "left":
            self.moveDistance -= 2
            self.monsterStart -= 2
            self.image = pygame.transform.flip(self.frame[int(self.index)], True, False)

        # Modificação do lado de movimento
        if self.direction == "right" and self.moveDistance >= self.end - self.start:
            self.direction = "left"
        elif self.direction == "left" and self.moveDistance <= 0:
            self.direction = "right"
            
        # Animation
        if self.index >= self.time-1:
            self.index = 0

        self.index += self.velocity
        self.mask = pygame.mask.from_surface(self.image)

        if self.monsterStart <= self.start:
            animationMonster.monster = "left"
        elif self.monsterEnd >= self.end:
            animationMonster.monster = "right"
        
        self.rect.topleft = (self.monsterStart, self.floor)

        


