import pygame
from root import MAIN_DIR
from root import connection

class Images:
    backgroundBlurd = pygame.image.load(MAIN_DIR + '/images/backgroundBlack.png')

    closeImg = pygame.image.load(MAIN_DIR + '/images/mainScreen/close-icon.png')
    closeRegister = closeImg.get_rect(topleft=( (1140-350)/2+ 330, (724-450)/2 - 25))

class configTxt:
    username = pygame.font.SysFont("Arial", 13).render("Nome de usuário: ", True, (82, 82, 82))
    email = pygame.font.SysFont("Arial", 13).render("Email: ", True, (82, 82, 82))
    password = pygame.font.SysFont("Arial", 13).render("Senha: ", True, (82, 82, 82))
    submit = pygame.font.SysFont("Arial", 17).render("Finalizar Cadastro", True, (255, 255, 255))

    emailValue = pygame.font.SysFont("Arial", 17)
    passwordValue = pygame.font.SysFont("Arial", 17)
    usernameValue = pygame.font.SysFont("Arial", 17)

    title = pygame.font.SysFont("Arial", 25).render("Cadastre-se", True, (0, 0, 0,))

    errorTxt = pygame.font.SysFont("Arial", 13)
    successTxt = pygame.font.SysFont("Arial", 13)

    errorMsg = ""
    successMsg = ""

    usernameContent = ""
    emailContent = ""
    passwordContent = ""

    inputFocus = False


class Colors:
    username = "gray"
    email = "gray"
    password = "gray"

    def reset():
        Colors.username = "gray"
        Colors.email = "gray"
        Colors.password = "gray"



def drawRegister(screen, event, state):
    screenWidth = screen.get_width()
    screenHeight = screen.get_height()

    screen.blit(Images.backgroundBlurd, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ( (screenWidth-350)/2, (screenHeight-450)/2, 350, 450) )
    screen.blit(Images.closeImg, Images.closeRegister)

    class Inputs: #Colors.username
        username = pygame.draw.rect(screen, Colors.username, ( (screenWidth-320)/2, (screenHeight-220)/2, 320, 60))
        email = pygame.draw.rect(screen, Colors.email, ( (screenWidth-320)/2, (screenHeight-80)/2, 320, 60) )
        password = pygame.draw.rect(screen, Colors.password, ( (screenWidth-320)/2, (screenHeight+60)/2, 320, 60) )
        submit = pygame.draw.rect(screen, (0, 100, 0), ( (screenWidth-320)/2, (screenHeight+200)/2, 320, 40 ) )


    def Texts():
        screen.blit(configTxt.username, ( (screenWidth-320)/2+10, (screenHeight-260)/2+25 ))
        screen.blit(configTxt.email, ( (screenWidth-320)/2+10, (screenHeight-120)/2+25 ))
        screen.blit(configTxt.password, ( (screenWidth-320)/2+10, (screenHeight+20)/2+25 ))
        screen.blit(configTxt.submit, ( (screenWidth-310+configTxt.submit.get_width())/2, (screenHeight+190+configTxt.submit.get_height())/2, 120, 40 ))

        renderUsername = configTxt.usernameValue.render(configTxt.usernameContent, True, (0, 0, 0))
        renderEmail = configTxt.emailValue.render(configTxt.emailContent, True, (0, 0, 0))
        renderPassword = configTxt.passwordValue.render(configTxt.passwordContent, True, (0, 0, 0))

        screen.blit(renderUsername, ( (screenWidth-320)/2+10, (screenHeight-260)/2+25+renderUsername.get_height()) )
        screen.blit(renderEmail, ( (screenWidth-320)/2+10, (screenHeight-120)/2+25+renderEmail.get_height()) )
        screen.blit(renderPassword, ( (screenWidth-320)/2+10, (screenHeight+20)/2+25+renderEmail.get_height()) )

        screen.blit(configTxt.title, ( (screenWidth-configTxt.title.get_width())/2, 170))

        renderErrorMsg = configTxt.errorTxt.render(configTxt.errorMsg, True, (150, 0, 0))
        renderSuccessMsg = configTxt.successTxt.render(configTxt.successMsg, True, (0, 150, 0))

        screen.blit(renderErrorMsg, ((1140-renderErrorMsg.get_width())/2, (724-400)/2+350))
        screen.blit(renderSuccessMsg, ((1140-renderSuccessMsg.get_width())/2, (724-400)/2+350))
    Texts()

    def register():
        if len(configTxt.usernameContent) < 3:
            configTxt.successMsg = ""
            configTxt.errorMsg = "Nome de usuário muito pequeno"
        elif len(configTxt.emailContent) < 3:
            configTxt.successMsg = ""
            configTxt.errorMsg = "Email inválido"
        elif len(configTxt.passwordContent) < 3:
            configTxt.successMsg = ""
            configTxt.errorMsg = "Senha muito fraca"
        else:
            connection.execute(f"SELECT * FROM player WHERE email = '{ configTxt.emailContent }'")
            emailResult = connection.fetchall()

            if len(emailResult) == 0:
                connection.execute(f"SELECT * FROM player WHERE username = '{ configTxt.usernameContent }'")
                usernameResult = connection.fetchall()

                if len(usernameResult) == 0:

                    connection.execute(f"INSERT INTO player (username, email, password) VALUES ('{ configTxt.usernameContent }', '{ configTxt.emailContent }', '{ configTxt.passwordContent }')")
                    configTxt.errorMsg = ""
                    configTxt.successMsg = "Usuário cadastrado com sucesso!"
                    return 

                else:
                    configTxt.errorMsg = "Nome de usuario já está em uso"
            else:
                configTxt.successMsg = ""
                configTxt.errorMsg = "Esse email pertence a outra conta"

    if event.type == pygame.MOUSEBUTTONUP:
        #focus input
        if Inputs.username.collidepoint(event.pos):
            Colors.reset()
            Colors.username = "skyblue"
            configTxt.inputFocus = "username"        
        elif Inputs.email.collidepoint(event.pos):
            Colors.reset()
            Colors.email = "skyblue"
            configTxt.inputFocus = "email"
        elif Inputs.password.collidepoint(event.pos):
            Colors.reset()
            Colors.password = "skyblue"
            configTxt.inputFocus = "password"
        else:
            configTxt.inputFocus = False
            Colors.reset()

        # Close register
        if Images.closeRegister.collidepoint(event.pos):
            configTxt.usernameContent = ""
            configTxt.emailContent = ""
            configTxt.passwordContent = ""

            return False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if Inputs.submit.collidepoint(event.pos):
            register()

    # Typing...
    if state != False:
        if configTxt.inputFocus == "email":
            configTxt.emailContent = configTxt.emailContent[:-1] if state == "delete" else configTxt.emailContent + state
            
        elif configTxt.inputFocus == "password":
            configTxt.passwordContent = configTxt.passwordContent[:-1] if state == "delete" else configTxt.passwordContent + state

        elif configTxt.inputFocus == "username":
            configTxt.usernameContent = configTxt.usernameContent[:-1] if state == "delete" else configTxt.usernameContent + state
        


    return "register"