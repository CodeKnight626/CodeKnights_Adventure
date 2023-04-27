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
        self.jumpReleased = False
        self.jumpCounter = 0
        self.startJumpLevel = 503

        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, 120, 120)

        self.lastState = 0
        self.currentState = 0

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

        self.imageSize_width = self.heroStandImg.get_width()
        self.imageSize_height = self.heroStandImg.get_height()

        # constantes para el personaje
        self.MAX_JUMP = 500


    def loadAndScaleImage(self, path, scale=(2, 2)):
        return pygame.transform.scale_by(pygame.image.load(path), scale)

    def getImg(self):
        return self.standSprite

    # Revisa si el personaje llego al maximo de su salto
    # si es verdadero, modifica la variable maxJumpReached
    def IsmaxJumpReached(self, valueHeight):
        maxJumpValue = self.startJumpLevel - self.MAX_JUMP
        if valueHeight < maxJumpValue:
            self.maxJumpReached = True
            #self.isJumping = False

    def move(self, valueX, valueY, ACC, FRIC, heroAgainsPlatform):
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
            # al salto maximo puede saltar
            if self.jumpCounter == 0:
                heroAgainsPlatform = False
                self.startJumpLevel = self.pos.y + self.imageSize_height
                #print(self.startJumpLevel)
                self.jumpCounter = 1 
            if self.jumpCounter == 2:
                self.jumpCounter = 3
            if self.pos.y >= self.startJumpLevel - self.MAX_JUMP and not self.maxJumpReached and not self.jumpReleased:
                self.vel.y = -15
        # Si no presionamos la tecla W liberamos el salto
        else:
            if self.jumpCounter == 1:
                self.jumpCounter = 2
            if self.jumpCounter == 3:
                self.jumpReleased = True
        

        #print(self.vel.y)
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        self.acc.y += self.vel.y * FRIC
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        
        
        # Evita que el personaje se salga de la pantalla visible en el eje de las x
        if self.pos.x > 1280:
            self.pos.x = 1280
        if self.pos.x < 0:
            self.pos.x = 0

        # Evita que el personaje se salga de la pantalla visble en el eje de las y...
        if heroAgainsPlatform:
            self.pos.y = self.startJumpLevel
            self.maxJumpReached = False
            self.jumpReleased = False
            self.jumpCounter = 0
            self.vel.y = 0

        # Si el personaje toca el hitbox de alguna plataforma reseta las condiciones de salto
        #if heroAgainsPlatform:
        #    #self.pos.y = self.startJumpLevel
        #    self.maxJumpReached = False
        #    self.jumpReleased = False
        #    self.jumpCounter = 0
        #    self.vel.y = 0
        

        self.moveHitbox()
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

    def moveHitbox(self):
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, self.imageSize_width, self.imageSize_height)
        return self.hitbox
    
    def getHitbox_x(self):
        #regresa la coordenada en X de la posicion donde inciia el hitbox
        return self.hitbox.topleft[0]
    
    def getHitbox_y(self):
        #regresa la coordenada en Y de la posicion donde inciia el hitbox
        return self.hitbox.topleft[1]
    
    def getHitbox_width(self):
        #regresa el ancho del hitbox
        return self.hitbox.width
    
    def getHitbox_height(self):
        #regresa el alto del hitbox
        return self.hitbox.height

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
