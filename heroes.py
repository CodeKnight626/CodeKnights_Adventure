# Archivo que va a contener todos los datos e imagenes para el personaje protagonista

# Importamos las librerias necesarias
import pygame
from pygame.locals import *
import sys
vec = pygame.math.Vector2


class Heroes:

    def __init__(self, heroDataDict):
        self.hp = heroDataDict['hp']
        self.atk = heroDataDict['atk']
        self.defs = heroDataDict['defs']
        self.characterSpeed = heroDataDict['speed']
        self.pos = heroDataDict['pos']
        self.standSprite, self.jumpingSprite, self.atkSprite, self.fallSprite, self.running_1Sprite, self.running_2Sprite = heroDataDict['sprites_front']
        self.standSprite_back, self.jumpingSprite_back, self.fallSprite_back, self.running_1Sprite_back, self.running_2Sprite_back = heroDataDict['sprites_back']
        # self.sprites = heroDataDict['sprites']
        self.maxJumpReached = False
        self.jumping = False
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.scale = (2, 2)

        self.heroStandImg = self.loadAndScaleImage(self.standSprite, self.scale)
        self.heroJumpImg = self.loadAndScaleImage(self.jumpingSprite, self.scale)
        self.atkSprite = self.loadAndScaleImage(self.atkSprite, self.scale)
        self.heroFalling = self.loadAndScaleImage(self.fallSprite, self.scale)
        self.heroRunning = self.loadAndScaleImage(self.running_1Sprite, self.scale)
        self.heroRunning2 = self.loadAndScaleImage(self.running_2Sprite, self.scale)

        self.heroStandImg_back = self.loadAndScaleImage(self.standSprite_back, self.scale)
        self.heroJumpImg_back = self.loadAndScaleImage(self.jumpingSprite_back, self.scale)
        self.heroFalling_back = self.loadAndScaleImage(self.fallSprite_back, self.scale)
        self.heroRunning_back = self.loadAndScaleImage(self.running_1Sprite_back, self.scale)
        self.heroRunning2_back = self.loadAndScaleImage(self.running_2Sprite_back, self.scale)

        # constantes para el personaje
        self.GROUND_LEVEL = 503.0
        self.MAX_JUMP = 300

    def loadAndScaleImage(self, path, scale=(2, 2)):
        return pygame.transform.scale_by(pygame.image.load(path), scale)

    def getImg(self):
        return self.standSprite

    # Revisa si el personaje llego al maximo de su salto
    # si es verdadero, modifica la variable maxJumpReached
    def IsmaxJumpReached(self, valueHeight):
        maxJumpValue = self.GROUND_LEVEL - self.MAX_JUMP
        if valueHeight < maxJumpValue:
            self.maxJumpReached = True

    def move(self, valueX, valueY, ACC, FRIC):
        # Tomamos la posicion actual tanto en X como en Y
        self.pos.x = valueX
        self.pos.y = valueY

        # Definimos la aceleracion en Y a 1 para activar la gravedad
        self.acc = vec(0, 1)

        # Revisa si el personaje llego al maximo de su salto
        self.IsmaxJumpReached(self.pos.y)

        # Revisamos si alguna de las teclas fue presionada
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -ACC
        if keys[pygame.K_d]:
            self.acc.x = ACC
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.acc.x = 0
            # borrar despues
            self.vel.x = 0
        if keys[pygame.K_w]:
            # Si el personaje esta al nivel del suelo y no ha llegado...
            # al saltro maximo puede saltar
            if self.pos.y > self.GROUND_LEVEL - self.MAX_JUMP and not self.maxJumpReached:
                self.vel.y = -15

        self.acc += self.vel * FRIC
        self.vel += self.acc
        # borrar esto tambien
        # if(self.vel.x) > 4:
        #    self.vel.x = 8
        self.pos += self.vel + 0.5 * self.acc

        
        # Evita que el personaje se salga de la pantalla visible en el eje de las x
        if self.pos.x > 1280:
            self.pos.x = 1280
        if self.pos.x < 0:
            self.pos.x = 0

        # Evita que el personaje se salga de la pantalla visble en el eje de las y
        if self.pos.y > self.GROUND_LEVEL:
            self.maxJumpReached = False
            self.pos.y = self.GROUND_LEVEL
            self.vel.y = 0

        print(self.vel.y)
        return self.pos

    def getAccion(self, valueX):
        self.pos.x = valueX
        modResultForX = int(self.pos.x) % 2
        if self.vel.x == 0 and self.vel.y == 0:
            return self.heroStandImg
        if self.vel.y < 0 and self.vel.x == 0:
            return self.heroJumpImg
        if self.vel.y > 0 and self.vel.x == 0:
            return self.heroJumpImg_back
        if self.vel.y < 0 and self.vel.x > 0:
            return self.heroJumpImg
        if self.vel.y < 0 and self.vel.x < 0:
            return self.heroJumpImg_back
        if self.vel.y > 0 and self.vel.x > 0:
            return self.heroFalling
        if self.vel.y > 0 and self.vel.x < 0:
            return self.heroFalling_back
        if self.vel.x < 0 and self.vel.y == 0:
            if modResultForX == 0:
                return self.heroRunning_back
            if modResultForX == 1:
                return self.heroRunning2_back
        if self.vel.x > 0 and self.vel.y == 0:
            if modResultForX == 0:
                return self.heroRunning
            if modResultForX == 1:
                return self.heroRunning2
        # estado = self.heroRunning if modResultForX == 0 and self.vel.x else self.heroRunning2
        # return estado


codeKnight = {
    'hp': 10,
    'atk': 10,
    'defs': 10,
    'speed': 0.5,
    'pos': vec(0, 0),
    'sprites': ['sprites\main_characters\cruzader.png', 'sprites\main_characters\cruzader.png', 'sprites\main_characters\cruzader.png']
}

ninja = {
    'hp': 10,
    'atk': 10,
    'defs': 10,
    'speed': 0.5,
    'pos': vec(0, 0),
    'sprites_front': ['sprites\sprites_red_ninja\ck_standing_red_ninja.png',
                      'sprites\sprites_red_ninja\ck_jumping_red_ninja.png',
                      'sprites\main_characters\cruzader.png',
                      'sprites\sprites_red_ninja\ck_falling_red_ninja.png',
                      'sprites\sprites_red_ninja\ck_running_red_ninja_1.png',
                      'sprites\sprites_red_ninja\ck_running_red_ninja_2.png'],

    'sprites_back': ['sprites\sprites_red_ninja\ck_standing_red_ninja_back.png',
                     'sprites\sprites_red_ninja\ck_jumping_red_ninja_back.png',
                     'sprites\sprites_red_ninja\ck_falling_red_ninja_back.png',
                     'sprites\sprites_red_ninja\ck_running_red_ninja_1_back.png',
                     'sprites\sprites_red_ninja\ck_running_red_ninja_2_back.png']
}

rey = {
    'hp': 20,
    'atk': 20,
    'defs': 20,
    'vel': 600,
    'pos': (0, 0),
    'sprites': ['sprites\main_characters\cruzader.png', 'sprites\main_characters\cruzader.png', 'sprites\main_characters\cruzader.png']
}
