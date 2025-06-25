#Llamar a pygame
import pygame

#Llamar a random 
import random
#Llamar a sys para cerrar funciones sistema
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla 
ancho = 400
alto = 400


pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Serpientuki por David Proaño")
clock = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 80)
ROJO = (255, 0, 0)

# Coordenadas iniciales donde incia
serpiente = [(100, 100)]  
direccion = (10, 0)  

# generar comida aleatoria
Comida = (random.randrange(0, 400, 10), random.randrange(0, 400, 10))

#puntajes marcadores
def gscore(puntaje):
    with open("marcadores.txt", "a") as archivo:
        archivo.write(str(puntaje) + "\n")

score = 0
# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP: direccion = (0, -10)
            if evento.key == pygame.K_DOWN: direccion = (0, 10)
            if evento.key == pygame.K_LEFT: direccion = (-10, 0)
            if evento.key == pygame.K_RIGHT: direccion = (10, 0)

 #movimiento de la serpiente 
 
    cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])
    serpiente = [cabeza] + serpiente[:-1]

    #choque contra muros
    if (cabeza[0] < 0 or cabeza[0] >= ancho or
        cabeza[1] < 0 or cabeza[1] >= alto):
        gscore(score)
        print("¡Perdiste!")
        print("Tu puntaje fue:", score)
        pygame.quit()
        sys.exit()

 # la serpiente comio la comida
    if serpiente[0] == Comida:
        Comida = (random.randrange(0,400,10), random.randrange(0,400,10))
        serpiente.append(serpiente[-1])
        score += 1


    # Dibujar todo
    pantalla.fill(NEGRO)
    for parte in serpiente:
     pygame.draw.rect(pantalla, VERDE, pygame.Rect(parte[0], parte[1], 10, 10))

    pygame.draw.rect(pantalla, ROJO, pygame.Rect(Comida[0], Comida[1], 10, 10))

    pygame.display.flip()
    clock.tick(10)  # Velocidad de la serpiente
