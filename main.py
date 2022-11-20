import pygame

from content.mainScreen import mainScreen

screen = pygame.display.set_mode((1140, 724))

pygame.init()

mainScreen.mainScreen(screen)

pygame.quit()
