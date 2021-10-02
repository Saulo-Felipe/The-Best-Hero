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


def twoLevel(screen):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    class configDead:
        pause = configGame(screen)
        isPaused = False
        isGameOver = False
        actionClickPause = False
        isDead = 0
        winCount = 0

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/levels/level02-background.png")
        playerSprite = pygame.image.load(MAIN_DIR + "/images/heroi/allpersons.png")
        pauseImg = pygame.image.load(MAIN_DIR + "/images/levels/pause.png")
        pause = pauseImg.get_rect(topleft=(screen.get_width()-pauseImg.get_width()-20, 20))
        coin = pygame.image.load(MAIN_DIR + "/images/levels/coin.png")

    class Moviments:
        backgroundX = 0
        backgroundY = 0

        playerX = 100
        playerY = 540
        floor = 540
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
            {"start": 1135, "end": 1328},
            {"start": 2007, "end": 2188},
            {"start": 3070, "end": 3353},
            {"start": 4236, "end": 4474},
            {"start": 5357, "end": 5548},
            {"start": 5705, "end": 5875},
            {"start": 6035, "end": 6185},
            {"start": 6346, "end": 6488},
            {"start": 6649, "end": 6823},
        ]

        allHolders = [
            {"start": 708-32, "end": 980, "down": 498, "up": 440, "floor": 444-97},
            {"start": 2441-32, "end": 2712, "down": 505, "up": 447, "floor": 447-97},
            {"start": 3855-32, "end": 4126, "down": 501, "up": 442, "floor": 439-97},
            {"start": 4456-32, "end": 4729, "down": 432, "up": 374, "floor": 373-97},
            {"start": 4215-32, "end": 4455, "down": 338, "up": 280, "floor": 281-97},
            {"start": 5150-32, "end": 5421, "down": 493, "up": 436, "floor": 433-97},
            {"start": 7238-32, "end": 7509, "down": 483, "up": 424, "floor": 421-97},
            {"start": 7575-32, "end": 7846, "down": 341, "up": 283, "floor": 282-97},
            {"start": 8500-32, "end": 8771, "down": 443, "up": 385, "floor": 383-97},
        ]

        allBoxes = [
            {"start": 3620, "end": 3683, "up": 555, "floor": 555-95},

            {"start": 1842, "end": 1897, "up": 561, "floor": 561-95},
            {"start": 1898, "end": 2008, "up": 522, "floor": 522-95},
            {"start": 1937, "end": 2007, "up": 469, "floor": 469-95},

            {"start": 8103, "end": 8159, "up": 562, "floor": 562-95},
            {"start": 8159, "end": 8269, "up": 521, "floor": 562-95},
            {"start": 8200, "end": 8269, "up": 468, "floor": 468-95},

            {"start": 8978, "end": 9041, "up": 557, "floor": 557-95},

            {"start": 9353, "end": 9416, "up": 557, "floor": 557-95},

            {"start": 9707, "end": 9770, "up": 558, "floor": 558-95},
        ]

        coinsPositions = [
            {"X": 750, "Y": 415-39},
            {"X": 820, "Y": 415-39},
            {"X": 890, "Y": 415-39},

            {"X": 2525, "Y": 612-39},
            {"X": 2595, "Y": 612-39},
        ]

        monstersPositions = [
            {"start": 2400, "end": 3070-105, "floor": 625-105, "type": 0},
            {"start": 660, "end": 1150, "floor": 415-57, "type": 1},
            {"start": 1350, "end": 0, "floor": 630-140, "type": 2},
            {"start": 2338, "end": 0, "floor": 630-140, "type": 3},
            {"start": 2195, "end": 3060, "floor": 400-50, "type": 5},
            {"start": 3684-72, "end": 4235-72, "floor": 632-120, "type": 4},
        ]

    def ObstaclesCollision():
        floor = (Moviments.backgroundX - 600)*(-1)
        Y = Moviments.playerY
        X = (Moviments.backgroundX * -1) + 540 + 52

        for hole in Obstacles.allHoles:
            if floor > hole["start"] and floor < hole["end"] and Moviments.playerY >= 540:
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
                Moviments.floor = 540
                Moviments.Type = "fall"

        for box in Obstacles.allBoxes:
            boxWidth = box["end"] - box["start"]

            # Subir na caixa
            if Y < box["up"] and (X+20 > box["start"] and X-20 < box["end"]) and Moviments.Type == "fall":
                Moviments.floor = box["floor"]

            # Descer da caixa
            if (X+20 < box["start"] or X-20 > box["end"]) and Moviments.floor == box["floor"] and Moviments.Type != "jump":
                Moviments.floor = 540
                Moviments.Type = "fall"

            # Colisão com a frente da caixa
            if X+20 >= box["start"] and X < box["end"]-boxWidth and Y+player.image.get_height()-10 > box["up"]:
                Moviments.backgroundX = box["start"]*-1 +610
                Moviments.isMoving = False

            # Colisão com a traseira da caixa
            if X >= box["start"]+boxWidth-10 and X <= box["end"] and Y+player.image.get_height()-10 > box["up"]:
                Moviments.backgroundX = box["end"] * -1 + 590
                Moviments.isMoving = False

    def moviments():
        if Moviments.Type == "jump":
            if Moviments.playerY > Moviments.floor -220 and Moviments.playerY <= 540:
                Moviments.playerY -= 8
            else:
                Moviments.Type = "fall"

        elif Moviments.Type == "fall":
            if Moviments.playerY < Moviments.floor:
                Moviments.playerY += 8
            else:
                Moviments.Type = "stopped"

        if Moviments.Type != "stopped" and Moviments.Side == "right" and Moviments.diagonally == True and Moviments.playerY <= 540:
            if Moviments.playerX < 570:
                Moviments.playerX += 6
            else:
                Moviments.backgroundX -= 6
                Moviments.isMoving = Moviments.Side

        elif Moviments.Type != "stopped" and Moviments.Side == "left" and Moviments.diagonally == True and Moviments.playerY <= 540:
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

    def updatePoints():
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
        
    player = Player()
    trophy = Trophy()

    allSpritesGroup = pygame.sprite.Group()
    monsterGroup = pygame.sprite.Group()
    coinsGroup = pygame.sprite.Group()
    trophyGroup = pygame.sprite.Group()

    allSpritesGroup.add(player)
    allSpritesGroup.add(trophy)
    trophyGroup.add(trophy)

    for c in Obstacles.coinsPositions:
        coin = Coins(c["X"], c["Y"])

        allSpritesGroup.add(coin)
        coinsGroup.add(coin)
    
    for m in Obstacles.monstersPositions:
        monster = Monster(m["start"], m["end"], m["floor"], m["type"])

        allSpritesGroup.add(monster)
        monsterGroup.add(monster)


    coinsAmount = 0
    txtCoins = pygame.font.Font(MAIN_DIR + "/fonts/Peace_Sans.otf", 30)

    def blitAll():
        screen.blit(Images.background, (Moviments.backgroundX, 0))
        screen.blit(Images.pauseImg, Images.pause)
        screen.blit(Images.coin, (20, 20))

        coinsTxtRender = txtCoins.render(str(coinsAmount), True, "black")
        screen.blit(coinsTxtRender, (Images.coin.get_width()+40, 20))


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                print("Player Y: ", Moviments.playerY)
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
            ObstaclesCollision()
            Moviments.diagonally = False
            allSpritesGroup.update(Moviments.isMoving)
            Moviments.isMoving = False

        else:
            if configDead.pause.win == True and configDead.winCount == 0:
                updatePoints()

            if configDead.actionClickPause == "backToGame":
                configDead.pause.Pause = False
                configDead.isPaused = False
                configDead.pause.pauseCount = configDead.pause.winCount = configDead.pause.gameOverCount = 0
            elif configDead.actionClickPause == "restartGame":
                twoLevel(screen)
            elif configDead.actionClickPause == "leaveGame":
                return chooseMode.chooseMode(screen)


        pygame.display.flip()