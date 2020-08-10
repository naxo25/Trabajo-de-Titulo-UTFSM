#!/usr/bin/env python
# -*- coding: utf-8 -*-

#modulos importados
import pygame
import sys
import variables as v
import perfil
import eventos
import game_over
from menu_juego import *
from pygame.locals import *
from random import randint

#se hace un loop infinito, esto es el alma del juego
#se ejecuta hasta que se cumpla una condicion de cierre

class juego():

        def __init__(self):

                self.menu = menu_juego()
                self.muertos = 0

        def loop_juego(self):

                pantalla = pygame.display.set_mode((1000,650))
                pygame.display.set_caption(v.titulo)
                reloj = pygame.time.Clock()
                
                fondo = pygame.image.load("image/mapa.png")

                pantalla.blit(fondo,(0,0))

                fuente = pygame.font.Font(None, 20)                
                
                while True:
                        self.tiempo = game.time.get_ticks()/800
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        sys.exit(0)
                                        
                                                
                        pantalla.blit(fondo,(0,0))
                        
                        muertos = 0
                        
                        for i in self.menu.player:
                                if not perfil.validar_vida(i):                                                
                                        pantalla.blit(self.menu.player[i].parte,self.menu.player[i].rect)
                                else:
                                        muertos += 1
                        for i in self.menu.enemigo:
                                if not perfil.validar_vida(i + 5):
                                        pantalla.blit(self.menu.enemigo[i].parte,self.menu.enemigo[i].rect)

                        if muertos == 5:
                                game_over.fin()
                                sys.exit(0)
                        
                        if self.menu.pj_enemigo <> -1:
                                if not (perfil.validar_vida(self.menu.pj_enemigo + 5)):                                     
                                        if self.menu.pj_enemigo + 5 == 13:                
                                                if perfil.estado.vida[13] - 5 < perfil.estado.vida_max[13]:
                                                        perfil.estado.vida[13] += 5
                                                if perfil.estado.vida[13] > perfil.estado.vida_max[13]:
                                                        perfil.estado.vida[13] = perfil.estado.vida_max[13]
                                        """elif self.menu.pj_enemigo + 5 < 13: 
                                                if perfil.estado.vida[self.menu.pj_enemigo + 5] - 2 < perfil.estado.vida_max[self.menu.pj_enemigo + 5]:
                                                        perfil.estado.vida[self.menu.pj_enemigo + 5] += 2
                                                if perfil.estado.vida[self.menu.pj_enemigo + 5] > perfil.estado.vida_max[self.menu.pj_enemigo + 5]:
                                                        perfil.estado.vida[self.menu.pj_enemigo + 5] = perfil.estado.vida_max[self.menu.pj_enemigo + 5]"""
                                        self.menu.pausa()
                                        self.menu.zona_enemigo()
                                        self.menu.pj_enemigo += 1   
                                else:
                                        self.menu.pj_enemigo += 1

                                        
                        if self.menu.pj_selec == 5:
                                        self.menu.pj_enemigo = 0
                                        self.menu.pj_selec = 0
                                        for i in range(0,5):
                                                if not perfil.validar_vida(i): 
                                                        if perfil.estado.vida[i] - 4 < perfil.estado.vida_max[i]:
                                                                perfil.estado.vida[i] += 0
                                                        if perfil.estado.vida[i] > perfil.estado.vida_max[i]:
                                                                perfil.estado.vida[i] = perfil.estado.vida_max[i]

                        if self.menu.pj_enemigo == 9:
                                        self.menu.pj_selec = 0
                                        self.menu.pj_enemigo = -1
                                        self.menu.salir = True


                        
                        if perfil.validar_vida(self.menu.pj_selec):
                                self.menu.pj_selec += 1
                                if perfil.muerto(self.menu.pj_selec) == 1:
                                        self.muertos += 1
                                
                        else:
                                        if self.menu.pj_enemigo == -1:
                                                self.menu.zona_libre(pantalla)
                                        pygame.display.flip()


                        reloj.tick(15)
