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

    def createPlataform(self):
        pass

    def drawPlatform(self):
        self.platformShape = pygame.Rect(self.left, self.top, self.width, self.height)
        return self.platformShape