import pygame

def mainScreen(screen):

    class Button:
        btn = pygame.image.load('./images/button_play.png')        
        ButtonPlay = pygame.transform.scale(btn, (int(btn.get_width()/2), int(btn.get_height()/2)))
        ButtonX = (1140 - ButtonPlay.get_width())/2
        ButtonY = (724 - ButtonPlay.get_height())/2

    def mouseMove():
        if event.type == pygame.MOUSEMOTION:
            clickX = event.pos[0]
            clickY = event.pos[1]
            if (clickX > Button.ButtonX and clickX < Button.ButtonX + Button.ButtonPlay.get_width()) and (clickY > Button.ButtonY and clickY < Button.ButtonY + Button.ButtonPlay.get_height()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    clock = pygame.time.Clock()
    while True:
        clock.tick(120)

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(Button.ButtonPlay, (Button.ButtonX, Button.ButtonY))

        mouseMove()

        if event.type == pygame.MOUSEBUTTONDOWN:
            clickX = event.pos[0]
            clickY = event.pos[1]
            
            if (clickX > Button.ButtonX and clickX < Button.ButtonX + Button.ButtonPlay.get_width()) and (clickY > Button.ButtonY and clickY < Button.ButtonY + Button.ButtonPlay.get_height()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                break

        pygame.display.flip()

    return
