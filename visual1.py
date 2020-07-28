import pygame
from pygame.locals import *
import sys

#variáveis que definem um jogo novo/limpo
board = ["-"]*9
current_player = "X"
game_still_going = True
white = (255,255,255)
cor_da_casa = [white] * 9
#variáveis de cunho geral
green = (0, 255, 0)
red = (255, 0, 0)
casas = [(20,20,140,140), (180,20,140,140), (340,20,140,140), (20,180,140,140), (180,180,140,140),
         (340,180,140,140), (20,340,140,140), (180,340,140,140), (340,340,140,140)]

def nome_da_cor(player):
    if current_player == "X":
        return "Vermelho"
    elif current_player == "O":
        return "Verde"

def marcar_casa():
    global pick
    if game_still_going:
        if pos[0] in range(20, 160) and pos[1] in range(20, 160):
            pick = 0
        elif pos[0] in range(180, 320) and pos[1] in range(20, 160):
            pick = 1
        elif pos[0] in range(340, 480) and pos[1] in range(20, 160):
            pick = 2
        elif pos[0] in range(20, 160) and pos[1] in range(180, 320):
            pick = 3
        elif pos[0] in range(180, 320) and pos[1] in range(180, 320):
            pick = 4
        elif pos[0] in range(340, 480) and pos[1] in range(180, 320):
            pick = 5
        elif pos[0] in range(20, 160) and pos[1] in range(340, 480):
            pick = 6
        elif pos[0] in range(180, 320) and pos[1] in range(340, 480):
            pick = 7
        elif pos[0] in range(340, 480) and pos[1] in range(340, 480):
            pick = 8
        else:
            print()
        if board[pick] == "-":
            board[pick] = current_player
            cor_da_casa[pick] = cor_do_player
            flip_player()
            print("É a vez do jogador ", nome_da_cor(current_player), "!")
        else:
            print("Seleção invalida! Clique em uma das casas ainda disponíveis!")
    else:
        print("O jogo já acabou! Aperte N para reiniciar")

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    global game_still_going
    # rows
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        game_still_going = False
    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
        game_still_going = False
    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
        game_still_going = False
    # columns
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        game_still_going = False
    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
        game_still_going = False
    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
        game_still_going = False
    # diagonals
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        game_still_going = False
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        game_still_going = False
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()
print(nome_da_cor(current_player), " inicia o jogo")

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for n in range(9):
            pygame.draw.rect(screen, cor_da_casa[n], casas[n])
        if current_player == "X":
            cor_do_player = red
        else:
            cor_do_player = green
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            marcar_casa()
            check_if_game_over()
            if game_still_going == False:
                if winner == None:
                    print("O jogo acabou empatado")
                else:
                    # aqui era pra usar a função nome_da_cor, mas o resultado tá vindo trocado
                    if winner == "X":
                        print("O jogador Vermelho venceu!")
                    elif winner == "O":
                        print("O jogador Verde venceu!")
        if event.type == KEYDOWN:
            if event.key == K_n:
                pick = None
                winner = None
                winner_color = None
                board = ["-"] * 9
                current_player = "X"
                game_still_going = True
                cor_da_casa = [white] * 9
                cor_do_player = None
                print("Novo jogo! ", current_player, "'s turn")

    pygame.display.update()