#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    fuente = pygame.font.Font(None, 40)
    pantalla = pygame.display.set_mode((1000,650))
    while True:
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                    sys.exit(0)
            y,x = 0,0
            while x < 990:
                mensaje = fuente.render("X",0,(255,255,255))
                pantalla.blit(mensaje,(x,y))
                y = 0
                while y < 630:
                    pantalla.blit(mensaje,(x,y))
                    y += 30
                x += 30
            
            asd()        
            pygame.display.flip()
    sys.exit(0)

def asd():
    if 
