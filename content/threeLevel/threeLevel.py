import pygame, random
from pygame.locals import *
from sys import exit
from root import MAIN_DIR
import content.chooseMode as chooseMode
from root import connection
import json

def threeLevel(screen):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mixer.music.load(MAIN_DIR + '/sons/init_bird.wav')
    pygame.mixer.music.play()
    
    LARGURA_TELA = 1140
    ALTURA_TELA = 724
    VELOCIDADE = 17
    GRAVIDADE = 1
    VELOCIDADE_JOGO = 5

    LARGURA_CHAO = 2 * LARGURA_TELA 
    ALTURA_CHAO = 100

    LARGURA_CANO = 100
    ALTURA_CANO = 450
    CANO_GAP = -330 

    tela = screen


    fps = pygame.time.Clock()

    IMAGEM_FUNDO = pygame.image.load(MAIN_DIR + '/images/levels/cenario3.png').convert_alpha()
    IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO,(1140,724))
    IMAGEM_MOEDA = pygame.image.load(MAIN_DIR + '/images/levels/coin.png')
    IMAGEM_GAMEOVER = pygame.image.load(MAIN_DIR + '/images/levels/game-over-screen.png')
    IMAGEM_DESFOQUE = pygame.image.load(MAIN_DIR + '/images/backgroundBlack.png')

    class moreConfigs:
        gameInit = False
        gameOver = False
        coins = 0
        count = 0
        rankingPlayers = False

    class rects:
        exitGame = pygame.image.load(MAIN_DIR + '/images/levels/list.png')
        restart = pygame.image.load(MAIN_DIR + '/images/levels/restart.png')
        configs = pygame.image.load(MAIN_DIR + '/images/levels/config.png')

        middleScreen = screen.get_height()/2

        exitGameRect = exitGame.get_rect(topleft=(736, middleScreen-74*2))
        restartRect = restart.get_rect(topleft=(736, middleScreen-74))
        configsRect = configs.get_rect(topleft=(736, middleScreen))

        def blitOptions():
            middleScreen = rects.middleScreen

            screen.blit(rects.exitGame, rects.exitGameRect)
            screen.blit(rects.restart, rects.restartRect)
            screen.blit(rects.configs, rects.configsRect)
            screen.blit(TxtMoedaBig.render(str(int(moreConfigs.coins)), True, "orange"), (620, middleScreen-40))

            # blit ranking
            for c in range(3):
                usernameTxt = TxtRanking.render(moreConfigs.rankingPlayers[c][0], True, "black")
                pointsTxt = TxtRanking.render(str(moreConfigs.rankingPlayers[c][1]) + " Pontos", True, "black")
                
                screen.blit(usernameTxt, (400, middleScreen+middleScreen/3+15+(45*c)))
                screen.blit(pointsTxt, (400+190, middleScreen+middleScreen/3+15+(45*c)))
            

    TxtMoeda = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 30)
    TxtMoedaBig = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 40)

    TxtRanking = pygame.font.Font(MAIN_DIR + '/fonts/Peace_Sans.otf', 20)


    class Chao(pygame.sprite.Sprite):
        def __init__(self,x_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(MAIN_DIR + '/images/levels/chao.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(LARGURA_CHAO, ALTURA_CHAO))
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect[0] = x_pos
            self.rect[1] = ALTURA_TELA - ALTURA_CHAO
        def update(self):
            self.rect[0] -= VELOCIDADE_JOGO

    class Cano(pygame.sprite.Sprite):
        
        def __init__(self, invertido, x_pos, y_tamanho):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(MAIN_DIR + '/images/levels/cano1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(LARGURA_CANO,ALTURA_CANO))
            self.rect = self.image.get_rect()
            self.rect[0] = x_pos

            if invertido:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect[1] = (self.rect[3] - y_tamanho)
            else:
                self.rect[1] = ALTURA_TELA - y_tamanho

            self.mask = pygame.mask.from_surface(self.image)

        def update(self):
            self.rect[0] -= VELOCIDADE_JOGO

            if heroi.playerX == self.rect.x: 
                moreConfigs.coins += 0.5
                pygame.mixer.music.load(MAIN_DIR + '/sons/coin.wav')
                pygame.mixer.music.play()

    class Heroi(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.imagens_heroi = []
            sprite_sheet = pygame.image.load(MAIN_DIR + '/images/levels/aviao_sprite_sheet.png').convert_alpha()

            for i in range (6):
                img = sprite_sheet.subsurface((i * 200.5,0),(200.5,135))
                img = pygame.transform.scale(img,(125,95))
                self.imagens_heroi.append(img)

            self.velocidade = VELOCIDADE
            self.playerX = 200
            self.playerY = screen.get_height()/2
            self.index_lista = 0
            self.image = self.imagens_heroi[self.index_lista]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = (self.playerX,self.playerY)

        def update(self):
            if self.index_lista > 5.90:
                self.index_lista = 0

            self.index_lista += 0.22
            self.image = self.imagens_heroi[int(self.index_lista)]
            if moreConfigs.gameInit == True:
                self.velocidade += GRAVIDADE
                self.playerY += self.velocidade
            self.rect.center = (self.playerX, self.playerY)

        def voar(self):
            self.velocidade = -VELOCIDADE
            pygame.mixer.music.load(MAIN_DIR + '/sons/jump_bird.wav')
            pygame.mixer.music.play()

    def fora_da_tela(sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def canos_aleatorios(x_pos):
        tamanho = random.randint(250, 350)
        cano = Cano(False, x_pos, tamanho)
        cano_invertido = Cano(True, x_pos, ALTURA_TELA - tamanho - CANO_GAP)
        return (cano, cano_invertido)

    def game_over():
        moreConfigs.gameOver = True

        if moreConfigs.count == 0:
            pygame.mixer.music.load(MAIN_DIR + '/sons/dead_bird.wav')
            pygame.mixer.music.play()

            # ------- Inserir novos pontos na para o usuario --------
            Afile = open(MAIN_DIR + "/localStorage.json")
            Ajson = json.load(Afile)
            connection.execute(f"SELECT flappyPoints, points, username from player WHERE id = {Ajson['id']}")
            result = connection.fetchall()
            
            if int(moreConfigs.coins) > result[0][0]:
                newPoints = int(moreConfigs.coins)
                connection.execute(f"UPDATE player SET flappyPoints = {newPoints} WHERE id = {Ajson['id']}")
            
            newPoints = int(moreConfigs.coins) + result[0][1]
            connection.execute(f"UPDATE player SET points = {newPoints} WHERE id = {Ajson['id']}")

            moreConfigs.count = 1

            # ------ Mini ranking do flappy plane -------
            connection.execute(f"SELECT username, flappyPoints FROM player ORDER BY flappyPoints DESC LIMIT 3")
            result = connection.fetchall()

            moreConfigs.rankingPlayers = result
            


    grupo_heroi = pygame.sprite.Group()
    heroi = Heroi()
    grupo_heroi.add(heroi)

    grupo_chao = pygame.sprite.Group()
    for i in range(2):
        chao = Chao(LARGURA_CHAO * i)
        grupo_chao.add(chao)

    grupo_cano = pygame.sprite.Group()
    for i in range (2):
        canos = canos_aleatorios(LARGURA_TELA * i + 800)
        grupo_cano.add(canos[0])
        grupo_cano.add(canos[1]) 

    while True:
        fps.tick(55)
        tela.blit(IMAGEM_FUNDO,(0,0))
        renderMoeda = TxtMoeda.render(str(int(moreConfigs.coins)), True, "black")
        grupo_heroi.draw(tela)
        grupo_cano.draw(tela)
        grupo_chao.draw(tela)
        tela.blit(IMAGEM_MOEDA, (20, 20))

        for event in pygame.event.get():    
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.type == K_UP:
                    heroi.voar()

                    moreConfigs.gameInit = True

            if event.type == pygame.MOUSEBUTTONUP:
                if rects.restartRect.collidepoint(event.pos):
                    return threeLevel(screen)

                if rects.exitGameRect.collidepoint(event.pos):
                    return chooseMode.chooseMode(screen)

            if rects.configsRect.collidepoint(pygame.mouse.get_pos()) or rects.exitGameRect.collidepoint(pygame.mouse.get_pos()) or rects.restartRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        if fora_da_tela(grupo_chao.sprites()[0]):
            grupo_chao.remove(grupo_chao.sprites()[0])
            novo_chao = Chao(LARGURA_CHAO - 20)
            grupo_chao.add(novo_chao)

        if fora_da_tela(grupo_cano.sprites()[0]):
            grupo_cano.remove(grupo_cano.sprites()[0])
            grupo_cano.remove(grupo_cano.sprites()[0])
            canos = canos_aleatorios(LARGURA_TELA * 2)
            grupo_cano.add(canos[0]) 
            grupo_cano.add(canos[1]) 
        
            
        if pygame.sprite.groupcollide(grupo_heroi, grupo_chao, False, False, pygame.sprite.collide_mask):
            game_over()
            
        if pygame.sprite.groupcollide(grupo_heroi, grupo_cano, False, False, pygame.sprite.collide_mask):
            game_over()


        if moreConfigs.gameOver == False:
            if moreConfigs.gameInit == True:
                grupo_cano.update()
            grupo_heroi.update()
            grupo_chao.update()
        else:
            tela.blit(IMAGEM_DESFOQUE, (0, 0))
            tela.blit(IMAGEM_GAMEOVER, ((screen.get_width()-IMAGEM_GAMEOVER.get_width())/2, (screen.get_height()-IMAGEM_GAMEOVER.get_height())/2))

            rects.blitOptions()


        tela.blit(renderMoeda, (IMAGEM_MOEDA.get_width()+30, 20))

        pygame.display.flip()