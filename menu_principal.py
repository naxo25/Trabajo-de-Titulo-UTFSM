#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as game
import sys
import variables as v
from main import *
from sprites import *
from pygame.locals import *

class menu_principal():
    def __init__(self):
        #init es un constructor que inicializa las variables que se usan dentro de la clase
        self.op = 1
        self.mantener = False
        self.salir = False
        self.pantalla = game.display.set_mode((990,650))
        #self.llamas = Sprite_fuego(329,234)
        self.sprites_menu = { 0: Sprite_fuego(363,252), 1: menu_sprite(0,0)}
        self.i = 0
        self.i2 = 0

    def cargar_menu_principal(self):
        pygame.display.set_caption(v.titulo)
        #pygame.display.set_icon(v.icono_game)
        game.mixer.music.load("musica/Elektronomia - Energy [NCS Release].mp3")
        #game.mixer.music.load("musica/Elektronomia - Energy [NCS Release].mp3")
        game.mixer.music.play(0)
        reloj = pygame.time.Clock()
        while 0 < 1:
            for event in game.event.get():
		    if  event.type == game.QUIT:
			    sys.exit(0)
            self.verificar_opcion(1)
            self.mover_menu()
            self.mover_fuego()
            self.actualizar_imagen(1)
            game.display.update()
            reloj.tick(10)


    def verificar_opcion(self, cargar):
            k = game.key.get_pressed()

            opc_max = 4
                
            if self.mantener == False:
                if self.op > 1 and k[K_UP]:
                    self.op -= 3
                elif self.op < opc_max and k[K_DOWN]:
                    self.op += 3
                elif k[K_RETURN]:
                    self.enter(cargar)

            #al mantener presionada una tecla cambiara el valor de mantener de false a true
            self.mantener = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def enter(self, cargar):
        if cargar == 1:
            if self.op == 1:
                main = juego()
                main.loop_juego()
            elif self.op == 4:
                sys.exit(0)
        
    def actualizar_imagen(self, cargar):
        if cargar == 1:
            if self.op == 1:
                imagen = game.image.load("image/menus/menuP1.png")
            if self.op == 4:
                imagen = game.image.load("image/menus/menuP2.png")
        self.pantalla.blit(imagen,(345,360))

    def mover_fuego(self):
        self.sprites_menu[0].handle_event(self.i)
        self.pantalla.blit(self.sprites_menu[0].parte,self.sprites_menu[0].rect)
        self.i += 1
        if self.i == 26:
            self.i = 0

    def mover_menu(self):
        self.sprites_menu[1].handle_event(self.i2)
        self.pantalla.blit(self.sprites_menu[1].parte,self.sprites_menu[1].rect)
        self.i2 += 1
        if self.i2 == 3:
            self.i2 = 0


        
