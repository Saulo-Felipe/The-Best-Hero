import pygame
import os
from root import MAIN_DIR
from time import sleep
from .monsters import Monster
from .restart_pause import configGame
from .coins import Coins
import content.chooseMode as chooseMode
import json
from root import connection
from .trophy import Trophy
from pygame.locals import *


def oneLevel(screen):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    class configDead:
        pause = configGame(screen)
        isPaused = False
        isGameOver = False
        actionClickPause = False
        isDead = 0
        winCount = 0

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/levels/level01-background1.png")
        background_bridge = pygame.image.load(MAIN_DIR + "/images/levels/level01-background-bridge.png")
        playerSprite = pygame.image.load(MAIN_DIR + "/images/heroi/allpersons.png")
        pauseImg = pygame.image.load(MAIN_DIR + "/images/levels/pause.png")
        pause = pauseImg.get_rect(topleft=(screen.get_width()-pauseImg.get_width()-20, 20))
        coin = pygame.image.load(MAIN_DIR + "/images/levels/coin.png")

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

        isMoving = False

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
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.topleft = (Moviments.playerX, Moviments.playerY)

        def update(self, backgroundX):
            self.mask = pygame.mask.from_surface(self.image)
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
            {"start": 4223-10, "end": 4467-13},
            {"start": 7311-13, "end": 7552-30},
        ]

        allHolders = [
            {"start": 1244, "end": 1528, "down": 495, "up": 443, "floor": 348},
            {"start": 2485, "end": 2770, "down": 501, "up": 448, "floor": 353},
            {"start": 3639, "end": 3923, "down": 498, "up": 445, "floor": 350},
            {"start": 4760, "end": 5044, "down": 502, "up": 449, "floor": 354},
            {"start": 5053, "end": 5336, "down": 391, "up": 338, "floor": 244},
            {"start": 5563, "end": 5847, "down": 386, "up": 333, "floor": 239},
            {"start": 7827, "end": 8111, "down": 506, "up": 453, "floor": 359},
            {"start": 8274, "end": 8559, "down": 384, "up": 331, "floor": 237},
        ]

        allBoxes = [
            {"start": 3062, "end": 3240, "up": 546, "floor": 456},
            {"start": 6296, "end": 6454, "up": 542, "floor": 452},
            {"start": 8854, "end": 9011, "up": 545, "floor": 455},
        ]

    def collision():
        floor = (Moviments.backgroundX - 570)*(-1)
        Y = Moviments.playerY
        X = (Moviments.backgroundX * -1) + 552 + 52


        for hole in Obstacles.allHoles:
            if floor > hole["start"] and floor < hole["end"] and Moviments.playerY >= Moviments.floor:
                Moviments.playerY += 8
                configDead.isDead += 8

                if configDead.isDead >= 130:
                    configDead.pause.gameOver = True
                    configDead.isPaused = True

        for holder in Obstacles.allHolders:

            # Bater na plataforma
            if Y < holder["down"] and Y > holder["up"] and holder["start"] < X < holder["end"]:
                Moviments.Type = "fall"

            #Subir na plataforma
            if Y + 93 <= holder["up"] and holder["start"]-52 < X < holder["end"]+70 and Moviments.Type == "fall":
                Moviments.floor = holder["floor"]

            # Descer da plataforma
            if (X < holder["start"] or X > holder["end"]) and Moviments.floor == holder["floor"] and Moviments.Type != "jump":
                Moviments.floor = 552
                Moviments.Type = "fall"

        for box in Obstacles.allBoxes:
            
            # Subir na caixa
            if Y < box["up"] and box["start"] < X < box["end"] and Moviments.Type == "fall":
                Moviments.floor = box["floor"]

            # Descer da caixa
            if (X < box["start"] or X > box["end"]) and Moviments.floor == box["floor"] and Moviments.Type != "jump":
                Moviments.floor = 552
                Moviments.Type = "fall"

            # Colisão com a frente da caixa
            if X > box["start"] and X < box["end"]-125 and Y -99 < 552 and Y > box["up"]:
                Moviments.backgroundX = (box["start"] *-1) + 555 + 52
                Moviments.isMoving = False

            # Colisão com a traseira da caixa
            if X < box["end"] and X > box["start"]+125 and Y -99 < 552 and Y > box["up"]:
                Moviments.backgroundX = (box["end"] *-1) + 555 + 52
                Moviments.isMoving = False

    def moviments():
        if Moviments.Type == "jump":
            if Moviments.playerY > Moviments.floor -220 and Moviments.playerY <= 552:
                Moviments.playerY -= 8
            else:
                Moviments.Type = "fall"

        elif Moviments.Type == "fall":
            if Moviments.playerY < Moviments.floor:
                Moviments.playerY += 8
            else:
                Moviments.Type = "stopped"

        if Moviments.Type != "stopped" and Moviments.Side == "right" and Moviments.diagonally == True and Moviments.playerY <= 552:
            if Moviments.playerX < 570:
                Moviments.playerX += 6
            else:
                Moviments.backgroundX -= 6
                Moviments.isMoving = Moviments.Side

        elif Moviments.Type != "stopped" and Moviments.Side == "left" and Moviments.diagonally == True and Moviments.playerY <= 552:
            if Moviments.backgroundX == 0 and Moviments.playerX > 0:
                Moviments.playerX -= 6
            elif Moviments.backgroundX != 0:
                Moviments.backgroundX += 6
                Moviments.isMoving = Moviments.Side

    def move():

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

    coinsPositions = [
        {"X": 1300, "Y": 438-39},
        {"X": 1370, "Y": 438-39},
        {"X": 1440, "Y": 438-39},
        
        {"X": 2537, "Y": 438-39},
        {"X": 2607, "Y": 438-39},
        {"X": 2677, "Y": 438-39},

        {"X": 4000, "Y": 630-39},

        {"X": 3720, "Y": 438-39},
        {"X": 3790, "Y": 438-39},

        {"X": 5620, "Y": 330-39},
        {"X": 5690, "Y": 330-39},
        {"X": 5760, "Y": 330-39},

        {"X": 7900, "Y": 433-39},
        {"X": 7970, "Y": 433-39},

        {"X": 8330, "Y": 308-39},
        {"X": 8400, "Y": 308-39},
        {"X": 8470, "Y": 308-39},

        {"X": 8905, "Y": 540-39},

        # ----- Pilha de moedas -----
        {"X": 9670, "Y": 590-39},
        {"X": 9740, "Y": 590-39},
        {"X": 9810, "Y": 590-39},
        {"X": 9880, "Y": 590-39},

        {"X": 9703, "Y": 590-78},
        {"X": 9773, "Y": 590-78},
        {"X": 9843, "Y": 590-78},

        {"X": 9736, "Y": 590-117},
        {"X": 9806, "Y": 590-117},

        {"X": 9769, "Y": 590-156},
    ]
    monstersPositions = [
        {"start": 2105, "end": 3062, "floor": 592, "type": 0},
        {"start": 3220, "end": 4188, "floor": 592, "type": 1},
        {"start": 5052, "end": 5873, "floor": 230, "type": 2},
        {"start": 4470, "end": 6296, "floor": 592, "type": 0},
        {"start": 5300, "end": 6296, "floor": 592, "type": 1},
        {"start": 1130, "end": 1580, "floor": 366, "type": 2},
        {"start": 6464, "end": 7160, "floor": 592, "type": 0},
        {"start": 7571, "end": 8840, "floor": 500, "type": 3},
        {"start": 9100, "end": 9990, "floor": 555, "type": 2},
    ]

    player = Player()
    trophy = Trophy()

    allSpritesGroup = pygame.sprite.Group()
    monsterGroup = pygame.sprite.Group()
    coinsGroup = pygame.sprite.Group()
    trophyGroup = pygame.sprite.Group()

    allSpritesGroup.add(player)
    allSpritesGroup.add(trophy)
    trophyGroup.add(trophy)

    for c in coinsPositions:
        coin = Coins(c["X"], c["Y"])

        allSpritesGroup.add(coin)
        coinsGroup.add(coin)
    
    for m in monstersPositions:
        monster = Monster(m["start"], m["end"], m["floor"], m["type"])

        allSpritesGroup.add(monster)
        monsterGroup.add(monster)

    coinsAmount = 0
    txtCoins = pygame.font.Font(MAIN_DIR + "/fonts/Peace_Sans.otf", 30)

    def blitAll():
        if (Moviments.backgroundX * -1) + 552 + 52 > 7220 and (Moviments.backgroundX * -1) + 552 + 52 < 7552 and Moviments.playerY == 552:
            Images.background = Images.background_bridge
        
        screen.blit(Images.background, (Moviments.backgroundX, 0))
        screen.blit(Images.pauseImg, Images.pause)
        screen.blit(Images.coin, (20, 20))

        coinsTxtRender = txtCoins.render(str(coinsAmount), True, "black")
        screen.blit(coinsTxtRender, (Images.coin.get_width()+40, 20))


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if Images.pause.collidepoint(event.pos):
                    configDead.pause.Pause = True
                    configDead.isPaused = True
    
            configDead.actionClickPause = configDead.pause.verifyScreen(event)

        move()

        coinCollision = pygame.sprite.spritecollide(player, coinsGroup, True, pygame.sprite.collide_mask)
        monsterCollision = pygame.sprite.spritecollide(player, monsterGroup, False, pygame.sprite.collide_mask)
        winGameCollision = pygame.sprite.spritecollide(player, trophyGroup, False, pygame.sprite.collide_mask)

        if len(winGameCollision) > 0:
            configDead.isPaused = True
            configDead.pause.win = True

        if len(coinCollision) > 0:
            coinsAmount += 1
            
            pygame.mixer.music.load(MAIN_DIR + '/sons/coin.wav')
            pygame.mixer.music.play()

        # Game Over
        if len(monsterCollision) > 0 and configDead.isGameOver == False:
            configDead.pause.gameOver = True
            configDead.isPaused = True

        configDead.pause.drawPause(coinsAmount)

        if configDead.isPaused == False:
            blitAll()
            allSpritesGroup.draw(screen)
            moviments()
            collision()
            Moviments.diagonally = False
            allSpritesGroup.update(Moviments.isMoving)
            Moviments.isMoving = False

        else:
            if configDead.pause.win == True and configDead.winCount == 0:

                # ------- Inserir novos pontos na para o usuario --------

                Afile = open(MAIN_DIR + "/localStorage.json")
                Ajson = json.load(Afile)

                connection.execute(f"SELECT points from player WHERE id = {Ajson['id']}")
                result = connection.fetchall()

                newPoints = result[0][0] + coinsAmount

                connection.execute(f"UPDATE player SET points = {newPoints} WHERE id = {Ajson['id']}")

                configDead.isGameOver = True
                configDead.pause.gameOver = False

                configDead.winCount = 1

            if configDead.actionClickPause == "backToGame":
                configDead.pause.Pause = False
                configDead.isPaused = False
                configDead.pause.pauseCount = configDead.pause.winCount = configDead.pause.gameOverCount = 0
            elif configDead.actionClickPause == "restartGame":
                oneLevel(screen)
            elif configDead.actionClickPause == "leaveGame":
                return chooseMode.chooseMode(screen)

        pygame.display.flip()