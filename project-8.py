# JUEGO NAVES ESPACIALES

import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasion espacial")
icon = pygame.image.load('nave-espacial.png')
pygame.display.set_icon(icon)
fondo = pygame.image.load('fondo.png')

jugador_imagen = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500
jugador_cambio_x = 0

enemigo_imagen = []
enemigo_x = []
enemigo_y = []
enemigo_cambio_x = []
enemigo_cambio_y = []
cantidad_enemigos = 8

mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

for e in range(cantidad_enemigos):
    enemigo_imagen.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_cambio_x.append(0.5)
    enemigo_cambio_y.append(50)

bala_imagen = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_cambio_y = 3
bala_visible = False

puntaje = 0
texto_x = 10
texto_y = 10
fuente = pygame.font.Font('freesansbold.ttf', 32)

def texto_final():
    fuente_final = fuente.render('JUEGO TERMINADO', True, (255, 255, 255))
    screen.blit(fuente_final, (60, 200))

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    screen.blit(texto, (x, y))

def jugador(x, y):  
    screen.blit(jugador_imagen, (x, y))

def enemigo(x, y, e):
    screen.blit(enemigo_imagen[e], (x, y))

def disparar(x, y):
    global bala_visible
    bala_visible = True
    screen.blit(bala_imagen, (x + 16, y + 10))

def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False

running = True
while running:

    screen.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_cambio_x = -0.5
            if event.key == pygame.K_RIGHT:
                jugador_cambio_x = 0.5
            if event.key == pygame.K_SPACE:
                if not bala_visible:
                    mixer.Sound('disparo.mp3').play()
                    bala_x = jugador_x
                    disparar(bala_x, bala_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_cambio_x = 0
    
    jugador_x += jugador_cambio_x

    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    for e in range(cantidad_enemigos):

        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_cambio_x[e]

        if enemigo_x[e] <= 0:
            enemigo_cambio_x[e] = 0.5
            enemigo_y[e] += enemigo_cambio_y[e]
        elif enemigo_x[e] >= 736:
            enemigo_cambio_x[e] = -0.5
            enemigo_y[e] += enemigo_cambio_y[e]

        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        
        if colision:
            mixer.Sound('Golpe.mp3').play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)
        

    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar(bala_x, bala_y)
        bala_y -= bala_cambio_y

    mostrar_puntaje(texto_x, texto_y)        

    jugador(jugador_x, jugador_y)

    pygame.display.update()