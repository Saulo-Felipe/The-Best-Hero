import pygame
import json
from root import MAIN_DIR
from root import connection
from . import loginScreen



def mainScreen(screen):
    class IsAuthenticated:
        Afile = open(MAIN_DIR + "/localStorage.json")
        UserState = json.load(Afile)
        Afile.close()

    # ================================================= #

    class Images:
        background = pygame.image.load(MAIN_DIR + "/images/mainScreen/background.png")

        enter = pygame.image.load(MAIN_DIR + "/images/mainScreen/enter.png")
        logout = pygame.image.load(MAIN_DIR + "/images/mainScreen/exit.png")

    class Rects:
        enter = Images.enter.get_rect(topleft=(1140-Images.enter.get_width()-50, 724-Images.enter.get_height()-50))
        logout = Images.logout.get_rect(topleft=(1140-Images.enter.get_width()-50, 724-Images.enter.get_height()-50))

    class inputValues:
        state = False
        emailContent = "Teste de texto aqui"
        passwordContent = "Teste de texto aqui"

        selectedSubScreen = False

    def Clicks():
        if event.type == pygame.MOUSEBUTTONUP:
            userStatus = IsAuthenticated.UserState["isAuthenticated"]

            if userStatus == False and Rects.enter.collidepoint(event.pos):
                print('Detectei colisão')
                inputValues.selectedSubScreen = "login"

            elif userStatus == True and Rects.logout.collidepoint(event.pos):
                inputValues.selectedSubScreen = "register"


    def BlitAll():
        screen.blit(Images.background, (-1293, -3))


        # Apenas elementos autenticados
        def isAuthenticated():
            if IsAuthenticated.UserState["isAuthenticated"] == True:
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
                            break


        if inputValues.selectedSubScreen == "login":
            inputValues.selectedSubScreen = loginScreen.drawLogin(screen, event, inputValues.state)
        elif inputValues.selectedSubScreen == "register":
            print('Esta na tela de registro')
        
        inputValues.state = False

        Clicks()


        pygame.display.flip()


    return