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

platform1  = platforms.Platform(50, 400, 200, 50)
platformsList = []
platformsList.append(floor)
platformsList.append(platform1)

# Espacio para las funciones generales
def hit_heroAgainstPlatform(heroHitboxPosX, heroHitboxPosY, heroHitboxWidth, heroHitboxHeight,
                            platformPosX, platformPosY, plaformWidth, plaformHeight):
    #print(f"pos Y + altura: {heroHitboxPosY + heroHitboxHeight}")
    #print(f"altura hitbox: {heroHitboxHeight}")
    #print(f"suma: {heroHitboxPosY + heroHitboxHeight}")
    #print(f"posicion plataforma Y: {platformPosY + 3}")
    #print(heroHitboxPosX + heroHitboxWidth)
    if heroHitboxPosX + heroHitboxWidth >= platformPosX and heroHitboxPosX <= platformPosX + plaformWidth:
        hitX =  True
    else:
        hitX = False
    if heroHitboxPosY + heroHitboxHeight >= platformPosY and not heroHitboxPosY + heroHitboxHeight >= platformPosY + 5:
        hitY =  True
    else:
        hitY =  False
    print(hitX and hitY)
    if hitX and hitY:
        #print("hit")
        hero.startJumpLevel = platformPosY - heroHitboxHeight
        return True
    else:
        return False


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
    pygame.draw.rect(screen, (255, 0, 0, 125), hero.moveHitbox(), 2)
    screen.blit(hero.getAccion(hero.pos.x), hero.pos)


    # revisamos por colisiones entre hitbos del personaje y palataformas
    heroAgainsPlatform1 = hit_heroAgainstPlatform(hero.getHitbox_x(), hero.getHitbox_y(), hero.getHitbox_width(), hero.getHitbox_height(),
                            floor.getHitbox_x(), floor.getHitbox_y(), floor.getHitbox_width(), floor.getHitbox_height())
    heroAgainsPlatform2 = hit_heroAgainstPlatform(hero.getHitbox_x(), hero.getHitbox_y(), hero.getHitbox_width(), hero.getHitbox_height(),
                        platform1.getHitbox_x(), platform1.getHitbox_y(), platform1.getHitbox_width(), platform1.getHitbox_height())
    
    if heroAgainsPlatform1 or heroAgainsPlatform2:
        heroAgainsPlatform = True
    else:
        heroAgainsPlatform = False

    # actualizamos la posicion del personaje en pantalla
    hero.pos = hero.move(hero.pos.x, hero.pos.y, ACC, FRIC, heroAgainsPlatform)
    
    # dibujamos las plataformas
    pygame.draw.rect(bg_scaled, floor.color, floor.drawPlatform(), 2)
    pygame.draw.rect(bg_scaled, platform1.color, platform1.drawPlatform(), 2)
    
    
    # flip() el display para poner el trabajo en pantalla
    pygame.display.flip()
    #print(hero.pos.y)w

    #clock.tick(60) #limita FPS a 60
    # dt es el tiempo delta en segundo desde el ultimo frame...
    # usado para la fisica independiente del framerate
    dt = clock.tick(60) / 1000

pygame.quit()