import pygame
import json
from time import sleep
from root import MAIN_DIR


def mainScreen(screen):

    class Button:
        btn = pygame.image.load(MAIN_DIR + '/images/button_play.png')        
        ButtonPlay = pygame.transform.scale(btn, (int(btn.get_width()/2), int(btn.get_height()/2)))
        ButtonX = (1140 - ButtonPlay.get_width())/2
        ButtonY = (724 - ButtonPlay.get_height())/2

    class interfaceAuth():
        def __init__(self):
            self.openedWindow = False

            self.name = str("Teste Inicial")
            self.username = str("Teste Inicial")
            self.password = str("Teste Inicial")

            self.selectedInput = False

            self.resetColors()

        def resetColors(self):
            class Colors:
                nameColor = "gray"
                userNameColor = "gray"
                passwordColor = "gray"

            self.colors = Colors

        def login(self):
            if self.openedWindow == "login":
                screen.blit(blackBackground, (0, 0))
                pygame.draw.rect(screen, 'white', ((screen.get_width()-350)/2, (screen.get_height()-400)/2, 350, 400))

                self.inputUsernameLogin = pygame.draw.rect(screen, self.colors.userNameColor, ((screen.get_width()-320)/2, (screen.get_height()-150)/2, 320, 60))
                self.inputPasswordLogin = pygame.draw.rect(screen, self.colors.passwordColor, ((screen.get_width()-320)/2, (screen.get_height()-0)/2, 320, 60))
                self.inputSubmitLogin = pygame.draw.rect(screen, (0, 100, 0), ((screen.get_width()-320)/2, (screen.get_height()+150)/2, 100, 40))
                self.closeLoginContainer = closeIcon.get_rect( center=((screen.get_width()+350)/2, (screen.get_height()-400)/2) )
                self.goToRegister = pygame.draw.rect(screen, 'white', ((screen.get_width()+350)/2 - goToRegister.get_width() - 15, (screen.get_height()+400)/2 - 25 - 15, goToRegister.get_width(), 25))

                renderLoginUsername = inputUsernameTxt.render(self.username, True, (0, 0, 0))
                renderLoginPassword = inputPasswordTxt.render(self.password, True, (0, 0, 0))

                screen.blit(titleLogin, ((screen.get_width()-titleRegister.get_width())/2, 175))
                screen.blit(usernameLogin, ((screen.get_width()-320)/2+10, (screen.get_height()-150)/2+3))
                screen.blit(passwordLogin, ((screen.get_width()-320)/2+10, (screen.get_height()-0)/2+3))
                screen.blit(submitLogin, ((screen.get_width()-320+submitLogin.get_width())/2, (screen.get_height()+150+submitLogin.get_height())/2))
                screen.blit(goToRegister, ((screen.get_width()+350)/2 - 115 - (goToRegister.get_width()/2), (screen.get_height()+400)/2 - 25 - 15))

                screen.blit(renderLoginUsername, ((screen.get_width()-320)/2+10, (screen.get_height()-150+renderLoginUsername.get_height()+25)/2))

                screen.blit(closeIcon, self.closeLoginContainer)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.closeLoginContainer.collidepoint(event.pos):
                        self.openedWindow = False
                    elif self.goToRegister.collidepoint(event.pos):
                        self.openedWindow = "register"

                    elif self.inputUsernameLogin.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.userNameColor = "skyblue"
                        self.selectedInput = "username"


                    elif self.inputPasswordLogin.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.passwordColor = "skyblue"
                        self.selectedInput = "password"




        def register(self):
            if self.openedWindow == "register":

                screen.blit(blackBackground, (0, 0))
                pygame.draw.rect(screen, 'white', ((screen.get_width()-350)/2, (screen.get_height()-400)/2, 350, 400))

                self.inputUsernameRegister = pygame.draw.rect(screen, self.colors.nameColor, ((screen.get_width()-320)/2, (screen.get_height()-200)/2, 320, 60))
                self.inputEmailRegister = pygame.draw.rect(screen, self.colors.userNameColor, ((screen.get_width()-320)/2, (screen.get_height()-50)/2, 320, 60))
                self.inputPasswordRegister = pygame.draw.rect(screen, self.colors.passwordColor, ((screen.get_width()-320)/2, (screen.get_height()+100)/2, 320, 60))
                self.inputSubmitRegister = pygame.draw.rect(screen, (0, 100, 0), ((screen.get_width()-320)/2, (screen.get_height()+250)/2, 320, 40))
                self.closeRegisterContainer = closeIcon.get_rect( center=((screen.get_width()+350)/2, (screen.get_height()-400)/2) )

                screen.blit(titleRegister, ((screen.get_width()-titleRegister.get_width())/2, 165))
                screen.blit(usernameRegister, ((screen.get_width()-315)/2, (screen.get_height()-200+3)/2))
                screen.blit(emailRegister, ((screen.get_width()-315)/2, (screen.get_height()-50)/2+3))
                screen.blit(passwordRegister, ((screen.get_width()-315)/2, (screen.get_height()+100+3)/2))
                screen.blit(submitRegister, ((screen.get_width()-290+submitRegister.get_width())/2, (screen.get_height()+250+submitRegister.get_height())/2))

                screen.blit(closeIcon, self.closeRegisterContainer)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.closeRegisterContainer.collidepoint(event.pos):
                        self.openedWindow = False

                    if self.inputUsernameRegister.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.nameColor = "skyblue"
                        self.selectedInput = "name"

                    elif self.inputEmailRegister.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.userNameColor = "skyblue"
                        self.selectedInput = "username"

                    elif self.inputPasswordRegister.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.passwordColor = "skyblue"
                        self.selectedInput = "password"





    # ============ Variables ============ #
    windows = interfaceAuth()
    blackBackground = pygame.image.load(MAIN_DIR + '/images/backgroundBlack.png')
    closeIcon = pygame.image.load(MAIN_DIR + '/images/close-icon.png')

    inputNameTxt = inputUsernameTxt = inputPasswordTxt = pygame.font.SysFont("Arial", 18)


    # Register txt
    titleRegister = pygame.font.SysFont("Arial", 25).render("Cadastre-se", True, (0, 0, 0))
    usernameRegister = pygame.font.SysFont("Comic Sans MS", 13).render("Nome de usuário: ", True, (82, 82, 82))
    emailRegister = pygame.font.SysFont("Comic Sans MS", 13).render("Email: ", True, (82, 82, 82))
    passwordRegister = pygame.font.SysFont("Comic Sans Ms", 13).render("Senha: ", True, (82, 82, 82))
    submitRegister = pygame.font.SysFont("Arial", 16).render("Finalizar Cadastro", True, (255, 255, 255))

    # Login txt
    titleLogin = pygame.font.SysFont("Arial", 25).render("Fazer Log In", True, (0, 0, 0))
    usernameLogin = pygame.font.SysFont("Comic Sans MS", 13).render("Usuário ou Email: ", True, (82, 82, 82))
    passwordLogin = pygame.font.SysFont("Comic Sans MS", 13).render("Senha: ", True, (82, 82, 82))
    submitLogin = pygame.font.SysFont("Arial", 16).render("Entrar", True, (255, 255, 255))
    goToRegister = pygame.font.SysFont("Arial", 12).render("Não tem uma conta? Cadastre-se", True, (82, 82, 82))


    clock = pygame.time.Clock()
    while True:
        clock.tick(120)

        screen.fill('skyblue')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if windows.openedWindow != False and windows.selectedInput != False:
                    windows.username += event.unicode


        screen.blit(Button.ButtonPlay, (Button.ButtonX, Button.ButtonY))

    
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickX = event.pos[0]
            clickY = event.pos[1]
            
            if (clickX > Button.ButtonX and clickX < Button.ButtonX + Button.ButtonPlay.get_width()) and (clickY > Button.ButtonY and clickY < Button.ButtonY + Button.ButtonPlay.get_height()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                Afile = open(MAIN_DIR + "/localStorage.json")
                JsonFile = json.load(Afile)
                Afile.close()

                if JsonFile["IsAuthenticated"] == True:
                    break
                else:
                    if windows.openedWindow == False:
                        windows.openedWindow = "login"

        if windows.openedWindow == "login":
            windows.login()
        elif windows.openedWindow == "register":
            windows.register()


        pygame.display.flip()

    return
