import pygame 
import os
from root import connection
from root import MAIN_DIR
from content import chooseMode


def rankingScreen(screen):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    connection.execute('SELECT * FROM player')

    records = connection.fetchall()

    def organizeList(e):
        return e[4]

    ranking = records

    ranking.sort(reverse=True, key=organizeList)

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/ranking/background.png")
        crown = pygame.image.load(MAIN_DIR + "/images/ranking/trophy.png")
        user = pygame.image.load(MAIN_DIR + "/images/ranking/user.png")
        backScreen = pygame.image.load(MAIN_DIR + "/images/backScreen.png")

        goldMedal = pygame.image.load(MAIN_DIR + "/images/ranking/gold-medal.png")
        silverMedal = pygame.image.load(MAIN_DIR + "/images/ranking/silver-medal.png")
        bronzeMedal = pygame.image.load(MAIN_DIR + "/images/ranking/bronze-medal.png")


    fontTitle = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 35)
    title = fontTitle.render("Veja sua posição no ranking", True, (255, 255, 255))

    fontConfig = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 25)
    backScreen = Images.backScreen.get_rect(topleft=(20, 20))

    class positions:
        rectsPositions = 100
        scrollY = 0

    def drawnRanking(player, count):
        id = player[0]
        username = player[1]
        email = player[2]
        punctuation = player[4]

        positions.rectsPositions += 90

        pygame.draw.rect(screen, "white", ((1140 - 900)/2,  positions.rectsPositions+positions.scrollY, 900, 75))

        # Imagem do usuário
        screen.blit(Images.user, ((1140 - 900)/2+75, positions.rectsPositions + 5 + positions.scrollY))

        # Nome do usuário
        playerName = fontConfig.render(username, True, (0, 0, 0))
        screen.blit(playerName, ((1140 - 900)/2+Images.user.get_width()+85, positions.rectsPositions+20 + positions.scrollY))

        # Pontuação
        playerPunctuation = fontConfig.render(str(punctuation) + " pontos", True, (0, 0, 0))
        screen.blit(playerPunctuation, ((1140 - 900)/2+900-playerPunctuation.get_width()-20, positions.rectsPositions+20 + positions.scrollY ))            

        # Rankin Positions
        pygame.draw.rect(screen, "gray", ((1140 - 900)/2+5,  positions.rectsPositions+5 + positions.scrollY, 65, 65))
        playerPosition = fontTitle.render(str(count), True, "black")
        screen.blit(playerPosition, ((1140 - 900)/2+25,  positions.rectsPositions+15 + positions.scrollY, 65, 65))

        if count == 1:
            screen.blit(Images.goldMedal, ((1140 - 900)/2-30,  positions.rectsPositions-20+positions.scrollY, 65, 65))
        elif count == 2:
            screen.blit(Images.silverMedal, ((1140 - 900)/2-30,  positions.rectsPositions-20+positions.scrollY, 65, 65))
        elif count == 3:
            screen.blit(Images.bronzeMedal, ((1140 - 900)/2-30,  positions.rectsPositions-20+positions.scrollY, 65, 65))


    while True:
        screen.blit(Images.background, (0, 0))
        screen.blit(title, ((screen.get_width()-title.get_width())/2, 50 + positions.scrollY))
        screen.blit(Images.crown, ((screen.get_width()+title.get_width())/2+20, 40 + positions.scrollY))
        screen.blit(Images.backScreen, (20, 20+positions.scrollY))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if backScreen.collidepoint(event.pos):
                    return chooseMode.chooseMode(screen)
                    break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    positions.scrollY -= 10
                if event.button == 4 and positions.scrollY != 0:
                    positions.scrollY += 10
                
        
        screen.scroll()

        positions.rectsPositions = 100
        count = 1
        for player in ranking:
            drawnRanking(player, count)
            count+=1



        pygame.display.flip()
    


    return
