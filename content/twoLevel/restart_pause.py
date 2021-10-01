import pygame
from root import MAIN_DIR


def configGame(screen):
    
    backgroundBlack = pygame.image.load(MAIN_DIR + "/images/backgroundBlack.png").convert_alpha()

    class configsImages:
        listBtn = pygame.image.load(MAIN_DIR + "/images/levels/list.png")
        restartBtn = pygame.image.load(MAIN_DIR + "/images/levels/restart.png")
        configBtn = pygame.image.load(MAIN_DIR + "/images/levels/config.png")
        backToGame = pygame.image.load(MAIN_DIR + "/images/levels/backToGame.png")

        victory = pygame.image.load(MAIN_DIR + "/images/levels/victory.png")
        backgroundBlack = pygame.image.load(MAIN_DIR + "/images/backgroundBlack.png")


    class rects:
        backToGameRect = configsImages.backToGame.get_rect(topleft=((screen.get_width()-configsImages.backToGame.get_width())/2, screen.get_height()/2+20))
        restartGameRect = configsImages.restartBtn.get_rect(topleft=((screen.get_width()-60)/2, (screen.get_height()-200)/2))
        listGameRect = configsImages.listBtn.get_rect(topleft=((screen.get_width()-350)/2, (screen.get_height()-200)/2))
        configGameRect = configsImages.configBtn.get_rect(topleft=(((screen.get_width()+220)/2, (screen.get_height()-200)/2)))

    class pause:
        Pause = False
        gameOver = False
        win = False
        fontPause = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 35)
        
        pauseCount = 0  
        winCount = 0
        gameOverCount = 0

        def drawPause(coins):
            if pause.Pause == True:
                if pause.pauseCount == 0:
                    screen.blit(backgroundBlack, (0, 0))
                    pause.pauseCount = 1

                TxtPaused = pause.fontPause.render("PAUSADO", True, (0, 0, 0))
                pygame.draw.rect(screen, "white", ((screen.get_width()-400)/2, (screen.get_height()-400)/2, 400, 350))
                screen.blit(TxtPaused, ((screen.get_width()-TxtPaused.get_width())/2, (screen.get_height()-400)/2+20))
                screen.blit(configsImages.backToGame, rects.backToGameRect)

            elif pause.gameOver == True:
                if pause.gameOverCount == 0:
                    screen.blit(backgroundBlack, (0, 0))
                    pause.gameOverCount = 1

                TxtPaused = pause.fontPause.render("GAME OVER", True, (0, 0, 0))
                pygame.draw.rect(screen, "white", ((screen.get_width()-400)/2, (screen.get_height()-400)/2, 400, 300))
                screen.blit(TxtPaused, ((screen.get_width()-TxtPaused.get_width())/2, (screen.get_height()-400)/2+20))
            
            elif pause.win == True:
                if pause.winCount == 0:
                    screen.blit(backgroundBlack, (0, 0))
                    pause.winCount = 1
            
                coinFont = pygame.font.Font(MAIN_DIR + "/fonts/Peace_Sans.otf", 65)
                coinRender = coinFont.render(str(coins), True, "gold")

                screen.blit(configsImages.victory.convert_alpha(), ((screen.get_width()-configsImages.victory.get_width())/2, (screen.get_height()-configsImages.victory.get_height()+100)/2, 400, 350))
                screen.blit(coinRender, (screen.get_width()/2-20, 250))
                

            if pause.gameOver == True or pause.Pause == True:
                screen.blit(configsImages.listBtn, rects.listGameRect)
                screen.blit(configsImages.restartBtn, rects.restartGameRect)
                screen.blit(configsImages.configBtn, rects.configGameRect)
            
            if pause.win == True:
                screen.blit(configsImages.listBtn, (screen.get_width()/2-130, screen.get_height()/2+220))
                screen.blit(configsImages.restartBtn, ((screen.get_width()-configsImages.restartBtn.get_width())/2, screen.get_height()/2+220))
                screen.blit(configsImages.configBtn, (screen.get_width()/2+65, screen.get_height()/2+220))

                rects.listGameRect.topleft = (screen.get_width()/2-130, screen.get_height()/2+220)
                rects.restartGameRect.topleft = ((screen.get_width()-configsImages.restartBtn.get_width())/2, screen.get_height()/2+220)
                rects.configGameRect.topleft = (screen.get_width()/2+65, screen.get_height()/2+220)
            

        def verifyScreen(event):
            if event.type == pygame.MOUSEBUTTONUP:
                if rects.backToGameRect.collidepoint(event.pos):
                    return "backToGame"
                
                if rects.restartGameRect.collidepoint(event.pos):
                    return "restartGame"

                if rects.listGameRect.collidepoint(event.pos):
                    return "leaveGame"




    return pause