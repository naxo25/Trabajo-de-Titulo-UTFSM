# -*- coding: utf-8 -*-
#modulos importados
import pygame as game
import sys
import eventos
import perfil
import variables as v
from personaje import *
from pygame.locals import *
from random import randint
""" agree perfil """


class menu_juego():

    def __init__(self):
        self.salir = False
        self.salir1 = False
        self.mantener = True
        self.pantalla = game.display.set_mode((1000,650))
        self.fuente = game.font.Font(None, 25)
        self.opcion = 1
        self.pj_selec = 0
        self.pj_enemigo = -1
        self.fondo = pygame.image.load("image/mapa.png")
        self.xc, self.yc = {}, {}
        self.pj_selec_enemigo = {0: randint(0,4), 1: randint(0,4), 2: randint(0,4), 3: randint(0,4), 4: randint(0,4)}
        self.tamano = 40
        self.exp_mult = 20
        self.player =   {  0 : Personaje(self.tamano * 5, self.tamano * 10, "img/annie_mov.png"),
                           1 : Personaje(self.tamano * 3, self.tamano * 5, "img/zero_mov.png"),
                           2 : Personaje(self.tamano * 11, self.tamano * 7, "img/hisoka_mov.png"),
                           3 : Personaje(self.tamano * 8, self.tamano * 7, "img/megaman_mov.png"),
                           4 : Personaje(self.tamano * 7, self.tamano * 4, "img/mikasa_mov.png") }

        self.enemigo = { 0: Enemigo(self.tamano * 4, self.tamano * 9, "img/orco_mov.png"),
                         1: Enemigo(self.tamano * 3, self.tamano * 10, "img/orco_mov.png"),
                         2: Enemigo(self.tamano * 8, self.tamano * 4, "img/orco_mov.png"),
                         3: Enemigo(self.tamano * 7, self.tamano * 10, "img/sonic_mov.png"),
                         4: Enemigo(self.tamano * 12, self.tamano * 8, "img/sonic_mov.png"),
                         5: Enemigo(self.tamano * 6, self.tamano * 12, "img/lord_mov.png"),
                         6: Enemigo(self.tamano * 9, self.tamano * 7, "img/lord_mov.png"),
                         7: Enemigo(self.tamano * 8, self.tamano * 9, "img/lord_mov.png"),
                         8: Enemigo(self.tamano * 15, self.tamano * 1, "img/angevo_mov.png") }

        
        
        reloj = pygame.time.Clock()


    def loop(self, pantalla):
        while not self.salir:
                for event in game.event.get():
                        if  event.type == game.QUIT:
                                        sys.exit(0)
                self.verificar_opciones()
                self.actualizar_imagen()
                game.display.flip()
        self.salir = False
        
    def verificar_opciones(self):
            k = game.key.get_pressed()

            if self.mantener == False:
                if self.opcion > 1 and k[K_UP]:
                    self.opcion -= 1
                elif self.opcion < 5 and k[K_DOWN]:
                    self.opcion += 1
                elif k[K_RETURN]:
                    self.enter()

            #al mantener presionada una tecla cambiara el valor de mantener de false a true
            self.mantener = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def enter(self):
        
        if self.opcion == 1:  #pasar turno (no hacer nada)
            self.player[self.pj_selec].no_actualizar()
            self.pj_selec += 1             
            self.salir = True
        elif self.opcion == 2:   #mover 
            self.salir = True
            self.zona_mov()
        elif self.opcion == 3:  #atacar 
            self.salir = True
            self.zona_ataque()
        elif self.opcion == 4:  #inventario
            self.inventario()
            self.salir = True
        elif self.opcion == 5: #salir
            self.salir = True
        self.opcion = 1
        

    def inventario(self):
        #carga la imagen de fondo del inventario
        imagen = game.image.load("image/menus/Inventario.png")
        self.pantalla.blit(imagen,(100,90))
        #carga la imagen del pj que corresponda el inventario
        imagen_pj = self.cambiar_img_inv()
        self.pantalla.blit(imagen_pj,(690,97))
        #carga sprite de zona seleccion en inventario
        z_selec_inv_img = game.image.load("image/x_seleccion_inv.png")
        z_selec = pygame.sprite.Sprite()
	z_selec.image = z_selec_inv_img
	z_selec.rect = z_selec_inv_img.get_rect()
	z_selec.rect.top = 225
	z_selec.rect.left = 115
        buff_dano = 0
        
	pos_x_inv = 0
        k = game.key.get_pressed()
        while not self.salir1:
            y_item = 230
            y_equipo = 230
            item_inv = {}
            dano_item = {}
            #cargar items en el inventario
            for i in perfil.estado.inventario_pj[self.pj_selec]:
                #item del inventario
                item_inv[i] = perfil.estado.nombre_item[perfil.estado.inventario_pj[self.pj_selec][i]]
                #atributo del item
                dano_item[i] = perfil.estado.puntos_objeto[perfil.estado.inventario_pj[self.pj_selec][i]]
                #mensaje que se muestra en inventario
                mensaje = self.fuente.render(item_inv[i]+"  + "+str(dano_item[i]),0,(255,255,255))
                self.pantalla.blit(mensaje,(150,y_item))
                y_item += 40
            dano_item = {}
            for i in perfil.estado.equipo_pj[self.pj_selec]:
                #item equipado
                item_equip = perfil.estado.nombre_item[perfil.estado.equipo_pj[self.pj_selec][i]]
                dano_item[i] = perfil.estado.puntos_objeto[perfil.estado.equipo_pj[self.pj_selec][i]]
                mensaje2 = self.fuente.render(item_equip,0,(255,255,255))
                self.pantalla.blit(mensaje2,(570,y_equipo))
                y_equipo += 40
                
            #estadisticas en el inventario
            ataque_p = perfil.estado.dano_min[self.pj_selec] + dano_item[0]
            ataque_pj = perfil.estado.dano_max[self.pj_selec] + dano_item[0]
            atq = self.fuente.render("ATQ: "+str(ataque_p)+ " - "+str(ataque_pj)+" (+"+str(dano_item[0])+")",0,(255,255,255))
            self.pantalla.blit(atq,(570,440))
            #perfil.estado.dano_max[self.pj_selec] = ataque_pj
            defensa_pj = perfil.estado.defensa[self.pj_selec] + dano_item[1]
            deff = self.fuente.render("DEF: "+str(defensa_pj)+" +("+str(dano_item[1])+")",0,(255,255,255))
            self.pantalla.blit(deff,(570,460))
            vida_pj = perfil.estado.vida[self.pj_selec]
            vidamax_pj = perfil.estado.vida_max[self.pj_selec] 
            vida = self.fuente.render("HP: "+str(vida_pj)+"/"+str(vidamax_pj),0,(255,255,255))
            self.pantalla.blit(vida,(570,480))
            exp = perfil.estado.exp[self.pj_selec]
            nivel_ant = perfil.estado.nivel[self.pj_selec] - 1
            exp_max = int(perfil.estado.nivel[self.pj_selec] * 1.3 + nivel_ant * 1.3) * self.exp_mult
            msg = self.fuente.render("EXP: "+str(exp)+"/"+str(exp_max),0,(255,255,255))
            self.pantalla.blit(msg,(570,500))
            msg_btn = self.fuente.render("'X' Aceptar",0,(50,250,50))
            msg_btn2 = self.fuente.render("'Z' Atras",0,(50,250,50))
            self.pantalla.blit(msg_btn,(640,380))
            self.pantalla.blit(msg_btn2,(640,400))
            

            buff_lista = {}
            for event in game.event.get():
                if  event.type == game.QUIT:
                    sys.exit(0)
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:                           
                        self.salir1 = True
                        
		    elif event.key == game.K_UP:
                        if z_selec.rect.top > 225:
                            z_selec.rect.top -= 40
                            self.pantalla.blit(imagen,(100,90))
                            self.pantalla.blit(imagen_pj,(690,97))
                            self.pantalla.blit(z_selec.image, z_selec.rect)
                            pos_x_inv -= 1
		    elif event.key == game.K_DOWN:
                        ult_item = 220
                        if len(item_inv)>1:
                             for j in range(len(item_inv)):
                                ult_item = ult_item + 40
                        if z_selec.rect.top < ult_item-40:
                            z_selec.rect.top += 40
                            self.pantalla.blit(imagen,(100,90))
                            self.pantalla.blit(imagen_pj,(690,97))
                            self.pantalla.blit(z_selec.image, z_selec.rect)
                            pos_x_inv +=1
                    elif event.key == game.K_x:
                        buff_item = perfil.estado.inventario_pj[self.pj_selec][pos_x_inv]
                        #consumir pota
                        if buff_item == 10 and perfil.estado.vida[self.pj_selec]<>perfil.estado.vida_max[self.pj_selec]:
                            perfil.estado.inventario_pj[self.pj_selec].pop(pos_x_inv)
                            v = pos_x_inv
                            while  len(perfil.estado.inventario_pj[self.pj_selec]) > v:
                                perfil.estado.inventario_pj[self.pj_selec][v] = perfil.estado.inventario_pj[self.pj_selec][v+1]
                                perfil.estado.inventario_pj[self.pj_selec].pop(v+1)
                                v += 1
                            perfil.estado.vida[self.pj_selec] += 25
                            if perfil.estado.vida[self.pj_selec]>perfil.estado.vida_max[self.pj_selec]:
                                perfil.estado.vida[self.pj_selec] = perfil.estado.vida_max[self.pj_selec]
                        else:
                            #validar arma
                            if perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] in range(1,6):
                                buff_item = perfil.estado.equipo_pj[self.pj_selec][0]
                                perfil.estado.equipo_pj[self.pj_selec][0] = perfil.estado.inventario_pj[self.pj_selec][pos_x_inv]
                                perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] = buff_item
                            #validar escudo
                            if perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] in range(6,10):
                                buff_item = perfil.estado.equipo_pj[self.pj_selec][1]
                                perfil.estado.equipo_pj[self.pj_selec][1] = perfil.estado.inventario_pj[self.pj_selec][pos_x_inv]
                                perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] = buff_item
                            #validar armadura
                            #if perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] in [5,6,7,8]:
                             #   buff_item = perfil.estado.equipo_pj[self.pj_selec][1]
                              #  perfil.estado.equipo_pj[self.pj_selec][1] = perfil.estado.inventario_pj[self.pj_selec][pos_x_inv]
                               # perfil.estado.inventario_pj[self.pj_selec][pos_x_inv] = buff_item
                        self.pantalla.blit(imagen,(100,90))
                        self.pantalla.blit(imagen_pj,(690,97))
                        self.pantalla.blit(z_selec.image, z_selec.rect)
            
            self.pantalla.blit(z_selec.image,z_selec.rect)
            game.display.flip()
        self.salir1 = False


    def zona_mov(self):
        #cuadrado zona ataque
        z_movimiento_img = game.image.load("image/z_movimiento.png")
        z_movimiento = pygame.sprite.Sprite()
	z_movimiento.image = z_movimiento_img
	z_movimiento.rect = z_movimiento_img.get_rect()
        #z_ataque.set_colorkey(0)
        #cuadrado zona seleccion
        z_selec_img = game.image.load("image/x_seleccion.png")
        z_selec = pygame.sprite.Sprite()
	z_selec.image = z_selec_img
	z_selec.rect = z_selec_img.get_rect()
	#manual -> instrucciones para jugar
        manual = game.image.load("image/menus/manual.png")
	
	z_pj_selec_img = game.image.load("image/x_seleccion.png")
        z_pj_selec = pygame.sprite.Sprite()
	z_pj_selec.image = z_pj_selec_img
	z_pj_selec.rect = z_pj_selec_img.get_rect()
	
        limite = 80
        avance = 40
        #coordenadas del personaje
        cor_x_pj = self.player[self.pj_selec].x
        cor_y_pj = self.player[self.pj_selec].y
        #coordenada zona de ataque
        x = z_movimiento.rect.left = cor_x_pj - limite 
        y = z_movimiento.rect.top  = cor_y_pj - limite 
        #coordenadas zona de seleccion
	xs = z_selec.rect.left = cor_x_pj 
	ys = z_selec.rect.top  = cor_y_pj
	
	z_pj_selec.rect.left = cor_x_pj
        z_pj_selec.rect.top  = cor_y_pj
       
        while not self.salir1:
            #dibujar area amarilla alrededor de personaje seleccionado
            self.cargar_mundo()
            self.pantalla.blit(manual,(770,30))
            for i in [x,x+40,x+80,x+120,x+160]:
                for j in [y,y+40,y+160,y+80,y+120]:
                    z_movimiento.rect.left = i
                    z_movimiento.rect.top  = j
                    self.pantalla.blit(z_movimiento.image,z_movimiento.rect)
                    
            self.actualizar_perfil(z_selec)
            self.pantalla.blit(z_selec.image, z_selec.rect)
            self.pantalla.blit(z_pj_selec.image, z_pj_selec.rect)
            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:                           
                        pass
                    #falta mover la zona seleccion
                    if event.key == game.K_LEFT:
                        if z_selec.rect.left > cor_x_pj - limite and z_selec.rect.left > 0 and z_movimiento.rect.left > 0:
                            z_selec.rect.left -= avance
                            if z_selec.rect.left == cor_x_pj > 0 and z_selec.rect.top == cor_y_pj:
                                z_selec.rect.left -= avance
                    elif event.key == game.K_RIGHT:
                        if z_selec.rect.left < cor_x_pj + limite and z_selec.rect.left < 990 and z_movimiento.rect.left < 990:
                            z_selec.rect.left += avance
                            if (z_selec.rect.left == cor_x_pj < 990 and z_selec.rect.top == cor_y_pj):
                                z_selec.rect.left += avance
		    elif event.key == game.K_UP:
                        if z_selec.rect.top > cor_y_pj - limite and z_selec.rect.top > 0 and z_movimiento.rect.top > 0:
                            z_selec.rect.top -= avance
                            if z_selec.rect.top == cor_y_pj > 0 and z_selec.rect.left == cor_x_pj:
                                z_selec.rect.top -= avance  
		    elif event.key == game.K_DOWN:
                        if z_selec.rect.top < cor_y_pj + limite:
                            z_selec.rect.top += avance
                            if z_selec.rect.top == cor_y_pj < 990 and z_selec.rect.left == cor_x_pj:
                                z_selec.rect.top += avance
                    elif event.key == game.K_x:
                        colision = 0
                        for i in self.enemigo:
                            if self.enemigo[i].rect.colliderect(z_selec) and not perfil.validar_vida(i + 5):
                                colision = 1
                            elif colision <> 1:
                                colision = 0
                        if colision == 0:
                            for i in self.player:
                                if self.player[i].rect.colliderect(z_selec) and not perfil.validar_vida(i):
                                    colision = 1
                                elif colision <> 1:
                                    colision = 0
                        if colision == 0:
                            self.player[self.pj_selec].actualizar(z_selec.rect.left, z_selec.rect.top)
                            self.pantalla.blit(self.player[self.pj_selec].parte,self.player[self.pj_selec].rect)
                            self.salir1 = True
                            self.pj_selec += 1
                    elif event.key == game.K_z:
                        self.salir1 = True
            
            game.display.flip()
        self.salir1 = False    

    def zona_ataque(self):
        #cuadrado zona ataque
        z_movimiento_img = game.image.load("image/z_atack.png")
        z_movimiento = pygame.sprite.Sprite()
	z_movimiento.image = z_movimiento_img
	z_movimiento.rect = z_movimiento_img.get_rect()
        #z_ataque.set_colorkey(0)
        #cuadrado zona seleccion
        z_selec_img = game.image.load("image/x_seleccion.png")
        z_selec = pygame.sprite.Sprite()
	z_selec.image = z_selec_img
	z_selec.rect = z_selec_img.get_rect()
	
        manual = game.image.load("image/menus/manual.png")

	z_pj_selec_img = game.image.load("image/x_seleccion.png")
        z_pj_selec = pygame.sprite.Sprite()
	z_pj_selec.image = z_pj_selec_img
	z_pj_selec.rect = z_pj_selec_img.get_rect()
        
        limite = 40
        #coordenadas del personaje
        cor_x_pj = self.player[self.pj_selec].x
        cor_y_pj = self.player[self.pj_selec].y
        #coordenada zona de ataque
        x = cor_x_pj - limite 
        y = cor_y_pj - limite 
        #coordenadas zona de seleccion
	xs = z_selec.rect.left = cor_x_pj - limite
	ys = z_selec.rect.top  = cor_y_pj - limite
	z_pj_selec.rect.left = cor_x_pj
        z_pj_selec.rect.top  = cor_y_pj
       
        while not self.salir1:
            #dibujar area roja alrededor de personaje seleccionado
            self.cargar_mundo()
            self.pantalla.blit(manual,(770,30))
            for i in [x,x+40,x+80]:
                for j in [y,y+40,y+80]:
                    z_movimiento.rect.left = i
                    z_movimiento.rect.top  = j
                    self.pantalla.blit(z_movimiento.image,z_movimiento.rect)
                                       
            self.actualizar_perfil(z_selec)            
            self.pantalla.blit(z_selec.image, z_selec.rect)
            self.pantalla.blit(z_pj_selec.image, z_pj_selec.rect)
                                       
            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:                           
                        pass
                    #falta mover la zona seleccion
                    if event.key == game.K_LEFT:
                        if z_selec.rect.left > cor_x_pj - limite:
                            z_selec.rect.left -= limite
                            if z_selec.rect.left == cor_x_pj and z_selec.rect.top == cor_y_pj:
                                z_selec.rect.left -= limite
                    elif event.key == game.K_RIGHT:
                        if z_selec.rect.left < cor_x_pj + limite:
                            z_selec.rect.left += limite
                            if z_selec.rect.left == cor_x_pj and z_selec.rect.top == cor_y_pj:
                                z_selec.rect.left += limite
		    elif event.key == game.K_UP:
                        if z_selec.rect.top > cor_y_pj - limite:
                            z_selec.rect.top -= limite
                            if z_selec.rect.top == cor_y_pj and z_selec.rect.left == cor_x_pj:
                                z_selec.rect.top -= limite                 
		    elif event.key == game.K_DOWN:
                        if z_selec.rect.top < cor_y_pj + limite:
                            z_selec.rect.top += limite
                            if z_selec.rect.top == cor_y_pj and z_selec.rect.left == cor_x_pj:
                                z_selec.rect.top += limite
                    elif event.key == game.K_x:
                        for i in self.enemigo:
                            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                                eventos.batle(self.pj_selec, i + 5, 1)
                                self.salir1 = True
                                self.pj_selec += 1
                    elif event.key == game.K_z:
                        self.salir1 = True
            
            game.display.flip()
        self.salir1 = False


    def zona_libre(self,pantalla):
        #cuadrado zona seleccion
        z_selec_img = game.image.load("image/x_seleccion.png")
        z_selec = pygame.sprite.Sprite()
	z_selec.image = z_selec_img
	z_selec.rect = z_selec_img.get_rect()

        z_pj_selec_img = game.image.load("image/x_seleccion.png")
        z_pj_selec = pygame.sprite.Sprite()
	z_pj_selec.image = z_pj_selec_img
	z_pj_selec.rect = z_pj_selec_img.get_rect()
        #coordenadas del personaje
        cor_x_pj = self.player[self.pj_selec].x
        cor_y_pj = self.player[self.pj_selec].y
        z_selec.rect.left = cor_x_pj
        z_selec.rect.top  = cor_y_pj

        z_pj_selec.rect.left = cor_x_pj
        z_pj_selec.rect.top  = cor_y_pj
        
        avance=40
        fondo = pygame.image.load("image/mapa.png")

                
        while not self.salir1:

            self.cargar_mundo()
            self.actualizar_perfil(z_selec)
            self.pantalla.blit(z_selec.image, z_selec.rect)
            self.pantalla.blit(z_pj_selec.image, z_pj_selec.rect)
            
            for event in game.event.get():
                for event in game.event.get():
                        if  event.type == game.QUIT:
                                        sys.exit(0)
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:                           
                        self.loop(pantalla)
                        self.salir1 = True
                    if event.key == game.K_LEFT:
                        if  z_selec.rect.left > 0:
                            z_selec.rect.left -= avance
                    elif event.key == game.K_RIGHT:
                        if  z_selec.rect.left < 950:
                            z_selec.rect.left += avance
		    elif event.key == game.K_UP:
                        if z_selec.rect.top > 0:
                            z_selec.rect.top -= avance
		    elif event.key == game.K_DOWN:
                        if z_selec.rect.top < 600:
                            z_selec.rect.top += avance
                        
            
            game.display.flip()
        self.salir1 = False

    def cargar_mundo(self):
            self.pantalla.blit(self.fondo,(0,0))
            for i in self.player:
                if not perfil.validar_vida(i):                                                
                    self.pantalla.blit(self.player[i].parte,self.player[i].rect)
            for i in self.enemigo:
                if not perfil.validar_vida(i + 5):
                    self.pantalla.blit(self.enemigo[i].parte,self.enemigo[i].rect)

    def actualizar_perfil(self, z_selec):
        puntos_equipo={}
        
        for j in perfil.estado.equipo_pj[self.pj_selec]:
                #item equipado
                puntos_equipo[j] = perfil.estado.puntos_objeto[perfil.estado.equipo_pj[self.pj_selec][j]]
                
        actual = perfil.cambiar_perfil(self.pj_selec)
        self.pantalla.blit(actual,(650,370))
        #nombre personaje
        nombre = perfil.estado.nombre[self.pj_selec]
        nivel = str(perfil.estado.nivel[self.pj_selec])
        nombre_msg = self.fuente.render(nombre +" Nv." +nivel,0,(0,0,0))
        self.pantalla.blit(nombre_msg,(810,385))
        #vida personaje seleccionado
        vida_pj = perfil.estado.vida[self.pj_selec]
        vidamax_pj = perfil.estado.vida_max[self.pj_selec]
        pintar_vida = perfil.pintar_vida(self.pj_selec)
        vida_msg = self.fuente.render("HP: "+str(vida_pj)+"/"+str(vidamax_pj),0,(pintar_vida))
        self.pantalla.blit(vida_msg,(810,405))
        #atauqe personaje seleccionado
        ataque_pj = perfil.estado.dano_max[self.pj_selec] + puntos_equipo[0]
        ataque_p = perfil.estado.dano_min[self.pj_selec] + puntos_equipo[0]
        atq_msg = self.fuente.render("ATQ: "+str(ataque_p)+" - "+str(ataque_pj),0,(0,0,0))
        self.pantalla.blit(atq_msg,(810,425))
        #defensa personaje seleccionado
        defensa_pj = perfil.estado.defensa[self.pj_selec] + puntos_equipo[1]
        def_msg = self.fuente.render("DEF: "+str(defensa_pj),0,(0,0,0))
        self.pantalla.blit(def_msg,(810,445))
        exp = perfil.estado.exp[self.pj_selec]
        nivel_ant = perfil.estado.nivel[self.pj_selec] - 1
        exp_max = int(perfil.estado.nivel[self.pj_selec] * 1.3 + nivel_ant * 1.3) * self.exp_mult
        msg = self.fuente.render("EXP: "+str(exp)+"/"+str(exp_max),0,(0,0,0))
        self.pantalla.blit(msg,(810,465))
        
        for i in self.player:
            for j in perfil.estado.equipo_pj[i]:
                #item equipado
                puntos_equipo[j] = perfil.estado.puntos_objeto[perfil.estado.equipo_pj[i][j]]
            cambiar_perfil = perfil.cambiar_perfil(i)
            if z_selec.rect.colliderect(self.player[i]) and not perfil.validar_vida(i) and self.pj_selec <> i:
                self.pantalla.blit(cambiar_perfil,(650,502))
                #nombre personaje
                nombre = perfil.estado.nombre[i]
                nivel = str(perfil.estado.nivel[i])
                nombre_msg = self.fuente.render(nombre +" Nv." +nivel,0,(0,0,0))
                self.pantalla.blit(nombre_msg,(810,520))
                #vida personaje seleccionado
                vida_pj = perfil.estado.vida[i]
                vidamax_pj = perfil.estado.vida_max[i]
                pintar_vida = perfil.pintar_vida(i)
                vida_msg = self.fuente.render("HP: "+str(vida_pj)+"/"+str(vidamax_pj),0,(pintar_vida))
                self.pantalla.blit(vida_msg,(810,540))
                #atauqe personaje seleccionado
                ataque_pj = perfil.estado.dano_max[i] + puntos_equipo[0]
                ataque_p = perfil.estado.dano_min[i] + puntos_equipo[0]
                atq_msg = self.fuente.render("ATQ: "+str(ataque_p)+" - "+str(ataque_pj),0,(0,0,0))
                self.pantalla.blit(atq_msg,(810,560))
                #defensa personaje seleccionado
                defensa_pj = perfil.estado.defensa[i] + puntos_equipo[1]
                def_msg = self.fuente.render("DEF: "+str(defensa_pj),0,(0,0,0))
                self.pantalla.blit(def_msg,(810,580))
                exp = perfil.estado.exp[i]
                nivel_ant = perfil.estado.nivel[i] - 1
                exp_max = int(perfil.estado.nivel[i] * 1.3 + nivel_ant * 1.3) * self.exp_mult
                msg = self.fuente.render("EXP: "+str(exp)+"/"+str(exp_max),0,(0,0,0))
                self.pantalla.blit(msg,(810,600))

        for i in self.enemigo:
            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                cambiar_perfil = perfil.cambiar_perfil(i + 5)
                self.pantalla.blit(cambiar_perfil,(650,502))
                #nombre personaje
                nombre = perfil.estado.nombre[i + 5]
                nombre_msg = self.fuente.render(nombre,0,(255,0,0))
                self.pantalla.blit(nombre_msg,(810,520))
                #vida personaje seleccionado
                vida_pj = perfil.estado.vida[i + 5]
                vidamax_pj = perfil.estado.vida_max[i + 5]
                pintar_vida = perfil.pintar_vida(i + 5)
                vida_msg = self.fuente.render("HP: "+str(vida_pj)+"/"+str(vidamax_pj),0,(pintar_vida))
                self.pantalla.blit(vida_msg,(810,540))
                #atauqe personaje seleccionado
                ataque_pj = perfil.estado.dano_max[i + 5]
                ataque_p = perfil.estado.dano_min[i + 5]
                atq_msg = self.fuente.render("ATQ: "+str(ataque_p)+" - "+str(ataque_pj),0,(0,0,0))
                self.pantalla.blit(atq_msg,(810,560))
                #defensa personaje seleccionado
                defensa_pj = perfil.estado.defensa[i + 5]
                def_msg = self.fuente.render("DEF: "+str(defensa_pj),0,(0,0,0))
                self.pantalla.blit(def_msg,(810,580))
                
    def cambiar_img_inv(self):
        if self.pj_selec == 0:
            imagen = game.image.load("perfiles/annie_inv.png")
        elif self.pj_selec == 1:
            imagen = game.image.load("perfiles/zero_inv.png")
        elif self.pj_selec == 3:
            imagen = game.image.load("perfiles/megaman_inv.png")
        elif self.pj_selec == 2:
            imagen = game.image.load("perfiles/hisoka_inv.png")
        elif self.pj_selec == 4:
            imagen = game.image.load("perfiles/mikasa_inv.png")
        return imagen
            
    def actualizar_imagen(self):
        if self.opcion == 1:
            imagen = game.image.load("image/menus/menu_interactuar_1.png")
        elif self.opcion == 2:
            imagen = game.image.load("image/menus/menu_interactuar_2.png")        
        elif self.opcion == 3:
            imagen = game.image.load("image/menus/menu_interactuar_3.png")
        elif self.opcion == 4:
            imagen = game.image.load("image/menus/menu_interactuar_4.png")
        elif self.opcion == 5:
            imagen = game.image.load("image/menus/menu_interactuar_5.png")
        elif self.opcion == 6:
            imagen = game.image.load("image/menus/menu_interactuar_6.png")
        self.pantalla.blit(imagen,(770,30))

    def zona_enemigo(self):
        #cuadrado zona ataque
        z_ataque = game.Surface((40,40))
        verde = (250,250,0)
        z_ataque.fill(verde)
        #z_ataque.set_colorkey(0)
        #cuadrado zona seleccion
        z_selec_img = game.image.load("image/x_seleccion.png")
        z_selec = pygame.sprite.Sprite()
	z_selec.image = z_selec_img
	z_selec.rect = z_selec_img.get_rect()

        limite = 80
        avance = 40
        #coordenadas del personaje
        cor_x_pj = self.enemigo[self.pj_enemigo].x
        cor_y_pj = self.enemigo[self.pj_enemigo].y
        #coordenada zona de ataque
        x = cor_x_pj - 80 
        y = cor_y_pj - 80 
        #coordenadas zona de seleccion
	xs = z_selec.rect.left = cor_x_pj
	ys = z_selec.rect.top  = cor_y_pj
                            
        lista_vida = perfil.estado
        lista = self.player
        self.enemigo[self.pj_enemigo].buscar(lista, lista_vida)
        xc = self.enemigo[self.pj_enemigo].getX()
        yc = self.enemigo[self.pj_enemigo].getY()
        movio = 0

        self.pantalla.blit(z_selec.image, z_selec.rect)

        pj = self.pj_enemigo + 5
        enemigo = perfil.cambiar_perfil(pj)
        self.pantalla.blit(enemigo,(650,370))
        #nombre personaje
        nombre = perfil.estado.nombre[pj]
        nombre_msg = self.fuente.render(nombre,0,(0,0,0))
        self.pantalla.blit(nombre_msg,(810,385))
        #vida personaje seleccionado
        vida_pj = perfil.estado.vida[pj]
        vidamax_pj = perfil.estado.vida_max[pj]
        pintar_vida = perfil.pintar_vida(pj)
        vida_msg = self.fuente.render("HP: "+str(vida_pj)+"/"+str(vidamax_pj),0,(pintar_vida))
        self.pantalla.blit(vida_msg,(810,405))
        #atauqe personaje seleccionado
        ataque_pj = perfil.estado.dano_max[pj]
        ataque_p = perfil.estado.dano_min[pj]
        atq_msg = self.fuente.render("ATQ: "+str(ataque_p)+" - "+str(ataque_pj),0,(0,0,0))
        self.pantalla.blit(atq_msg,(810,425))
        #defensa personaje seleccionado
        defensa_pj = perfil.estado.defensa[pj]
        def_msg = self.fuente.render("DEF: "+str(defensa_pj),0,(0,0,0))
        self.pantalla.blit(def_msg,(810,445))
        
        valor = 40
        
        
        if z_selec.rect.left > xc:
                z_selec.rect.left -= valor
                for i in self.player:
                    if self.colision(z_selec,i):
                        eventos.batle(i, self.pj_enemigo + 5, 2)
                        z_selec.rect.left += valor
                        movio = 1
                    if movio == 0:
                        for i in self.enemigo:
                            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                                z_selec.rect.left += valor    
        if z_selec.rect.left < xc and movio == 0:
                z_selec.rect.left += valor
                for i in self.player:
                    if self.colision(z_selec,i):
                        eventos.batle(i, self.pj_enemigo + 5, 2)
                        z_selec.rect.left -= valor
                        movio = 1
                    if movio == 0:
                        for i in self.enemigo:
                            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                                z_selec.rect.left -= valor
        if z_selec.rect.top > yc and movio == 0:
                z_selec.rect.top  -= valor
                for i in self.player:
                    if self.colision(z_selec,i):
                        eventos.batle(i, self.pj_enemigo + 5, 2)
                        z_selec.rect.top += valor
                        movio = 1
                    if movio == 0:
                        for i in self.enemigo:
                            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                                z_selec.rect.top += valor
        if z_selec.rect.top < yc and movio == 0:
                z_selec.rect.top  += valor
                for i in self.player:
                    if self.colision(z_selec,i):
                        eventos.batle(i, self.pj_enemigo + 5, 2)
                        z_selec.rect.top -= valor
                        movio = 1
                    if movio == 0:
                        for i in self.enemigo:
                            if z_selec.rect.colliderect(self.enemigo[i]) and not perfil.validar_vida(i + 5):
                                z_selec.rect.top -= valor
        
        self.enemigo[self.pj_enemigo].actualizar(z_selec.rect.left, z_selec.rect.top)
        game.display.flip()

    def colision(self, z_selec, pj):
        atacar = False
        if z_selec.rect.colliderect(self.player[pj]) and not perfil.validar_vida(pj):
            atacar = True
        return atacar
        
    def pausa(self):
            salir = True
            tiempo = game.time.get_ticks()/220
            while salir:
                actual = game.time.get_ticks()/220
                if actual - tiempo == 3:
                    salir = False
