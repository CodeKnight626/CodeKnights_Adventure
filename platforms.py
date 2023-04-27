import pygame
from pygame.locals import *
import sys
vec = pygame.math.Vector2


class Platform():
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.color = pygame.Color(0, 0, 255, 255)
        self.platformShape = pygame.Rect(self.left, self.top, self.width, self.height)

    def createPlataform(self):
        pass

    def drawPlatform(self):
        self.platformShape = pygame.Rect(self.left, self.top, self.width, self.height)
        return self.platformShape
    
    def getHitbox_x(self):
        #regresa la coordenada en X de la posicion donde inciia el hitbox
        return self.platformShape.topleft[0]
    
    def getHitbox_y(self):
        #regresa la coordenada en Y de la posicion donde inciia el hitbox
        return self.platformShape.topleft[1]
    
    def getHitbox_width(self):
        #regresa el ancho del hitbox
        return self.platformShape.width
    
    def getHitbox_height(self):
        #regresa el alto del hitbox
        return self.platformShape.height