import pygame 
from root import MAIN_DIR


def WinGame(screen):
    class Images:
        optionsDisplay = pygame.image.load(MAIN_DIR + "/images/levels/winGame.png")
        backgroundBlack = pygame.image.load(MAIN_DIR + "/images/mainScreen/backgroundBlack.png")

    screen.blit(Images.backgroundBlack, (0, 0))
    screen.blit(Images.optionsDisplay, ((screen.get_width()-Images.optionsDisplay.get_width())/2, (screen.get_height()-Images.optionsDisplay.get_height())/2))

        
