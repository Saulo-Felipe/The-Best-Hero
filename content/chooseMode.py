import pygame

from .oneLevel import oneLevel
from .twoLevel import twoLevel
from .threeLevel import threeLevel
from .ranking import rankingScreen
from .mainScreen import mainScreen


from root import MAIN_DIR


def chooseMode(screen):


    class GameOptions:
        def __init__(self):
            self.images = []
            self.rects = []
            self.masks = []

            for i in range(4):
                self.images.append(pygame.image.load(MAIN_DIR + '/images/chooseGame/option'+str(i)+'.png'))
                self.masks.append(pygame.mask.from_surface(self.images[i]))
            
            for r in range(4):
                positionRect = 0
                if r == 0:
                    positionRect = 250, 300
                elif r == 1:
                    positionRect = 600, 300
                elif r == 2:
                    positionRect = 950, 300
                elif r == 3:
                    positionRect = 300, 530
                else:
                    print('Erro interno na linha 25')

                self.rects.append(self.images[r].get_rect(center=positionRect))


    # ======| Variables |====== #
    font = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 30)
    title = font.render("Escolha um modo de Jogo", True, (255, 255, 255))

    backScreenImg = pygame.image.load(MAIN_DIR + '/images/backScreen.png')
    backScreen = backScreenImg.get_rect(topleft=(screen.get_width()-backScreenImg.get_width()-20, 20))
    
    gameOptions = GameOptions()
    background = pygame.image.load(MAIN_DIR + '/images/chooseGame/background.png')
    clock = pygame.time.Clock()


    choosing = True
    while choosing:
        clock.tick(120)

        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                for e in range(4):
                    pos = pygame.mouse.get_pos()
                    clickPosition = pos[0] - gameOptions.rects[e].x, pos[1] - gameOptions.rects[e].y

                    if gameOptions.rects[e].collidepoint(pos) and gameOptions.masks[e].get_at(clickPosition):
                        
                        choosing = False

                        if e == 0:
                            return twoLevel.twoLevel(screen)                        
                        elif e == 1:
                            return oneLevel.oneLevel(screen)
                        elif e == 2:
                            return threeLevel.threeLevel(screen)
                        elif e == 3:
                            return rankingScreen(screen)


                if backScreen.collidepoint(event.pos):
                    return mainScreen.mainScreen(screen)
                    break
                    

        mouseEnter = False
        for c in range(4):
            pos = pygame.mouse.get_pos()
            clickPosition = pos[0] - gameOptions.rects[c].x, pos[1] - gameOptions.rects[c].y

            if gameOptions.rects[c].collidepoint(pos) and gameOptions.masks[c].get_at(clickPosition):
                if c != 3:
                    gameOptions.images[c] = pygame.transform.scale(pygame.image.load(MAIN_DIR + '/images/chooseGame/option'+str(c)+'.png'), (int(309*1.08), int(227*1.08)))
                mouseEnter = True
                
            else:
                gameOptions.images[c] = pygame.image.load(MAIN_DIR + '/images/chooseGame/option'+str(c)+'.png').convert_alpha()

        if mouseEnter:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            mouseEnter = False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        for c in range(4):
            screen.blit(gameOptions.images[c], gameOptions.rects[c])
        
        
        screen.blit(title, (20, 40))
        screen.blit(backScreenImg, backScreen)
        pygame.display.flip()

    return