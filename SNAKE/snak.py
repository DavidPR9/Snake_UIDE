#variables

import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla 
ancho = 600
alto = 400
tamano_celda = 10

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Serpientuki por David Proaño")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 80)
ROJO = (255, 0, 0)

# Reloj para controlar la velocidad
reloj = pygame.time.Clock()

# Función para generar comida aleatoria
def generar_comida():
    x = random.randint(0, 30) * tamano_celda
    y = random.randint(0, 35) * tamano_celda
    return [x, y]

# Coordenadas iniciales donde incia
serpiente = [[100, 100]]  
direccion = [10, 0]  
comida = generar_comida()
score = 0

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != [0, tamano_celda]:
                direccion = [0, -tamano_celda]
            elif evento.key == pygame.K_DOWN and direccion != [0, -tamano_celda]:
                direccion = [0, tamano_celda]
            elif evento.key == pygame.K_LEFT and direccion != [tamano_celda, 0]:
                direccion = [-tamano_celda, 0]
            elif evento.key == pygame.K_RIGHT and direccion != [-tamano_celda, 0]:
                direccion = [tamano_celda, 0]

    # Mover la serpiente
    nueva_cabeza = [serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1]]
    serpiente.insert(0, nueva_cabeza)

    # Verificar si comió la comida
    if nueva_cabeza == comida:
        comida = generar_comida()
        score += 1
    else:
        serpiente.pop()  # Quitar la cola si no comió

    # Verificar colisiones (pared o cuerpo)
    if (
        nueva_cabeza in serpiente[1:] or
        nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ancho or
        nueva_cabeza[1] < 0 or nueva_cabeza[1] >= alto
    ):
        print(f"Game Over! Puntuación: {score}")
        pygame.quit()
        sys.exit()

    # Dibujar todo
    pantalla.fill(NEGRO)
    for parte in serpiente:
        pygame.draw.rect(pantalla, VERDE, pygame.Rect(parte[0], parte[1], tamano_celda, tamano_celda))

    pygame.draw.rect(pantalla, ROJO, pygame.Rect(comida[0], comida[1], tamano_celda, tamano_celda))

    pygame.display.flip()
    reloj.tick(10)  # Velocidad de la serpiente
