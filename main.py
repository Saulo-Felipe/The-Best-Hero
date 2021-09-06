import pygame
import json

from content import mainScreen
from content import chooseMode

screen = pygame.display.set_mode((1140, 724))


pygame.init()

mainScreen.mainScreen(screen)
chooseMode.chooseMode(screen)

pygame.quit()
