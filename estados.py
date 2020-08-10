#!/usr/bin/env python
# -*- coding: utf-8 -*-

#modulos importados
import pygame
import sys
from pygame.locals import *

class status():

    def __init__(self):
        self.vida = {}
        self.dano_min = {}
        self.dano_max = {}
        self.nombre = {}
        self.defensa= {}
        self.vida_max = {}
        self.vivo = {}
        self.id = {}
        self.nombre_item = {}
        self.puntos_objeto = {}
        self.inventario_pj = {}
        self.equipo_pj = {}
        self.nivel = {0:1,1:1,2:1,3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:4,11:4,12:4,13:5}
        self.exp = {}
        
    
    def iniciar_status(self):
        salir = True
        i = 0
        if salir == True:
            inventario = open('Inventario.txt','r')
            for linea in inventario.readlines():
                self.iniciar_inventario(i, linea)
                i += 1
            self.iniciar_inventario_pj()
            i = 0
            archivo = open('Estados.txt','r')
            for linea in archivo.readlines():
                self.iniciar_pj(i, linea)
                i += 1
            salir = False
            archivo.close()
            inventario.close()

    def iniciar_inventario_pj(self):
        self.inventario_pj[0] = {0:10, 1:10, 2:10}
        self.inventario_pj[1] = {0:10, 1:10, 2:10}
        self.inventario_pj[2] = {0:10, 1:10, 2:10}
        self.inventario_pj[3] = {0:10, 1:10, 2:10}
        self.inventario_pj[4] = {0:10, 1:10, 2:10}
        self.equipo_pj[0] = {0: 1, 1: 6, 2:0}
        self.equipo_pj[1] = {0: 1, 1: 6, 2:0}
        self.equipo_pj[2] = {0: 1, 1: 6, 2:0}
        self.equipo_pj[3] = {0: 1, 1: 6, 2:0}
        self.equipo_pj[4] = {0: 1, 1: 6, 2:0}
    
    def iniciar_pj(self, op, linea):
        self.vida[op] = int(linea.split(",")[1])
        self.nombre[op] = linea.split(",")[0]
        self.dano_min[op] = int(linea.split(",")[2])
        self.dano_max[op] = int(linea.split(",")[3])
        self.defensa[op] = int(linea.split(",")[4]) 
        self.vida_max[op] = self.vida[op]
        self.vivo[op] = 1
        self.exp[op] = 0

    def iniciar_inventario(self, op, linea):
        self.id[op] = int(linea.split(",")[0])
        self.nombre_item[op] = linea.split(",")[1]                              
        self.puntos_objeto[op] = int(linea.split(",")[2])
        
