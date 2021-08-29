import pygame
from pygame.locals import *
from sys import exit

from time import sleep
pygame.init()


telaLargura = 600
telaAltura = 600
elementX = 275
elementY = 0

def movePlayer():
	global elementY, elementX

	if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
		elementY -= 5
	if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
		elementY += 5
	if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
		elementX += 5
	if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
		elementX -= 5


tela = pygame.display.set_mode((telaLargura, telaAltura))

pygame.display.set_caption('Testando Pygame...')

frame = pygame.time.Clock()



while True:
	frame.tick(120) # Quanto mais alto o frame, mas rapido o jogo será executado

	tela.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()


	movePlayer()

	pygame.draw.rect(tela, (255, 0, 0), (elementX, elementY, 50, 50))

	if elementY > telaAltura:
		elementY = -50
	if elementY < -50:
		elementY = telaAltura

	if elementX > telaAltura:
		elementX = -50
	if elementX < -50:
		elementX = telaLargura



	pygame.display.update() #Atualiza a tela a cada looping

pygame.quit()
