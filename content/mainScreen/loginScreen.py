import pygame
pygame.font.init()
from root import MAIN_DIR

class configTxt:
    email = pygame.font.SysFont("Arial", 13).render("Email ou Nome de usuário: ", True, (82, 82, 82))
    password = pygame.font.SysFont("Arial", 13).render("Senha: ", True, (82, 82, 82))
    submit = pygame.font.SysFont("Arial", 17).render("Entrar", True, (255, 255, 255))

    emailValue = pygame.font.SysFont("Arial", 17)
    passwordValue = pygame.font.SysFont("Arial", 17)

    title = pygame.font.SysFont("Arial", 25).render("Entre na sua conta", True, (0, 0, 0,))
    txtRegister = pygame.font.SysFont("Arial", 13).render("Não tem uma conta? Cadastre-se", True, (82, 82, 82))
    goToRegister = txtRegister.get_rect(topleft=((1140-350)/2+100, (724-400)/2+355))


    emailContent = ""
    passwordContent = ""

    inputFocus = False


class Colors:
    email = "gray"
    password = "gray"
    def reset():
        Colors.email = "gray"
        Colors.password = "gray"

class Images:
    backgroundBlurd = pygame.image.load(MAIN_DIR + '/images/mainScreen/backgroundBlack.png')

    closeImg = pygame.image.load(MAIN_DIR + '/images/mainScreen/close-icon.png')
    closeLogin = closeImg.get_rect(topleft=( (1140-350)/2+ 330, (724-400)/2 - 25))


def drawLogin(screen, event, state):

    screenWidth = screen.get_width()
    screenHeight = screen.get_height()

    screen.blit(Images.backgroundBlurd, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ( (screenWidth-350)/2, (screenHeight-400)/2, 350, 400) )
    screen.blit(Images.closeImg, Images.closeLogin)

    class Inputs:
        email = pygame.draw.rect(screen, Colors.email, ( (screenWidth-320)/2, (screenHeight-120)/2, 320, 60) )
        password = pygame.draw.rect(screen, Colors.password, ( (screenWidth-320)/2, (screenHeight+20)/2, 320, 60) )
        submit = pygame.draw.rect(screen, (0, 100, 0), ( (screenWidth-320)/2, (screenHeight+160)/2, 120, 40 ) )

    def Texts():
        screen.blit(configTxt.email, ( (screenWidth-320)/2+10, (screenHeight-120)/2+5 ) )
        screen.blit(configTxt.password, ( (screenWidth-320)/2+10, (screenHeight+20)/2+5 ) )
        screen.blit(configTxt.submit, ( (screenWidth-310+configTxt.submit.get_width())/2, (screenHeight+150+configTxt.submit.get_height())/2, 120, 40 ) )

        renderEmail = configTxt.emailValue.render(configTxt.emailContent, True, (0, 0, 0))
        renderPassword = configTxt.passwordValue.render(configTxt.passwordContent, True, (0, 0, 0))

        screen.blit(renderEmail, ( (screenWidth-320)/2+10, (screenHeight-120)/2+5+renderEmail.get_height()) )
        screen.blit(renderPassword, ( (screenWidth-320)/2+10, (screenHeight+20)/2+5+renderEmail.get_height()) )

        screen.blit(renderEmail, ( (screenWidth-320)/2+10, (screenHeight-120)/2+5+renderEmail.get_height()) )
        screen.blit(renderPassword, ( (screenWidth-320)/2+10, (screenHeight+20)/2+5+renderEmail.get_height()) )

        screen.blit(configTxt.title, ( (screenWidth-configTxt.title.get_width())/2, 220))
        screen.blit(configTxt.txtRegister, configTxt.goToRegister)
    Texts()


    if event.type == pygame.MOUSEBUTTONUP:

        #focus input
        if Inputs.email.collidepoint(event.pos):
            Colors.reset()
            Colors.email = "skyblue"
            configTxt.inputFocus = "email"
        elif Inputs.password.collidepoint(event.pos):
            Colors.reset()
            Colors.password = "skyblue"
            configTxt.inputFocus = "password"
        elif Inputs.submit.collidepoint(event.pos):
            print('Submit')
        else:
            configTxt.inputFocus = False
            Colors.reset()

        # Close Login
        if Images.closeLogin.collidepoint(event.pos):
            return False

        # Go to register
        if configTxt.goToRegister.collidepoint(event.pos):
            return "register"

    # Typing...
    if state != False:
        if configTxt.inputFocus == "email":
            configTxt.emailContent = configTxt.emailContent[:-1] if state == "delete" else configTxt.emailContent + state
            
        elif configTxt.inputFocus == "password":
            configTxt.passwordContent = configTxt.passwordContent[:-1] if state == "delete" else configTxt.passwordContent + state

    return "login"