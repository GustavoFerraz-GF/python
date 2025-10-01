import pygame

# Inicializa Pygame
pygame.init()

# Criar a janela
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Teste Pygame 🚀")

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# Finalizar
pygame.quit()