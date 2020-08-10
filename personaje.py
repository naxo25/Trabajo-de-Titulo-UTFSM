# -*- coding: utf-8 -*-
#modulos importados
import pygame
from random import randint
from pygame.locals import *
#--------------------------------- CLASES ---------------------------------------------------
class Personaje(pygame.sprite.Sprite):

         
	def __init__(self, x ,y, cod_img):
		#cargo el fotograma con todas las pociones del personaje
                self.imagen = pygame.image.load(cod_img)
		#le paso a la variable parte el tamaño de los rectangulos (32x32)
		self.imagen.set_clip(pygame.Rect(0,0,31,31))
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		#creo el rectangulo a partir de los datos de parte
		self.rect = self.parte.get_rect()
		#achico dicho rectangulo para que se vea como si de verdad
		#se toca el vorde del obj con el que hace colision
		self.rect.inflate_ip(5,5)
		#valor de las posiciones
		self.x = x
		self.y = y
		self.rect.top = y
		self.rect.left = x
		self.velocidad = 7
		#el primer frame de mi fotograma
		self.frame = 0
		#------- cada uno de los cortes del fotograma segun su orientacion -------------- #
		self.pj = { 0: (0, 0, 35, 35) }

        def actualizar(self, xx, yx):
                self.rect.left = xx
                self.rect.top = yx
                self.x = self.rect.left
                self.y = self.rect.top

        def no_actualizar(self):
                self.rect.left = self.x
                self.rect.top = self.y


class Enemigo(Personaje):
         
	def __init__(self, x, y, cod_img):
		Personaje.__init__(self, x, y, cod_img)
		self.velocidad = 4
                self.xe, self.ye = 0,0
                self.pj = randint(0,4)

	def buscar(self, lista, lista_vida):
                while lista_vida.vida[self.pj] <= 0:
                        self.pj = randint(0,4)
                self.xe = lista[self.pj].x
                self.ye = lista[self.pj].y

        def getX(self):
                return self.xe

        def getY(self):
                return self.ye
	
	def handle_event(self, lista, lista_vida):

                self.buscar(lista, lista_vida)
		self.update(lista, lista_vida)			
		

