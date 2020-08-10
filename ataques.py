# -*- coding: utf-8 -*-
#modulos importados
import pygame
from pygame.locals import *

#--------------------------------- CLASES ---------------------------------------------------
class zero(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/zero_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,45,55), 1: (60,0,60,55), 2: (120,0,70,55), 3: (195,0,90,55), 4: (285,0,105,55), 5: (395,0,75,55), 6: (470,0,75,55),
                                       7: (0,70,75,50), 8: (80,70,55,50), 9: (145,70,55,50), 10: (210,70,45,50), 11: (260,70,45,55), 12: (315,60,55,65),
                                       13: (375,55,70,65), 14: (460,55,90,65), 15: (0,125,90,50), 16: (92,124,80,51), 17: (174,129,71,56), 18: (244,127,70,45),
                                       19: (313,129,70,46), 20: (384,126,60,47), 21: (446,126,54,50), 22: (0,210,46,75), 23: (50,210,40,55), 24: (90,210,51,55),
                                       25: (139,210,45,65), 26: (185,210,50,65), 27: (240,210,50,65), 28: (295,210,50,65), 29: (350,200,65,65), 30:(430,200,105,65),
                                       31: (0,270,105,80), 32: (105,270,107,80), 33: (212,270,108,80), 34: (325,270,70,80), 35: (400,270,60,80), 36: (465,270,60,80),
                                       37: (0,370,55,50), 38: (60,370,50,50), 39: (110,370,50,55), 40: (160,370,55,50), 41: (205,370,50,50), 42: (260,370,50,50)}

                
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
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
	#funcion que detecta los eventos que son del tipo teclado
	def handle_event(self, op):
                        self.update('atack', op)

class hisoka(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/hisoka_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,10,40,75), 1:(40,10,40,75), 2: (80,10,40,75), 3:(150,10,70,75), 4:(250,10,100,75), 5:(350,10,120,75),
                                       6:(470,10,90,75), 7:(590,10,80,75), 8:(680,10,70,75), 9:(150,90,75,65), 10:(245,90,100,65), 11:(360,90,105,65),
                                       12:(475,90,110,65), 13:(590,85,80,65), 14:(680,85,80,70), 15:(150,160,60,80), 16:(225,160,70,70), 17:(300,160,75,70),
                                       18:(390,160,85,70), 19:(480,160,75,70), 20:(580,160,70,75), 21:(670,160,45,70), 22:(715,165,40,65)}

                
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
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
	#funcion que detecta los eventos que son del tipo teclado
	def handle_event(self, op):
                        self.update('atack', op)


class megaman(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/Megaman_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,132,47,55), 1: (261,0,57,49), 2: (200,0,66,49), 3: (140,0,54,49), 4: (75,0,70,49), 5: (0,0,80,49), 6: (0,132,47,55)}


	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
			self.rect.left += 0
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class orco(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/orco_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,52,84), 1: (53,0,61,80), 2: (112,0,35,84), 3: (149,0,65,78), 4: (215,0,66,76)}


	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class sonic(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/sonic_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,150,80),  1: (150,0,150,80), 2: (300,0,150,80), 3:(450,0,150,80),
                                       4: (0,80,150,80),  5: (150,80,150,80), 6: (300,80,150,80), 7:(450,80,150,80),
                                       8: (0, 180,150,80), 9:(160,180,150,80), 10:(20,270,600,90), 11:(20,380,600,90),
                                       12:(20,270,600,90), 13:(20,380,600,90), 14:(20,380,600,90), 15:(20,270,600,90) }


	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
                if op == 10:
                        self.rect.left = 270
                elif op == 0:
                        self.rect.left = 700
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)

class canon(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/Megaman_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.canon = { 7: (240,60,78,70), 8: (160,60,80,70), 9: (80,60,80,70), 10: (0,60,80,70), 11: (305,200,50,40),
                               12: (245,200,60,50), 13: (180,200,60,55), 14: (120,200,60,55), 15: (60,200,60,55), 16: (0,200,60,55)}

	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
                if op == 17:
                        self.rect.left = 200                
		elif direccion == 'atack':
                        self.rect.left += 18
                        self.clip(self.canon[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class magia_old(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/old_wizard_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.magia = { 13:(225,185,75,85) }

	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):               
		if direccion == 'atack':
                        self.rect.right += 14
                        self.clip(self.magia[13])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class lord_hacha(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/Lord_hacha_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,110,57),  1: (125,0,115,58), 2: (245,0,120,58), 3:(365,0,115,60),
                                       4: (0,59,120,56), 5: (125,65,115,58), 6: (245,65,115,54), 7: (366,62,114,55),
                                       8: (0, 125,120,175), 9:(125,125,115,58), 10:(245,125,115,68), 11:(365,125,115,55) }


	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class annie(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/annie_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,66,56),  1: (66,0,66,56),  2: (132,0,58,56),  3: (190,0,66,56),  4: (256,0,64,56),  5: (320,0,66,56),
                                       6: (0,74,66,56), 7: (32,74,66,56), 8: (132,74,66,56), 9:(190,74,66,56), 10:(256,74,66,56), 11:(320,74,66,56)}
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class mikasa(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/mikasa_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,58,55),  1: (58,0,58,55),  2: (116,0,56,55),  3: (172,0,56,55),   4: (228,0,56,55),  5: (284,0,56,55),
                                       6: (0,60,58,55), 7: (58,60,58,55), 8: (116,60,56,55), 9:(172,60,58,55), 10:(228,60,56,55), 11:(284,60,56,55)}
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)
                        

class old_wizard(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/old_wizard_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,75,80),   1:(75,0,75,80),   2: (150,0,75,80),   3: (225,0,75,80),     4: (300,0,75,80),
                                       5: (0,80,75,105), 6:(75,80,75,105), 7: (150,80,75,105), 8: (225, 80,75,105), 9:(300,80,75,105),
                                       10:(0,185,75,85), 11:(75,185,75,85),12:(150,185,75,85), 13:(225,185,75,85)}
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)


class angevo(pygame.sprite.Sprite):

        def __init__(self,x,y):
                self.imagen = pygame.image.load("img/angevo_atq.png")
                self.imagen.set_clip(pygame.Rect(0,0,45,45))
                self.parte = self.imagen.subsurface(self.imagen.get_clip())
                self.rect = self.parte.get_rect()
                self.rect.top = y
                self.rect.left = x
                self.frame = 0
                
                self.atacar_states = { 0: (0,0,120,130), 1:(120,0,120,130),   2: (250,0,120,130),   3: (370,0,120,130),
                                       4: (0,130,120,130), 5: (120,130,120,130), 6:(260,130,110,130), 7: (380,130,120,130) }
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame > (len(frame_set) - 1):
			self.frame = 0
		return frame_set[self.frame]
	
	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.imagen.set_clip(pygame.Rect(clipped_rect))
		return clipped_rect
	
	def update(self, direccion, op):
		if direccion == 'atack':
                        self.clip(self.atacar_states[op])
		self.parte = self.imagen.subsurface(self.imagen.get_clip())
		
	def handle_event(self, op):
                        self.update('atack', op)
