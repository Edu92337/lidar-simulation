from constantes import *
def dentro_dos_limites(i, j):
    return 0 <= i < GRID_HEIGHT and 0 <= j < GRID_WIDTH

def contar_vizinhos(mapa, i, j, altura, largura):
    total = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < altura and 0 <= nj < largura:
                total += mapa[ni][nj]
            else:
                total += 1
    return total


