import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola e das raquetes
ball_speed_x = 5
ball_speed_y = 5
ball_size = 20

paddle_width, paddle_height = 10, 100
player_speed = 10
computer_speed = 5

# Inicializa a posição da bola e das raquetes
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
player_y = (HEIGHT // 2) - (paddle_height // 2)
computer_y = (HEIGHT // 2) - (paddle_height // 2)

# Função principal do jogo
def main():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, player_y, computer_y
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - paddle_height:
            player_y += player_speed

        # Movimentação da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisão com as bordas
        if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
            ball_speed_y *= -1

        # Colisão com as raquetes
        if (ball_x <= paddle_width and player_y <= ball_y <= player_y + paddle_height) or \
           (ball_x >= WIDTH - paddle_width - ball_size and computer_y <= ball_y <= computer_y + paddle_height):
            ball_speed_x *= -1

        # Movimentação do computador
        if computer_y + paddle_height / 2 < ball_y:
            computer_y += computer_speed
        else:
            computer_y -= computer_speed

        # Limita a raquete do computador dentro da tela
        if computer_y < 0:
            computer_y = 0
        elif computer_y > HEIGHT - paddle_height:
            computer_y = HEIGHT - paddle_height

        # Limita a bola dentro da tela
        if ball_x < 0 or ball_x > WIDTH:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x *= -1

        # Desenha tudo
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, player_y, paddle_width, paddle_height))  # Raquete do jogador
        pygame.draw.rect(screen, WHITE, (WIDTH - paddle_width, computer_y, paddle_width, paddle_height))  # Raquete do computador
        pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))  # Bola
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == "__main__":
    main()
