import pygame
from root import MAIN_DIR

monsterDesert = pygame.image.load(MAIN_DIR + "/images/monsters/monster-desert.png")
monsterDesert2 = pygame.image.load(MAIN_DIR + "/images/monsters/monster-desert2.png")
birdMonster = pygame.image.load(MAIN_DIR + "/images/monsters/bird-monster.png")
birdMonster2 = pygame.image.load(MAIN_DIR + "/images/monsters/bird-monster2.png")
plansMonster = pygame.image.load(MAIN_DIR + "/images/monsters/plantMonster.png")
cactusMonster = pygame.image.load(MAIN_DIR + "/images/monsters/cactusMonster.png")
nightMonster = pygame.image.load(MAIN_DIR + "/images/monsters/nightMonster.png")
allMonster = pygame.image.load(MAIN_DIR + "/images/monsters/allMonsters.png")


class animationMonster:
    monster = "right"

class Monster(pygame.sprite.Sprite):
    def __init__(self, start, end, floor, Type):
        pygame.sprite.Sprite.__init__(self)
        
        y = 0
        x = 200
        altura = 149
        self.time = 12
        self.AnimationDelay = 0.1
        self.imageType = False
        self.isMove = False
        self.velocity = 2

        if Type == 0:
            self.imageType = monsterDesert
            self.AnimationDelay = 0.12
            self.isMove = True
        elif Type == 1:
            x = 75
            altura = 58
            self.time = 4
            self.imageType = birdMonster
            self.isMove = True
        elif Type == 2 or Type == 3:
            x = 225
            altura = 169
            self.AnimationDelay = 0.2
            self.imageType = plansMonster
            self.isMove = False
        elif Type == 4:
            altura = 168
            x = 225
            self.imageType = monsterDesert2
            self.AnimationDelay = 0.12
            self.isMove = True
        elif Type == 5:
            altura = 71
            x = 119
            self.time = 4
            self.imageType = birdMonster2
            self.isMove = True
            self.AnimationDelay = 0.2
            self.velocity = 4
        elif Type == 6:
            altura = 189
            x = 194
            self.time = 18
            self.imageType = nightMonster
            self.isMove = True
            self.AnimationDelay = 0.4
            self.velocity = 4
        elif Type == 7:
            altura = 52
            x = 71
            self.time = 4
            self.imageType = allMonster
            self.isMove = True
            self.AnimationDelay = 0.3
            self.velocity = 3
        elif Type == 8:
            y = 86
            altura = 52
            x = 71
            self.time = 4
            self.imageType = allMonster
            self.isMove = True
            self.AnimationDelay = 0.3
            self.velocity = 3


        if Type == 3:
            self.imageType = cactusMonster


        self.start = start # Fixo
        self.end = end - 71
        self.monsterStart = start # Dinâmico
        self.monsterEnd = end
        self.floor = floor
        self.moveDistance = 0
        self.direction = "right"

        self.frame = []
        for c in range(self.time):
            cutImage = self.imageType.subsurface((c*x, y), (x, altura))
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
        if self.isMove == True:
            if self.direction == "right":
                self.moveDistance += self.velocity
                self.monsterStart += self.velocity
                self.image = self.frame[int(self.index)]
                
            elif self.direction == "left":
                self.moveDistance -= self.velocity
                self.monsterStart -= self.velocity
                self.image = pygame.transform.flip(self.frame[int(self.index)], True, False)

            # Modificação do lado de movimento
            if self.direction == "right" and self.moveDistance >= self.end - self.start:
                self.direction = "left"
            elif self.direction == "left" and self.moveDistance <= 0:
                self.direction = "right"

            if self.monsterStart <= self.start:
                animationMonster.monster = "left"
            elif self.monsterEnd >= self.end:
                animationMonster.monster = "right"

            self.rect.topleft = (self.monsterStart, self.floor)
        else:
            self.image = self.frame[int(self.index)]
            self.rect.topleft = (self.monsterStart, self.floor)

        # Animation
        if self.index >= self.time-1:
            self.index = 0

        self.index += self.AnimationDelay
        self.mask = pygame.mask.from_surface(self.image)
