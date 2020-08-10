# -*- coding: utf-8 -*-
#modulos importados
import pygame
from pygame.locals import *

#--------------------------------- CLASES ---------------------------------------------------
class Sprite_fuego(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/llamas_sprite.png")
                self.imagen.set_clip(pygame.Rect(0,0,275,155))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
		self.llamas_gif     = { 0: (0, 40,275,155), 1: (275, 40,275,155), 2: (550, 40,275,155), 3: (825, 40,275,155),
                                        4: (0,195,275,155), 5: (275,195,275,155), 6: (550,195,275,155), 7: (825,195,275,155),
                                        8: (0,350,275,155), 9: (275,350,275,155), 10:(550,350,275,155), 11:(825,350,275,155),
                                        12:(0,505,275,155), 13:(275,505,275,155), 14:(550,505,275,155), 15:(825,505,275,155),
                                        16:(0,660,275,155), 17:(275,660,275,155), 18:(550,660,275,155), 19:(825,660,275,155),
                                        20:(0,815,275,155), 21:(275,815,275,155), 22:(550,815,275,155), 23:(825,815,275,155),
                                        24:(0,970,275,155), 25:(275,970,275,155)
                                        }
                #punto izquierdo arriba (1x,2x) punto derecha abajo (z,y) z - 1x = 3x, y - 2x = 4x
                #osea que la coordenada z - la 1era coordenada dara el numero que corresponde al espacio entre estas coordenadas 
		

                
	#funcion que cambia el corte del fotograma a medida que el personaje se mueve
	#en una direccion
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	#crea la animacion
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	#funcion que se encarga de mover al personaje
	def update(self, direccion, op):
		if direccion == 'atack':
			self.rect.left += 0
                        self.clip(self.llamas_gif[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
	#funcion que detecta los eventos que son del tipo teclado
	def handle_event(self, op):
                        self.update('atack', op)



class menu_sprite(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/gohan.png")
                self.imagen.set_clip(pygame.Rect(0,0,275,155))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
		#self.menu     = { 0: (1000,2260,990,730), 1: (2000, 2260,990,730) }
                self.menu = {0: (0,0,990,730), 1: (1000, 0,990,730), 2: (2000,0,990,730), 3: (0, 750,990,750), 4: (1000,750,990,750),
                             5: (2000,750,990,750), 6: (0,1500,990,750), 7: (1000,1500,990,750), 8: (2000,1500,990,750),
                             9: (0,2250,990,740), 10: (1000,2250,990,740), 11: (2000, 2250,990,740)}

                
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	#crea la animacion
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	#funcion que se encarga de mover al personaje
	def update(self, direccion, op):
		"""if op/2 <> (op/2.0):
                        self.clip(self.menu[0])
                else:"""
                self.clip(self.menu[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
	#funcion que detecta los eventos que son del tipo teclado
	def handle_event(self, op):
                        self.update('atack', op)

class barra_hp(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/sprite_hp.png")
                self.imagen.set_clip(pygame.Rect(0,0,50,50))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
		#self.menu     = { 0: (1000,2260,990,730), 1: (2000, 2260,990,730) }
                self.barra      = { 0: (0, 28,64,14), 1: (64, 28,64,14), 2: (128, 28,64,14), 3: (192, 28,64,14), 4: (256, 28,64,14), 5: (320, 28,64,14),
                                       6: (0, 92,64,14), 7: (64, 92,64,14), 8: (128, 92,64,14), 9: (192, 92,64,14), 10:(256, 92,64,14), 11:(320, 92,64,14),
                                       12:(0,156,64,14), 13:(64,156,64,14), 14:(128,156,64,14), 15:(192,156,64,14), 16:(256,156,64,14), 17:(320,156,64,14),
                                       18:(0,220,64,14), 19:(64,220,64,14), 20:(128,220,64,14), 21:(192,220,64,14), 22:(256,220,64,14), 23:(320,220,64,14),
                                       24:(0,284,64,14), 25:(64,284,64,14), 26:(128,284,64,14), 27:(128,284,64,14), 28:(256,284,64,14), 29:(320,284,64,14),
                                       30:(0,348,64,14), 31:(64,348,64,14)
                                     }

                
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	#crea la animacion
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	#funcion que se encarga de mover al personaje
	def update(self, direccion, op):
		if direccion == 'estatica':
                        self.clip(self.barra[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
	#funcion que detecta los eventos que son del tipo teclado
	def handle_event(self, op):
                        self.update('estatica', op)


