import pygame
import string

pygame.init()

screen = pygame.display.set_mode((300, 300))
intermediate = pygame.surface.Surface((300, 600))
i_a = intermediate.get_rect()
x1 = i_a[0]
x2 = x1 + i_a[2]
a, b = (255, 0, 0), (60, 255, 120)
y1 = i_a[1]
y2 = y1 + i_a[3]
h = y2-y1
rate = (float((b[0]-a[0])/h),
         (float(b[1]-a[1])/h),
         (float(b[2]-a[2])/h)
         )
for line in range(y1,y2):
     color = (min(max(a[0]+(rate[0]*line),0),255),
              min(max(a[1]+(rate[1]*line),0),255),
              min(max(a[2]+(rate[2]*line),0),255)
              )
     pygame.draw.line(intermediate, color, (x1, line),(x2, line))

y = 20
f = pygame.font.SysFont('', 17)
for l in string.ascii_uppercase:
    intermediate.blit(f.render(l, True, (255, 255, 255)), (10, y))
    y += 20

clock = pygame.time.Clock()    
quit = False

scroll_y = 0

while not quit:
    quit = pygame.event.get(pygame.QUIT)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4: scroll_y = min(scroll_y + 15, 0)
            if e.button == 5: scroll_y = max(scroll_y - 15, -300)

    screen.blit(intermediate, (0, scroll_y))
    pygame.display.flip()
    clock.tick(60)