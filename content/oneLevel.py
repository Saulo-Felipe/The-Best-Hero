import pygame

def oneLevel(screen):

    class MoveBackground:
        x = 0
        y = 0

    background = pygame.image.load('./images/levels/level01-background.png')

    clock = pygame.time.Clock()
    while True:
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        MoveBackground.x -= 1
    
        screen.blit(background, (MoveBackground.x, MoveBackground.y))

        pygame.display.flip()
    
    return