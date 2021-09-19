import pygame 
from root import MAIN_DIR
from random import randint

class monsterImages:
    allMonsters = pygame.image.load(MAIN_DIR + "/images/monsters/allMonsters.png")

class Moviments:
    monsterX = 2105
    between = {
        "start": 2105,
        "pos": 2105,
        "end": 3060-71,
        "side": "left"
    }

    monsterX2 = 3218
    between2 = {
        "start": 3218,
        "pos": 3218,
        "end": 4188-71,
        "side": "left"
    }

    monsterX3 = 4467
    between3 = {
        "start": 4467,
        "pos": 4467,
        "end": 6297-71,
        "side": "left"
    }

    monsterX4 = 5300
    between4 = {
        "start": 5300,
        "pos": 5300,
        "end": 6297-71,
        "side": "left"
    }

    monsterX5 = 5058
    between5 = {
        "start": 5058,
        "pos": 5058,
        "end": 5332-71,
        "side": "left"
    }



def restartGame():
    Moviments.monsterX = 2105
    Moviments.between = {
        "start": 2105,
        "pos": 2105,
        "end": 3060-71,
        "side": "left"
    }

    Moviments.monsterX2 = 3218
    Moviments.between2 = {
        "start": 3218,
        "pos": 3218,
        "end": 4188-71,
        "side": "left"
    }

    Moviments.monsterX3 = 4467
    Moviments.between3 = {
        "start": 4467,
        "pos": 4467,
        "end": 6297-71,
        "side": "left"
    }

    Moviments.monsterX4 = 5300
    Moviments.between4 = {
        "start": 5300,
        "pos": 5300,
        "end": 6297-71,
        "side": "left"
    }

    Moviments.monsterX5 = 5058
    Moviments.between5 = {
        "start": 5058,
        "pos": 5058,
        "end": 5332-71,
        "side": "left"
    }

