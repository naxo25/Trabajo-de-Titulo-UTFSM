#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from estados import *
from random import randint
from pygame.locals import *

#una de las variables mas importantes, instancia el objeto en cual se guardan los estados de los personajes

estado = status()

estado.iniciar_status()


def objeto():
    return estado
    
def cambiar_perfil(pj_selec):
    if pj_selec == 0:
        imagen = pygame.image.load("perfiles/annie_perfil.png")
    elif pj_selec == 1:
        imagen = pygame.image.load("perfiles/zero_perfil.png")
    elif pj_selec == 3:
        imagen = pygame.image.load("perfiles/megaman_perfil.png")
    elif pj_selec == 4:
        imagen = pygame.image.load("perfiles/mikasa_perfil.png")
    elif pj_selec == 2:
        imagen = pygame.image.load("perfiles/hisoka_perfil.png")
    elif pj_selec < 8:
        imagen = pygame.image.load("perfiles/orco_perfil.png")
    elif pj_selec < 10:
        imagen = pygame.image.load("perfiles/sonic_perfil.png")
    elif pj_selec < 13:
        imagen = pygame.image.load("perfiles/cruzado_perfil.png")
    elif pj_selec == 13:
        imagen = pygame.image.load("perfiles/angevo_perfil.png")
    return imagen

def actualizar_vida(op):
    vida = estado.vida[op]
    return vida

def validar_vida(op):
    i = False
    if estado.vida[op] <= 0:
        i = True
    return i

def muerto(op):
    i = 0
    if estado.vivo[op] == 1:
            estado.vivo[op] = 0
            i = 1
    return i

def pintar_vida(op):

    return (0,0,0)
        
