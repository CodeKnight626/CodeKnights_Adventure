import pygame
import sys

# cargamos los datos de los personajes principales
import heroes

# cargamos los datos par alas plataformas
import platforms

# Configuracion inicial pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Cargamos el fondo de pantalla
bg = pygame.image.load('sprites\stages\stage1.jpg')
bg_scaled = pygame.transform.scale_by(bg, (1.7, 1.5))

# creamos una instancia de la clase heroes para el protagonista
hero = heroes.Heroes(heroes.ninja)
# cargamos las imagenes de los sprites de movimiento y las escalamos al doble

# variable para la posicion del jugador y pone el sprite enmedio de la pantalla
hero.pos = pygame.Vector2(hero.pos)

# variables para la fisca, saltos, gravedad
ACC = 0.5 # aceleracion general para todos los personajes
FRIC = -0.12 # friccion general para todos los personajes

# Plataformas
floor = platforms.Platform(0, 627, 1280, 50)

# Espacio para las funciones generales
def hit():
    return


while running:
    # rutina para eventos
    # el evento pygame.QUIT significa que el usuario presiono la X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pinta la pantalla de un solo color
    #screen.fill("blue")
    # cargamos la imagen de fondo
    screen.blit(bg_scaled, (0,0))
    #screen.fill("black")


    #Cargamos el diseño del protagonista
    pygame.draw.rect(bg_scaled, (255, 0, 0, 255), hero.moveHitbox(),  2)
    #pygame.draw.rect(bg_scaled, (255, 0, 0, 255), pygame.Rect(0, 0, 500, 60), 2)
    screen.blit(hero.getAccion(hero.pos.x), hero.pos)
    # actualizamos la posicion del personaje en pantalla
    hero.pos = hero.move(hero.pos.x, hero.pos.y, ACC, FRIC)

    # dibujamos las plataformas
    pygame.draw.rect(bg_scaled, floor.color, floor.drawPlatform(), 2)
    
    
    # flip() el display para poner el trabajo en pantalla
    pygame.display.flip()
    #print(hero.pos.y)w

    #clock.tick(60) #limita FPS a 60
    # dt es el tiempo delta en segundo desde el ultimo frame...
    # usado para la fisica independiente del framerate
    dt = clock.tick(60) / 1000

pygame.quit()