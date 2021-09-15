import pygame
from content import oneLevel

from content.mainScreen import mainScreen
from content.ranking import rankingScreen
from content.oneLevel import oneLevel


screen = pygame.display.set_mode((1140, 724))

pygame.init()

oneLevel(screen)
# mainScreen.mainScreen(screen)
# rankingScreen(screen)

pygame.quit()
