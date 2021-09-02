import pygame

from oneleve import oneLevel
from twoLevel import twoLevel

def chooseMode(screen):

    class GameOptions:
        def __init__(self):
            self.images = []
            self.rects = []
            self.masks = []

            for i in range(3):
                self.images.append(pygame.image.load('./images/chooseGame/option'+str(i)+'.png'))
                self.masks.append(pygame.mask.from_surface(self.images[0]))
            
            for r in range(3):
                positionRect = 0
                if r == 0:
                    positionRect = 250, 300
                elif r == 1:
                    positionRect = 600, 300
                elif r == 2:
                    positionRect = 950, 300
                else:
                    print('Erro interno na linha 25')

                self.rects.append(self.images[r].get_rect(center=positionRect))
    
    #title = pygame.image.load('./images/chooseGame/title.png')

    font = pygame.font.Font('./Peace Sans.otf', 30)
    title = font.render("Escolha um modo de Jogo!", True, (255, 255, 255))

    ranking = pygame.image.load('./images/chooseGame/ranking.png')
    ranking_rect = ranking.get_rect(center=(300, 530))


    gameOptions = GameOptions()
    
    background = pygame.image.load('./images/chooseGame/background.png')

    clock = pygame.time.Clock()

    choosing = True
    while choosing:
        clock.tick(120)

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        mouseEnter = False
        for c in range(3):
            pos = pygame.mouse.get_pos()
            clickPosition = pos[0] - gameOptions.rects[c].x, pos[1] - gameOptions.rects[c].y

            if gameOptions.rects[c].collidepoint(pos) and gameOptions.masks[c].get_at(clickPosition):
                gameOptions.images[c] = pygame.transform.scale(pygame.image.load('./images/chooseGame/option'+str(c)+'.png'), (int(309*1.08), int(227*1.08)))
                mouseEnter = True
                
            else:
                gameOptions.images[c] = pygame.image.load('./images/chooseGame/option'+str(c)+'.png').convert_alpha()

        if mouseEnter:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            mouseEnter = False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for e in range(3):
                pos = pygame.mouse.get_pos()
                clickPosition = pos[0] - gameOptions.rects[e].x, pos[1] - gameOptions.rects[c].y

                if gameOptions.rects[e].collidepoint(pos) and gameOptions.masks[e].get_at(clickPosition):
                    choosing = False
                    if e == 0:
                        oneLevel(screen)
                    elif e == 1:
                        twoLevel(screen)

        print('Ainda estou no loop principal')
        for c in range(3):
            screen.blit(gameOptions.images[c], gameOptions.rects[c])
        
        screen.blit(title, (20, 40))
        screen.blit(ranking, ranking_rect)

        pygame.display.flip()

    return