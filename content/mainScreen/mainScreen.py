import pygame
import json
from root import MAIN_DIR
from root import connection
from . import loginScreen
from . import registerScreen
from ..chooseMode import chooseMode


clock = pygame.time.Clock()

def mainScreen(screen):

    clock.tick(60)
    class IsAuthenticated:
        def verify():
            Afile = open(MAIN_DIR + "/localStorage.json", "r")
            UserState = json.load(Afile)
            Afile.close()
            
            return UserState

    # ================================================= #

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/mainScreen/background.png")

        enter = pygame.image.load(MAIN_DIR + "/images/mainScreen/enter.png")
        logout = pygame.image.load(MAIN_DIR + "/images/mainScreen/exit.png")

        play = pygame.image.load(MAIN_DIR + "/images/mainScreen/play.png")

    class Rects:
        enter = Images.enter.get_rect(topleft=(1140-Images.enter.get_width()-50, 724-Images.enter.get_height()-50))
        logout = Images.logout.get_rect(topleft=(1140-Images.enter.get_width()-50, 724-Images.enter.get_height()-50))

        play = Images.play.get_rect(topleft=(440, 419))

    class inputValues:
        state = False

        selectedSubScreen = False

    TxtWelCome = pygame.font.SysFont("Arial", 20, bold=True)

    def BlitAll():
        screen.blit(Images.background, (-1293, -3))
        screen.blit(Images.play, Rects.play)

        # Apenas elementos autenticados
        def isAuthenticated():
            if IsAuthenticated.verify()["isAuthenticated"] == True:
                renderWelCome = TxtWelCome.render(f"Seja Bem Vindo, {IsAuthenticated.verify()['username']}", True, "black")
                
                screen.blit(renderWelCome, (60, 60))
                screen.blit(Images.logout, Rects.logout)
            else:
                screen.blit(Images.enter, Rects.enter)
        isAuthenticated()
    
    aceptedLetters = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n", 
    "o", "p", "q", "r", "s", "t", "u",
    "v", "x", "w", "y", "z", "1", "2", 
    "3", "4", "5", "6", "7", "8", "9", 
    "_", ".", "@"
    ]


    while True:
        BlitAll()
        nextScreen = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    inputValues.state = "delete"
                else:
                    for letter in range(len(aceptedLetters)):
                        if event.unicode == aceptedLetters[letter]:
                            inputValues.state = aceptedLetters[letter]
            
            if event.type == pygame.MOUSEBUTTONUP:
                userStatus = IsAuthenticated.verify()["isAuthenticated"]

                if userStatus == False and Rects.enter.collidepoint(event.pos):
                    inputValues.selectedSubScreen = "login"

                elif userStatus == True and Rects.logout.collidepoint(event.pos):
                    Afile = open(MAIN_DIR + "/localStorage.json", "w")
                    jsonUpdate = { "isAuthenticated": False }
                    json.dump(jsonUpdate, Afile)
                    Afile.close()
                
                if Rects.play.collidepoint(event.pos) and inputValues.selectedSubScreen == False:
                    if userStatus == True:
                        nextScreen = True
                    else:
                        inputValues.selectedSubScreen = "login"
                        nextScreen = False
            


        if inputValues.selectedSubScreen == "login":
            inputValues.selectedSubScreen = loginScreen.drawLogin(screen, event, inputValues.state)
        elif inputValues.selectedSubScreen == "register":
            inputValues.selectedSubScreen = registerScreen.drawRegister(screen, event, inputValues.state)
        
        
        inputValues.state = False


        if nextScreen == True:
            break


        pygame.display.flip()


    return chooseMode(screen)