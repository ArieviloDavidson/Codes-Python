# LETS CODE, LETS PLAY

import pygame # CRIAÇÃO DE JOGOS
import os # UTILIZAR E/S DA MAQUINA
import random # GERAR VALOR ALEATORIO

# CONFIGURAÇÕES DE TAMANHO DE TELA
TELA_LARGURA = 500
TELA_ALTURA = 800

# INICIALIZANDO TODAS AS IMAGENS
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('cloneflappybird/imagens', 'bird3.png')))
]

# INICIALIZANDO FONTE
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

# DEFINICAO DAS CLASSES DE TODOS OS ELEMENTOS
class Passaro:
    IMGS = IMAGENS_PASSARO
    # CRIANDO AS ANIMAÇÕES PARA O PASSARIO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    # VARIAVEIS (FUNCOES) DO PASSARO
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
    
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        # CALCULANDO O DESLOCAMENTO
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        
        # RESTRINGIR O DESLOCAMENTO
        if deslocamento > 16 :
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
            
        self.y += deslocamento
        
        # ANGULO DO PASSARO PARA DEIXAR MAIS FLUIDO
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
                
    def desenhar(self, tela):
        # IMAGEM DO PASSARO
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4+1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
        
        # CAINDO NÃO BATE ASA
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2
        
        # DESENHAR A IMAGEM
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Cano:
    DISTANCIA = 250 
    VELOCIDADE = 5
    
    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_BASE = IMAGEM_CANO
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.passou = False
        self.definir_altura()
        
    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA
        
    def mover(self):
        self.x -= self.VELOCIDADE
        
    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))
        
    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)
        
        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
        
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)
        
        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        
    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA
            
    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))
        
def desenhar_tela(tela, passaro, canos, chao, pontos):
    #  DESENHANDO TODA A TELA DO JOGO
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)
    texto = FONTE_PONTOS.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (300, 10))
    chao.desenhar(tela)
    
    pygame.display.update()
    
# FUNCAO MAIN IRA CRIAR TODOS OS OBJETOS DO JOGO
def main():
    # CRIANDO PASSARO
    passaro = Passaro(230, 350)
    # CRIANDO CHAO
    chao = Chao(730)
    # CRIANDO CANOS
    canos = [Cano(700)]
    # TELA E PONTOS
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    
    rodando = True
    while rodando:
        
        relogio.tick(30) # FRAMERATE DO JOGO
        
        # ANALISANDO EVENTOS COM PYGAME PARA INTERAGIR COM USUARIO
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    passaro.pular()
                    
        # MOVIMENTACAO DO JOGO
        passaro.mover()
        chao.mover()
        
        # LOGICA PARA VER SE O PASSARO BATEU NO CANO OU PASSOU DO CANO
        adicionar_cano = False
        remover_canos = []
        
        for cano in canos:
            if cano.colidir(passaro):
                pygame.quit()
                quit()
            if not cano.passou and passaro.x > cano.x:
                cano.passou = True
                adicionar_cano = True
                
            cano.mover()
            
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)
                
        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        
        for cano in remover_canos:
            canos.remove(cano)
            
        if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
            pygame.quit()
            quit()
        
        desenhar_tela(tela, passaro, canos, chao, pontos)
        
if __name__ == '__main__':
    main()   