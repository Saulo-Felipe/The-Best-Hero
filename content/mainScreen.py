import pygame
import json
from root import MAIN_DIR
from root import connection



def mainScreen(screen):

    class Button:
        imgBtn = pygame.image.load(MAIN_DIR + '/images/mainScreen/play.png')
        buttonPlay = imgBtn.get_rect(topleft=(437+10, 418))


    class interfaceAuth():
        def __init__(self):
            self.openedWindow = False

            self.name = str()
            self.username = str()
            self.password = str()

            self.msgError = str()
            self.msgSuccess = str()

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
                renderLoginErrorMsg = loginMsgErrorTxt.render(self.msgError, True, (200, 0, 0))
                renderLoginSuccessMsg = loginMsgSuccessTxt.render(self.msgSuccess, True, (0, 150, 0))

                screen.blit(titleLogin, ((screen.get_width()-titleRegister.get_width())/2, 175))
                screen.blit(usernameLogin, ((screen.get_width()-320)/2+10, (screen.get_height()-150)/2+3))
                screen.blit(passwordLogin, ((screen.get_width()-320)/2+10, (screen.get_height()-0)/2+3))
                screen.blit(submitLogin, ((screen.get_width()-320+submitLogin.get_width())/2, (screen.get_height()+150+submitLogin.get_height())/2))
                screen.blit(goToRegister, ((screen.get_width()+350)/2 - 115 - (goToRegister.get_width()/2), (screen.get_height()+400)/2 - 25 - 15))

                screen.blit(renderLoginUsername, ((screen.get_width()-320)/2+10, (screen.get_height()-150+renderLoginUsername.get_height()+25)/2))
                screen.blit(renderLoginPassword, ((screen.get_width()-320)/2+10, (screen.get_height()-0+renderLoginPassword.get_height()+25)/2))
                screen.blit(renderLoginErrorMsg, ((screen.get_width()-renderLoginErrorMsg.get_width())/2, (screen.get_height()+400)/2 - 40 - (renderLoginErrorMsg.get_height()*2)))
                screen.blit(renderLoginSuccessMsg, ((screen.get_width()-renderLoginSuccessMsg.get_width())/2, (screen.get_height()+400)/2 - 40 - (renderLoginSuccessMsg.get_height()*2)))

                screen.blit(closeIcon, self.closeLoginContainer)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.closeLoginContainer.collidepoint(event.pos):
                        self.openedWindow = False
                    elif self.goToRegister.collidepoint(event.pos):
                        self.openedWindow = "register"

                    if self.inputUsernameLogin.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.userNameColor = "skyblue"
                        self.selectedInput = "username"

                    elif self.inputPasswordLogin.collidepoint(event.pos):
                        self.resetColors()
                        self.colors.passwordColor = "skyblue"
                        self.selectedInput = "password"
                    
                    if self.inputSubmitLogin.collidepoint(event.pos):
                        if len(self.username) < 1 and len(self.password) < 1:
                            self.msgError = "Por favor, preencha todos os campos."
                            self.msgSuccess = ""
                        else:
                            connection.execute(f"SELECT * FROM player WHERE username = '{self.username}' OR email = '{self.username}'")
                            result = connection.fetchall()

                            if len(result) != 0:
                                user = result[0]
                                userId = user[0]
                                userName = user[1]
                                userPassword = user[2]
                                userEmail = user[3]

                                if self.password == userPassword:
                                    self.msgSuccess = "Login realizando com sucesso!"
                                    self.msgError = ""

                                    refreshLogin = {
                                        "IsAuthenticated": True, 
                                        "id": userId,
                                        "name": userName,
                                        "email": userEmail
                                    }

                                    Afile = open("localStorage.json", "w")
                                    json.dump(refreshLogin, Afile)
                                    Afile.close()

                                    self.openedWindow = False

                                else:
                                    self.msgError = f"Senha incorreta para {self.username}"
                                    self.msgSuccess = ""
                            else:
                                self.msgError = "Não existe nenhuma conta com esses dados"
                                self.msgSuccess = ""


        def register(self):
            if self.openedWindow == "register":

                screen.blit(blackBackground, (0, 0))
                pygame.draw.rect(screen, 'white', ((screen.get_width()-350)/2, (screen.get_height()-400)/2, 350, 450))

                self.inputUsernameRegister = pygame.draw.rect(screen, self.colors.nameColor, ((screen.get_width()-320)/2, (screen.get_height()-200)/2, 320, 60))
                self.inputEmailRegister = pygame.draw.rect(screen, self.colors.userNameColor, ((screen.get_width()-320)/2, (screen.get_height()-50)/2, 320, 60))
                self.inputPasswordRegister = pygame.draw.rect(screen, self.colors.passwordColor, ((screen.get_width()-320)/2, (screen.get_height()+100)/2, 320, 60))
                self.inputSubmitRegister = pygame.draw.rect(screen, (0, 100, 0), ((screen.get_width()-320)/2, (screen.get_height()+250)/2, 320, 40))
                self.closeRegisterContainer = closeIcon.get_rect( center=((screen.get_width()+350)/2, (screen.get_height()-400)/2) )

                renderRegisterName = inputNameTxt.render(self.name, True, (0, 0, 0))
                renderRegisterUsername = inputUsernameTxt.render(self.username, True, (0, 0, 0))
                renderRegisterPassword = inputPasswordTxt.render(self.password, True, (0, 0, 0))
                renderRegisterErrorMsg = registerMsgErrorTxt.render(self.msgError, True, (200, 0, 0)) 
                renderRegisterSuccessMsg = registerMsgSuccessTxt.render(self.msgSuccess, True, (0, 150, 0))

                screen.blit(titleRegister, ((screen.get_width()-titleRegister.get_width())/2, 165))
                screen.blit(usernameRegister, ((screen.get_width()-315)/2+10, (screen.get_height()-200+3)/2))
                screen.blit(emailRegister, ((screen.get_width()-315)/2+10, (screen.get_height()-50)/2+3))
                screen.blit(passwordRegister, ((screen.get_width()-315)/2+10, (screen.get_height()+100+3)/2))
                screen.blit(submitRegister, ((screen.get_width()-290+submitRegister.get_width())/2, (screen.get_height()+250+submitRegister.get_height())/2))

                screen.blit(renderRegisterName, ((screen.get_width()-320)/2+10, (screen.get_height()-200 + renderRegisterName.get_height()+25)/2))
                screen.blit(renderRegisterUsername, ((screen.get_width()-320)/2+10, (screen.get_height()-50 + renderRegisterUsername.get_height()+25)/2))
                screen.blit(renderRegisterPassword, ((screen.get_width()-320)/2+10, (screen.get_height()+100 + renderRegisterPassword.get_height()+25)/2))
                screen.blit(renderRegisterErrorMsg, ((screen.get_width()-renderRegisterErrorMsg.get_width())/2, (screen.get_height()+250)/2+80))
                screen.blit(renderRegisterSuccessMsg, ((screen.get_width()-renderRegisterSuccessMsg.get_width())/2, (screen.get_height()+250)/2+80))


                screen.blit(closeIcon, self.closeRegisterContainer)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.inputSubmitRegister.collidepoint(event.pos):
                        if len(self.username) < 3 or len(self.name) < 3 or len(self.password) < 3:
                            self.msgError = "Insira pelo menos 3 caracteres em cada campo."
                            self.msgSuccess = ""
                        else:
                            connection.execute(f"SELECT * FROM player WHERE email = '{self.username}'")
                            result = connection.fetchall()

                            if len(result) == 0:
                                connection.execute(f"SELECT * FROM player WHERE username = '{self.name}'")
                                result = connection.fetchall()

                                if len(result) == 0:
                                    connection.execute(f"INSERT INTO player (username, password, email) values ('{self.name}', '{self.password}', '{self.username}')")

                                    self.msgSuccess = "Cadastrado com sucesso! realize o Log in."
                                    self.msgError = ""
                                    
                                    self.openedWindow = "login"
                                else:
                                    self.msgError = "Esse nome de usuário já foi usado"
                                    self.msgSuccess = ""
                                    
                            else:
                                self.msgError = "Esse email já está em uso."
                                self.msgSuccess = ""


    # ============ Variables ============ #
    windows = interfaceAuth()
    blackBackground = pygame.image.load(MAIN_DIR + '/images/mainScreen/backgroundBlack.png')
    closeIcon = pygame.image.load(MAIN_DIR + '/images/mainScreen/close-icon.png')
    background = pygame.image.load(MAIN_DIR + '/images/mainScreen/initialScreen.png')

    logoutBtn = pygame.image.load(MAIN_DIR + '/images/mainScreen/exit.png')
    logoutRect = logoutBtn.get_rect(topleft=(screen.get_width()-logoutBtn.get_width()-55, screen.get_height() - logoutBtn.get_height()-50))
    enterBtn = pygame.image.load(MAIN_DIR + '/images/mainScreen/enter.png')
    enterRect = enterBtn.get_rect(topleft=(screen.get_width()-enterBtn.get_width()-55, screen.get_height() - enterBtn.get_height()-50))

    inputNameTxt = inputUsernameTxt = inputPasswordTxt = pygame.font.SysFont("Arial", 18)
    registerMsgErrorTxt = loginMsgErrorTxt = registerMsgSuccessTxt = loginMsgSuccessTxt = pygame.font.SysFont("Arial", 12)

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

    def verifyFile():
        Afile = open("localStorage.json")
        JsonFile = json.load(Afile)
        Afile.close()

        return JsonFile


    clock = pygame.time.Clock()
    while True:
        clock.tick(120)

        screen.blit(background, (-1293, -2))
        screen.blit(Button.imgBtn, Button.buttonPlay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Verificação de digitação
            if event.type == pygame.KEYDOWN:
                if windows.openedWindow != False and windows.selectedInput != False:
                    if windows.selectedInput == "username":
                        if event.key == pygame.K_BACKSPACE:
                            windows.username = windows.username[:-1]
                        else:
                            if len(windows.username) < 26:
                                windows.username += event.unicode
                    elif windows.selectedInput == "password":
                        if event.key == pygame.K_BACKSPACE:
                            windows.password = windows.password[:-1]
                        else:
                            if len(windows.password) < 26:
                                windows.password += event.unicode
                    elif windows.selectedInput == "name":
                        if event.key == pygame.K_BACKSPACE:
                            windows.name = windows.name[:-1]
                        else:
                            if len(windows.name) < 26:
                                windows.name += event.unicode


                    

        # Verifica se o usuario está logado após ao clique do PLAY
        if event.type == pygame.MOUSEBUTTONDOWN:

            if (Button.buttonPlay.collidepoint(event.pos)):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if verifyFile()["IsAuthenticated"] == True:
                    break
                else:
                    if windows.openedWindow == False:
                        windows.openedWindow = "login"
                        



            

        # Se o usuario está ou não logado
        if verifyFile()["IsAuthenticated"] == True:
            screen.blit(logoutBtn, logoutRect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if logoutRect.collidepoint(event.pos):
                    Afile = open("localStorage.json", "w")
                    newJson = {"IsAuthenticated": False}
                    json.dump(newJson, Afile)
                    Afile.close()

        else:
            screen.blit(enterBtn, enterRect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if enterRect.collidepoint(event.pos):
                    windows.openedWindow = "login"


        if windows.openedWindow == "login":
            windows.login()
        elif windows.openedWindow == "register":
            windows.register()
            # Register input focus
            if event.type == pygame.MOUSEBUTTONUP:
                if windows.inputUsernameRegister.collidepoint(event.pos):
                    windows.resetColors()
                    windows.colors.nameColor = "skyblue"
                    windows.selectedInput = "name"

                elif windows.inputEmailRegister.collidepoint(event.pos):
                    windows.resetColors()
                    windows.colors.userNameColor = "skyblue"
                    windows.selectedInput = "username"

                elif windows.inputPasswordRegister.collidepoint(event.pos):
                    windows.resetColors()
                    windows.colors.passwordColor = "skyblue"
                    windows.selectedInput = "password"


        pygame.display.flip()


    return