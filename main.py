from constantes import *
from uteis import *
from mapa import *
from lidar import *

def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    clock = pygame.time.Clock()
    pygame.display.set_caption("LIDAR SENSOR")
    mapa = gerar_mapa_aberto(GRID_HEIGHT,GRID_WIDTH)
    lidar = LIDAR(mapa)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        draw_obstaculos(screen,mapa)
        lidar.draw(screen,mapa)
        lidar.move(mapa)
        pygame.display.flip()
        clock.tick(10)
    


if __name__ == '__main__':
    main()