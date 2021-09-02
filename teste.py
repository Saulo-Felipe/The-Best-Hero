import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
class Cat:
    def __init__(self):
        self.image = pygame.image.load('./images/button_play.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect(center=(400, 300))
        self.mask = pygame.mask.from_surface(self.image)
running = True
cat = Cat()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pos = pygame.mouse.get_pos()
    pos_in_mask = pos[0] - cat.rect.x, pos[1] - cat.rect.y
    touching = cat.rect.collidepoint(pos) and cat.mask.get_at(pos_in_mask)

    screen.fill(pygame.Color('red') if touching else pygame.Color('green'))
    screen.blit(cat.image, cat.rect)
    pygame.display.update()