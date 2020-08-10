# -*- coding: utf-8 -*-
#modulos importados
import pygame
from pygame.locals import *


def fin():

        salir = True
        fondo = pygame.image.load("image/game_over.png")
        pantalla = pygame.display.set_mode((1000,650))
        pantalla.blit(fondo,(0,0))
        tiempo = pygame.time.get_ticks()/250    
        while salir == True:
                actual = pygame.time.get_ticks()/250
                if actual - tiempo == 10:
                    salir = False
                
                pantalla.blit(fondo,(0,0))
                pygame.display.flip()
                
