from constantes import *
from uteis import *
from mapa import *
import math

class LIDAR():
    def __init__(self,mapa):
        vazios =[]
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                if mapa[i][j] == 0 :
                    vazios.append((j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
        self.posicao = list(random.choice(vazios))
        self.velocidade = [0,0]
        self.aceleracao = [0,0]
        self.direcao = 0
        self.distancias_lidas = []
    
    def draw(self, screen, mapa):
        self.distancias_lidas.clear()
        x0 = int(self.posicao[0])  
        y0 = int(self.posicao[1])  
        pygame.draw.circle(screen, 'yellow', (x0, y0), CELL_SIZE // 2)

        delta = 120 / 9
        angulo_inicial = self.direcao - 60  
        for i in range(10):
            comprimento = 1  
            angulo = angulo_inicial + i * delta
            angulo_rad = math.radians(angulo)
            while True:
                xf = x0 + int(comprimento * math.cos(angulo_rad))
                yf = y0 + int(comprimento * math.sin(angulo_rad))
                grid_x = yf // CELL_SIZE
                grid_y = xf // CELL_SIZE
                if xf < 0 or xf >= WIDTH or yf < 0 or yf >= HEIGHT:
                    break
                elif dentro_dos_limites(grid_x, grid_y) and mapa[grid_x][grid_y] == 1:
                    break
                comprimento += 1
            self.distancias_lidas.append([math.dist((x0, y0), (xf, yf)),angulo])
            pygame.draw.line(screen, 'blue', (x0, y0), (xf, yf), 1)

    def move(self,mapa):
        comp = -1
        ang = -1
        for dist,angulo in self.distancias_lidas:
            if dist> comp:
                comp = dist
                ang = angulo
        if comp <= 20:
            self.direcao = (self.direcao + 180) % 360
            return
        self.direcao = ang

        ax = math.cos(math.radians(self.direcao))*0.2
        ay = math.sin(math.radians(self.direcao))*0.2

        self.velocidade[0] += ax
        self.velocidade[1] += ay
        self.velocidade[0] *= 0.9
        self.velocidade[1] *= 0.9

        nova_pos = [
            self.posicao[0] + self.velocidade[0],
            self.posicao[1] + self.velocidade[1]
        ]
        grid_x = int(nova_pos[0] // CELL_SIZE)
        grid_y = int(nova_pos[1] // CELL_SIZE)
        if dentro_dos_limites(grid_y, grid_x) and mapa[grid_y][grid_x] == 0:
            self.posicao = nova_pos

