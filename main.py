import pygame
from content import oneLevel

from content.mainScreen import mainScreen
from content.ranking import rankingScreen
from content.oneLevel import oneLevel
from content.threeLevel import threeLevel
from content.twoLevel import twoLevel

screen = pygame.display.set_mode((1140, 724))

pygame.init()

# oneLevel.oneLevel(screen)
mainScreen.mainScreen(screen)
# rankingScreen(screen)
# threeLevel.threeLevel(screen)
# twoLevel.twoLevel(screen)

pygame.quit()
