import pygame
import sys
import random

pygame.init()

LARGURA = 800
ALTURA = 600
FPS = 60
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Escape do Labirinto")
clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 64)
fonte_pequena = pygame.font.SysFont(None, 32)

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (60, ALTURA // 2)
        self.vel = 5
        self.vida = 3

    def update(self, paredes):
        teclas = pygame.key.get_pressed()
        dx, dy = 0, 0
        if teclas[pygame.K_LEFT]: dx = -self.vel
        if teclas[pygame.K_RIGHT]: dx = self.vel
        if teclas[pygame.K_UP]: dy = -self.vel
        if teclas[pygame.K_DOWN]: dy = self.vel

        self.rect.x += dx
        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                self.rect.x -= dx

        self.rect.y += dy
        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                self.rect.y -= dy

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > LARGURA:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > ALTURA:
            self.dy *= -1

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Saida(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

parede1 = Parede(200, 100, 20, 600)
parede2 = Parede(400, 0, 20, 500)
parede3 = Parede(600, 100, 20, 600)
paredes = pygame.sprite.Group(parede1, parede2, parede3)

saida = Saida(740, 520, 40, 40)

jogador = Jogador()
inimigo1 = Inimigo(300, 150, 3, 0)
inimigo2 = Inimigo(100, 400, 0, 3)
inimigos = pygame.sprite.Group(inimigo1, inimigo2)

all_sprites = pygame.sprite.Group(jogador, parede1, parede2, parede3, saida, inimigo1, inimigo2)

deve_continuar = True
venceu = False
while deve_continuar:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    if not venceu and jogador.vida > 0:
        jogador.update(paredes)
        inimigos.update()
        if jogador.rect.colliderect(saida.rect):
            venceu = True

        for inimigo in inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.vida -= 1
                jogador.rect.center = (60, ALTURA // 2)  # reset posição

    janela.fill(PRETO)
    all_sprites.draw(janela)

    vida_texto = fonte_pequena.render(f"Vida: {jogador.vida}", True, BRANCO)
    janela.blit(vida_texto, (10, 10))

    if venceu:
        texto = fonte.render("Você escapou!", True, VERMELHO)
        janela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))
    elif jogador.vida <= 0:
        texto = fonte.render("Game Over", True, VERMELHO)
        janela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))

    pygame.display.flip()

pygame.quit()
sys.exit()