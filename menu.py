#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as game
import sys
import main
import variables as v
from sprites import *
from menu_sprite import *
from pygame.locals import *

class menu_principal():
    def __init__(self):
        #init es un constructor que inicializa las variables que se usan dentro de la clase
        self.op = 1
        self.mantener = False
        self.salir = False
        self.pantalla = game.display.set_mode((990,650))
        #self.llamas = Sprite_fuego(329,234)
        self.llamas = Sprite_fuego(377,252)
        self.menu_sprite = menu_sprite(0,0)
        self.i = 0
        self.i2 = 0

    def loop(self):
        pygame.display.set_caption(v.titulo)
        fondo = game.image.load("image/Fondo_MenuP.jpg")
        game.mixer.music.load("musica/Elektronomia - Energy [NCS Release].mp3")
        #game.mixer.music.load("musica/Elektronomia - Energy [NCS Release].mp3")
        game.mixer.music.play(0)
        reloj = pygame.time.Clock()
        while not self.salir:
            for event in game.event.get():
		    if  event.type == game.QUIT:
			    sys.exit(0)
            self.menu()
            self.mover_menu()
            self.mover_fuego()
            self.actualizar()
            game.display.update()
            reloj.tick(10)


    def menu(self):
            k = game.key.get_pressed()

            if self.mantener == False:
                if self.op > 1 and k[K_UP]:
                    self.op -= 1
                elif self.op < 4 and k[K_DOWN]:
                    self.op += 1
                elif k[K_RETURN]:
                    self.opciones()

            #al mantener presionada una tecla cambiara el valor de mantener de false a true
            self.mantener = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def opciones(self):
        if self.op == 1:
            self.salir = True
        elif self.op == 4:
            sys.exit(0)
        
    def actualizar(self):
        if self.op == 1:
                fondo = game.image.load("image/menus/menuP1.png")
        if self.op == 2:
                fondo = game.image.load("image/menus/menuP2.png")
        if self.op == 3:
                fondo = game.image.load("image/menus/menuP3.png")
        if self.op == 4:
                fondo = game.image.load("image/menus/menuP4.png")
        self.pantalla.blit(fondo,(362,360))

    def mover_fuego(self):
        self.llamas.handle_event(self.i)
        self.pantalla.blit(self.llamas.parte,self.llamas.rect)
        self.i += 1
        if self.i == 26:
            self.i = 0

    def mover_menu(self):
        self.menu_sprite.handle_event(self.i2)
        self.pantalla.blit(self.menu_sprite.parte,self.menu_sprite.rect)
        self.i2 += 1
        if self.i2 == 12:
            self.i2 = 0
