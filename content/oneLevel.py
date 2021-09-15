import pygame
import os
from root import MAIN_DIR
from time import sleep

def oneLevel(screen):

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/levels/level01-background.png")
        playerSprite = pygame.image.load(MAIN_DIR + "/images/heroi/allpersons.png")
        pauseImg = pygame.image.load(MAIN_DIR + "/images/levels/pause.png")
        pause = pauseImg.get_rect(topleft=(screen.get_width()-pauseImg.get_width()-20, 20))

    class Moviments:
        backgroundX = 0
        backgroundY = 0

        playerX = 100
        playerY = 552
        floor = 552
        isUp = False

        Type = "stopped"
        Side = "right"
        diagonally = False

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.spriteFrames = []
            for c in range(5):
                cutImage = Images.playerSprite.subsurface((c*52, 0), (52, 93))
                self.spriteFrames.append(cutImage.convert_alpha())
            
            for c in range(5):
                cutImage = Images.playerSprite.subsurface((c*52, 100), (52, 99))
                self.spriteFrames.append(cutImage.convert_alpha())

            self.frameIndex = 0
            self.image = self.spriteFrames[int(self.frameIndex)]
            self.rect = self.image.get_rect()
            self.rect.topleft = (Moviments.playerX, Moviments.playerY)

        def update(self):
            if Moviments.Type == "jump":
                self.frameIndex += 0.05
            else:
                self.frameIndex += 0.11

            self.rect.topleft = (Moviments.playerX, Moviments.playerY)

            if self.frameIndex > 4.8:
                self.frameIndex = 1


            # Verify Moviment type
            if Moviments.Type == "walk" and Moviments.Side == "left":
                self.image = pygame.transform.flip(self.spriteFrames[int(self.frameIndex)], True, False)
                Moviments.Type = "stopped"


            elif Moviments.Type == "walk" and Moviments.Side == "right":
                self.image = self.spriteFrames[int(self.frameIndex)]
                Moviments.Type = "stopped"

            elif Moviments.Type == "jump" and Moviments.Side == "left":
                self.image = pygame.transform.flip(self.spriteFrames[int(self.frameIndex) + 5], True, False)
            elif Moviments.Type == "jump" and Moviments.Side == "right":
                self.image = self.spriteFrames[int(self.frameIndex) + 5]
            
            elif Moviments.Type == "fall" and Moviments.Side == "left":
                self.image = pygame.transform.flip(self.spriteFrames[6], True, False)
            elif Moviments.Type == "fall" and Moviments.Side == "right":
                self.image = self.spriteFrames[6]

            else:
                self.image = self.spriteFrames[0] if Moviments.Side == "right" else pygame.transform.flip(self.spriteFrames[0], True, False)


    class Obstacles():
        allHoles = [
            {"start": 1885-15, "end": 2104-15},
            {"start": 4187-10, "end": 4467-13},
            {"start": 7188-13, "end": 7552-30},
        ]

        allHolders = [
            {"start": 1244, "end": 1528, "down": 495, "up": 443, "floor": 348},
            {"start": 2485, "end": 2770, "down": 501, "up": 448, "floor": 353},
            {"start": 3639, "end": 3923, "down": 498, "up": 445, "floor": 350},
            {"start": 4760, "end": 5044, "down": 502, "up": 449, "floor": 354},
            {"start": 5563, "end": 5847, "down": 386, "up": 333, "floor": 238},

        ]


    def collision():
        floor = (Moviments.backgroundX - 570)*(-1)
        
        for hole in Obstacles.allHoles:
            if floor > hole["start"] and floor < hole["end"] and Moviments.playerY >= Moviments.floor:
                Moviments.playerY += 8

        for holder in Obstacles.allHolders:
            Y = Moviments.playerY
            X = (Moviments.backgroundX * -1) + 552 + 52

            if Y < holder["down"] and Y > holder["up"] and holder["start"] < X < holder["end"]:
                Moviments.Type = "fall"
            
            if Y <= holder["up"] and holder["start"] < X < holder["end"] and Moviments.Type == "fall":
                Moviments.floor = holder["floor"]
            
            if (X < holder["start"] or X > holder["end"]) and Moviments.floor == holder["floor"]:
                # Reserva: and (Y >= Moviments.floor)
                print("Saiu")
                Moviments.floor = 552
                Moviments.Type = "fall"
            


    def moviments():

        if Moviments.Type == "jump":
            if Moviments.playerY > Moviments.floor -220:
                Moviments.playerY -= 8
            else:
                Moviments.Type = "fall"

        elif Moviments.Type == "fall":
            if Moviments.playerY < Moviments.floor:
                Moviments.playerY += 8
            else:
                Moviments.Type = "stopped"

        if Moviments.Type != "stopped" and Moviments.Side == "right" and Moviments.diagonally == True:
            if Moviments.playerX < 570:
                Moviments.playerX += 5
            else:
                Moviments.backgroundX -= 5

        elif Moviments.Type != "stopped" and Moviments.Side == "left" and Moviments.diagonally == True:
            if Moviments.backgroundX == 0 and Moviments.playerX > 0:
                Moviments.playerX -= 5
            elif Moviments.backgroundX != 0:
                Moviments.backgroundX += 5


    playerGroup = pygame.sprite.Group()
    player = Player()
    playerGroup.add(player)

    def blitAll():
        screen.blit(Images.background, (Moviments.backgroundX, 0))
        screen.blit(Images.pauseImg, Images.pause)

    class pause:
        Pause = False

        def drawPause():
            pygame.draw.rect(screen, "white", (300, 200, 200, 400))


    clock = pygame.time.Clock()
    while True:
        if pause.Pause == False:
            clock.tick(60)
            screen.fill("black")

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    exit()
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if Images.pause.collidepoint(event.pos):
                        pause.Pause = True
            
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                Moviments.Side = "right"
                Moviments.diagonally = True
                if Moviments.Type != "jump" and Moviments.Type != "fall":
                    Moviments.Type = "walk"

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                Moviments.Side = "left"
                Moviments.diagonally = True
                if Moviments.Type != "jump" and Moviments.Type != "fall":
                    Moviments.Type = "walk"            

            if pygame.key.get_pressed()[pygame.K_UP]:
                if "fall" != Moviments.Type != "jump":
                    Moviments.Type = "jump"

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if Moviments.Type == "jump":
                    Moviments.Type = "fall"



            blitAll()


            playerGroup.draw(screen)

            moviments()

            Moviments.diagonally = False

            collision()
        else:

            pause.drawPause()

        playerGroup.update()
        
        pygame.display.flip()
