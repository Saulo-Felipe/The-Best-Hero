import pygame
from content import mainScreen
from content import chooseMode
from content import oneLevel
from content import twoLevel

screen = pygame.display.set_mode((1140, 724))

pygame.init()


mainScreen.mainScreen(screen)
chooseMode.chooseMode(screen)

pygame.quit()