def monsters(restart):
    if restart == True:
        restartGame()

    class Monster(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.monsterFrame = []

            for c in range(4):
                cutImage = monsterImages.allMonsters.subsurface((c*71, 0), (71, 52))
                self.monsterFrame.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.monsterFrame[self.frameIndex]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (300, 592)
        
        def update(self, isMoving):
            self.frameIndex += 0.1 

            if Moviments.between["side"] == "left":
                self.image = pygame.transform.flip(self.monsterFrame[int(self.frameIndex)], True, False)
            else:
                self.image = self.monsterFrame[int(self.frameIndex)]

            # Calcula movimento do player e subtrai/soma posição do monster            
            if isMoving == "right":
                Moviments.monsterX -= 5

            elif isMoving == "left":
                Moviments.monsterX += 5

            # Começo e fim do movimento automatico
            if Moviments.between["side"] == "left":
                Moviments.monsterX -= 2
                Moviments.between["pos"] -= 2

                if Moviments.between["pos"] <= Moviments.between["start"]:
                    Moviments.between["side"] = "right"

            elif Moviments.between["side"] == "right":
                Moviments.monsterX += 2
                Moviments.between["pos"] += 2
                
                if Moviments.between["pos"] >= Moviments.between["end"]:
                    Moviments.between["side"] = "left"


            if self.frameIndex > 3:
                self.frameIndex = 0

            self.rect.topleft = (Moviments.monsterX, 592)
    
    class Monster2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.monsterFrame = []

            for c in range(4):
                cutImage = monsterImages.allMonsters.subsurface((c*71, 86), (71, 52))
                self.monsterFrame.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.monsterFrame[self.frameIndex]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (300, 592)
        
        def update(self, isMoving):
            self.frameIndex += 0.1 

            if Moviments.between2["side"] == "left":
                self.image = pygame.transform.flip(self.monsterFrame[int(self.frameIndex)], True, False)
            else:
                self.image = self.monsterFrame[int(self.frameIndex)]

            # Calcula movimento do player e subtrai/soma posição do monster            
            if isMoving == "right":
                Moviments.monsterX2 -= 5

            elif isMoving == "left":
                Moviments.monsterX2 += 5

            # Começo e fim do movimento automatico
            if Moviments.between2["side"] == "left":
                Moviments.monsterX2 -= 2
                Moviments.between2["pos"] -= 2

                if Moviments.between2["pos"] <= Moviments.between2["start"]:
                    Moviments.between2["side"] = "right"

            elif Moviments.between2["side"] == "right":
                Moviments.monsterX2 += 2
                Moviments.between2["pos"] += 2
                
                if Moviments.between2["pos"] >= Moviments.between2["end"]:
                    Moviments.between2["side"] = "left"


            if self.frameIndex > 3:
                self.frameIndex = 0

            self.rect.topleft = (Moviments.monsterX2, 592)
            
    class Monster3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.monsterFrame = []

            for c in range(4):
                cutImage = monsterImages.allMonsters.subsurface((c*71, 86), (71, 52))
                self.monsterFrame.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.monsterFrame[self.frameIndex]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (300, 592)
        
        def update(self, isMoving):
            self.frameIndex += 0.1 

            if Moviments.between3["side"] == "left":
                self.image = pygame.transform.flip(self.monsterFrame[int(self.frameIndex)], True, False)
            else:
                self.image = self.monsterFrame[int(self.frameIndex)]

            # Calcula movimento do player e subtrai/soma posição do monster            
            if isMoving == "right":
                Moviments.monsterX3 -= 5

            elif isMoving == "left":
                Moviments.monsterX3 += 5

            # Começo e fim do movimento automatico
            if Moviments.between3["side"] == "left":
                Moviments.monsterX3 -= 3
                Moviments.between3["pos"] -= 3

                if Moviments.between3["pos"] <= Moviments.between3["start"]:
                    Moviments.between3["side"] = "right"

            elif Moviments.between3["side"] == "right":
                Moviments.monsterX3 += 3
                Moviments.between3["pos"] += 3
                
                if Moviments.between3["pos"] >= Moviments.between3["end"]:
                    Moviments.between3["side"] = "left"


            if self.frameIndex > 3:
                self.frameIndex = 0

            self.rect.topleft = (Moviments.monsterX3, 592)

    class Monster4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.monsterFrame = []

            for c in range(4):
                cutImage = monsterImages.allMonsters.subsurface((c*71, 0), (71, 52))
                self.monsterFrame.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.monsterFrame[self.frameIndex]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (300, 592)
        
        def update(self, isMoving):
            self.frameIndex += 0.1 

            if Moviments.between4["side"] == "left":
                self.image = pygame.transform.flip(self.monsterFrame[int(self.frameIndex)], True, False)
            else:
                self.image = self.monsterFrame[int(self.frameIndex)]

            # Calcula movimento do player e subtrai/soma posição do monster            
            if isMoving == "right":
                Moviments.monsterX4 -= 5

            elif isMoving == "left":
                Moviments.monsterX4 += 5

            # Começo e fim do movimento automatico
            if Moviments.between4["side"] == "left":
                Moviments.monsterX4 -= 2
                Moviments.between4["pos"] -= 2

                if Moviments.between4["pos"] <= Moviments.between4["start"]:
                    Moviments.between4["side"] = "right"

            elif Moviments.between4["side"] == "right":
                Moviments.monsterX4 += 2
                Moviments.between4["pos"] += 2
                
                if Moviments.between4["pos"] >= Moviments.between4["end"]:
                    Moviments.between4["side"] = "left"


            if self.frameIndex > 3:
                self.frameIndex = 0

            self.rect.topleft = (Moviments.monsterX4, 592)

    class Monster5(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.monsterFrame = []

            for c in range(4):
                cutImage = monsterImages.allMonsters.subsurface((c*71, 0), (71, 52))
                self.monsterFrame.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.monsterFrame[self.frameIndex]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (300, 292)
        
        def update(self, isMoving):
            self.frameIndex += 0.1 

            if Moviments.between5["side"] == "left":
                self.image = pygame.transform.flip(self.monsterFrame[int(self.frameIndex)], True, False)
            else:
                self.image = self.monsterFrame[int(self.frameIndex)]

            # Calcula movimento do player e subtrai/soma posição do monster            
            if isMoving == "right":
                Moviments.monsterX5 -= 5

            elif isMoving == "left":
                Moviments.monsterX5 += 5

            # Começo e fim do movimento automatico
            if Moviments.between5["side"] == "left":
                Moviments.monsterX5 -= 2
                Moviments.between5["pos"] -= 2

                if Moviments.between5["pos"] <= Moviments.between5["start"]:
                    Moviments.between5["side"] = "right"

            elif Moviments.between5["side"] == "right":
                Moviments.monsterX5 += 2
                Moviments.between5["pos"] += 2
                
                if Moviments.between5["pos"] >= Moviments.between5["end"]:
                    Moviments.between5["side"] = "left"


            if self.frameIndex > 3:
                self.frameIndex = 0

            self.rect.topleft = (Moviments.monsterX5, 292)


    return { 
        "Monster": Monster, 
        "Monster2": Monster2, 
        "Monster3": Monster3, 
        "Monster4": Monster4, 
        "Monster5": Monster5
        }
