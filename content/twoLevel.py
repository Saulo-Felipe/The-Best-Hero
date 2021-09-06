import pygame


def twoLevel(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        
        pygame.display.flip()

    return