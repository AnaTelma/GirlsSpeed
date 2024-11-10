
import sys
import pygame
from pygame import mixer

# Inicializa o Pygame e o mixer
pygame.init()
mixer.init()

# Configuração da tela
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Jogo de Arrancada - Girls Speed")

# Carregando o som dos carros
mixer.music.load('asset_car/motor.mp3')
mixer.music.play()

# Carregando as imagens
track = pygame.image.load("asset_car/track.png")
car1 = pygame.image.load("asset_car/car1_barbie.png")
car2 = pygame.image.load("asset_car/car2_penelope.png")
t_girls = pygame.image.load("asset_car/girls_speed.png")

# Carregando os botões
b_play = pygame.image.load("button/play.png")
b_exit = pygame.image.load("button/exit.png")

# Posições iniciais
track_x = 0
track_y = 0
car1_x = 5
car1_y = 135
car2_x = 5
car2_y = 355
b_play_x = 1005
b_play_y = 5
b_exit_x = 1150
b_exit_y = 5
t_girls_x = 500
t_girls_y = -2

# Velocidades iniciais
car1_speed = 0
car2_speed = 0

# Variáveis de controle do jogo
game_started = False  # Para iniciar o jogo quando "Play" for clicado
game_exit = False  # Para sair do jogo ao clicar em "Exit"
winner = None  # Armazena o vencedor quando há uma vitória

# Fonte para exibir o texto do vencedor
font = pygame.font.Font(None, 100)

# Relógio para controlar a taxa de frames
clock = pygame.time.Clock()

# Função principal do jogo
def game_loop():
    global car1_x, car1_y, car2_x, car2_y, car1_speed, car2_speed
    global b_play_x, b_play_y, b_exit_x, b_exit_y, game_started, game_exit, winner

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Verifica se o botão foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if b_exit_x < mouse_x < b_exit_x + 65 and b_exit_y < mouse_y < b_exit_y + 65:
                    game_exit = True
                elif b_play_x < mouse_x < b_play_x + 65 and b_play_y < mouse_y < b_play_y + 65:
                    game_started = True  # Inicia o jogo ao clicar no botão "Play"
                    winner = None  # Reinicia o vencedor

            # Controles dos carros
            if event.type == pygame.KEYDOWN and game_started:
                if event.key == pygame.K_w:
                    car1_speed = 20
                if event.key == pygame.K_UP:
                    car2_speed = 20

            if event.type == pygame.KEYUP and game_started:
                if event.key == pygame.K_w:
                    car1_speed = 0
                if event.key == pygame.K_UP:
                    car2_speed = 0

        # Atualiza a posição dos carros apenas se o jogo tiver começado e não houver vencedor
        if game_started and winner is None:
            car1_x += car1_speed
            car2_x += car2_speed

            # Checa se algum carro venceu
            if car1_x > screen_width - 250:
                winner = "Barbie venceu!"
                game_started = False  # Pausa o jogo

            if car2_x > screen_width - 250:
                winner = "Penélope venceu!"
                game_started = False  # Pausa o jogo

        # Desenhando as imagens na tela
        screen.blit(track, (track_x, track_y))
        screen.blit(car1, (car1_x, car1_y))
        screen.blit(car2, (car2_x, car2_y))
        screen.blit(b_play, (b_play_x, b_play_y))
        screen.blit(b_exit, (b_exit_x, b_exit_y))
        screen.blit(t_girls, (t_girls_x, t_girls_y))

        # Exibe o vencedor
        if winner:
            text = font.render(winner, True, (0, 0, 0))  # Texto em black
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

        # Atualizando a tela
        pygame.display.update()

        # Controlando a taxa de frames
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Iniciando o loop do jogo
game_loop()
