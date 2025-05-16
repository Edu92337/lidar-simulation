from constantes import *
from uteis import *
import pygame,random,copy

def draw_obstaculos(screen,matriz):
    screen.fill('black')
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if matriz[i][j] == 1:
                pygame.draw.rect(screen,'green',(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE,CELL_SIZE))

def gerar_mapa_aberto(altura, largura, prob_obstaculo=0.1):
    mapa = []
    for i in range(altura):
        linha = []
        for j in range(largura):
            if random.random() < prob_obstaculo:
                linha.append(1) 
            else:
                linha.append(0)  
        mapa.append(linha)

    for _ in range(2):
        novo_mapa = copy.deepcopy(mapa)
        for i in range(altura):
            for j in range(largura):
                if contar_vizinhos(mapa, i, j, altura, largura) > 1:
                    novo_mapa[i][j] = 1
                else:
                    novo_mapa[i][j] = 0
        mapa = novo_mapa  

    return mapa