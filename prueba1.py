import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load images

# variable para la posicion del jugador
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last game
    screen.fill("black")

    # RENDER YOUR GAME HERE
    #screen.blit(rocket, (player_pos.x, player_pos.y))
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1000 * dt
    if keys[pygame.K_s]:
        player_pos.y += 1000 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 1000 * dt
    if keys[pygame.K_d]:
        player_pos.x += 1000 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    #clock.tick(60) #limit FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()