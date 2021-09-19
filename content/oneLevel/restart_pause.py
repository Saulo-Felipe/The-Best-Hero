import pygame
from root import MAIN_DIR

def configGame(screen):

    class configsImages:
        listBtn = pygame.image.load(MAIN_DIR + "/images/levels/list.png")
        restartBtn = pygame.image.load(MAIN_DIR + "/images/levels/restart.png")
        configBtn = pygame.image.load(MAIN_DIR + "/images/levels/config.png")
        backToGame = pygame.image.load(MAIN_DIR + "/images/levels/backToGame.png")

    
    class rects:
        backToGameRect = configsImages.backToGame.get_rect(topleft=((screen.get_width()-configsImages.backToGame.get_width())/2, screen.get_height()/2+20))
        restartGameRect = configsImages.restartBtn.get_rect(topleft=((screen.get_width()-60)/2, (screen.get_height()-200)/2+15))

        
    class pause:
        Pause = False
        fontPause = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 35)
        pauseRender = fontPause.render("PAUSADO", True, (0, 0, 0))

        def drawPause(event):
            pygame.draw.rect(screen, "white", ((screen.get_width()-400)/2, (screen.get_height()-400)/2, 400, 350))
            screen.blit(pause.pauseRender, ((screen.get_width()-pause.pauseRender.get_width())/2, (screen.get_height()-400)/2+20))
            
            screen.blit(configsImages.listBtn, ((screen.get_width()-350)/2, (screen.get_height()-200)/2+15))
            screen.blit(configsImages.restartBtn, rects.restartGameRect)
            screen.blit(configsImages.configBtn, ((screen.get_width()+220)/2, (screen.get_height()-200)/2+15))

            screen.blit(configsImages.backToGame, rects.backToGameRect)

            return verifyScreen(event)

    def verifyScreen(event):
        if event.type == pygame.MOUSEBUTTONUP:
            if rects.backToGameRect.collidepoint(event.pos):
                return "backToGame"
            
            if rects.restartGameRect.collidepoint(event.pos):
                return "restartGame"



    return pause