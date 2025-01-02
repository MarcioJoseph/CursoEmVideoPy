import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Exemplo de Reinício de Jogo")

# Definindo cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Função para inicializar os elementos do jogo
def init_game():
    # Exemplo de inicialização de variáveis
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player_speed = 5
    return player_x, player_y, player_speed

# Função para reiniciar o jogo
def restart_game():
    return init_game()

# Inicializando o jogo
player_x, player_y, player_speed = init_game()

# Loop principal do jogo
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movendo o jogador com as teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Desenhando o jogador
    pygame.draw.rect(screen, RED, (player_x, player_y, 50, 50))

    # Verificando condição de reinício (Exemplo: pressionar a tecla R)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # Pressione "R" para reiniciar o jogo
        player_x, player_y, player_speed = restart_game()

    # Atualizando a tela
    pygame.display.flip()

    # Controlando a taxa de quadros por segundo
    pygame.time.Clock().tick(60)

# Finalizando o Pygame
pygame.quit()
sys.exit()
