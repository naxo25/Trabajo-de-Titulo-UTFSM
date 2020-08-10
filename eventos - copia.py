# -*- coding: utf-8 -*-
#modulos importados
import pygame as game
import sys
import time
import perfil as menuC
from sprites import *
from ataques import *
from random import randint
from pygame.locals import *

pantalla = game.display.set_mode((640,480))
barra = game.image.load("image/barra.png")
barra1 = barra
barra2 = barra
barrita = game.Surface((2,2))
hp = game.Surface((1,12))

def pelea(selec, enemigo, turno):
        
        fondo = game.image.load("image/fondo_batalla.jpg")
        i = 0
        player_pj = zero(200,300)
        
        cant_animaciones = 21
        vel_pj = 60
        selec_nom, selec_enemigo = "",""
        if selec == 0:
                imagen_player = game.image.load("perfiles/annie_inv.png")
                player_pj = annie(200,300)
                vel_pj = 60
                cant_animaciones = 12
        elif selec == 1:
                imagen_player = game.image.load("perfiles/zero_inv.png")
                player_pj = zero(200,300)
                vel_pj = 60
                cant_animaciones = 21
        elif selec == 2:
                imagen_player = game.image.load("perfiles/megaman_black.png")
                player_pj = megaman(200, 300)
                bala = canon(200,292)
                vel_pj = 45
                selec_nom = "megaman"
                cant_animaciones = 17
        elif selec == 3:
                imagen_player = game.image.load("perfiles/mikasa_inv.png")
                player_pj = mikasa(200,300)
                vel_pj = 100
                cant_animaciones = 12
        elif selec == 4:
                imagen_player = game.image.load("perfiles/mago_inv.png")
                player_pj = old_wizard(200,300)
                vel_pj = 135
                cant_animaciones = 14
                selec_nom = "mago_old"
                magia = magia_old(200,292)
        if enemigo < 8:
                imagen_enemigo = game.image.load("perfiles/orco_inv.png")
                player_enemigo = orco(700,305)
                cant_animaciones_enemigo = 4
                vel_enemigo = 120
        elif enemigo < 10:
                imagen_enemigo = game.image.load("perfiles/sonic_inv.png")
                player_enemigo = sonic(700,305)
                cant_animaciones_enemigo = 11
                vel_enemigo = 130
        elif enemigo < 13:
                imagen_enemigo = game.image.load("perfiles/cruzado_inv.png")
                player_enemigo = lord_hacha(700,305)
                cant_animaciones_enemigo = 12
                vel_enemigo = 70
        if enemigo == 13:
                imagen_enemigo = game.image.load("perfiles/angevo_inv.png")
                player_enemigo = angevo(700,305)
                cant_animaciones_enemigo = 8
                vel_enemigo = 90

                
        if 3 > 2:
                if turno == 1:
                        
                        if not menuC.validar_vida(selec):
                                salir = True
                                tiempo = game.time.get_ticks()/vel_pj
                        while salir == True:
                                pantalla.blit(fondo,(0,0))
                                actual = game.time.get_ticks()/vel_pj
                                i = actual - tiempo
                                #el programa funciona por milisegundos, osea entrara al while 100 veces mientras el tiempo solo aumentara de 0 a 30
                                if selec_nom == "mago_old":
                                        if i == 14:     
                                                player_pj.handle_event(0)
                                                player_enemigo.handle_event(0)
                                                magia.handle_event(14)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False
                                        elif i < 7:
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                i += 1
                                        elif i < 13 and i > 7:
                                                magia.handle_event(13)
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                pantalla.blit(magia.parte,magia.rect)
                                                i += 1
                
                                elif selec_nom == "megaman":
                                        if i == 17:     
                                                bala.handle_event(17)
                                                player_pj.handle_event(0)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False
                                        elif i < 7:
                                                player_enemigo.handle_event(0)
                                                player_pj.handle_event(i)
                                                i += 1                
                                        elif i < 17 and i > 6:
                                                bala.handle_event(i)
                                                player_pj.handle_event(0)
                                                pantalla.blit(bala.parte,bala.rect)
                                                i += 1
                                else:
                                        if i == cant_animaciones: 
                                                player_pj.handle_event(0)
                                                player_enemigo.handle_event(0)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False               
                                        elif i < cant_animaciones:
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                i += 1
                                #menu_stats
                                pantalla.blit(barra1,(180,500))
                                pantalla.blit(imagen_player,(70,435))
                                pantalla.blit(barra2,(730,130))
                                pantalla.blit(imagen_enemigo,(610,60))
                                pantalla.blit(player_enemigo.parte,player_enemigo.rect)
                                pantalla.blit(player_pj.parte,player_pj.rect)
                                cargar_barras(selec, enemigo)
                                game.display.update()
                        
                        if not menuC.validar_vida(enemigo):
                                salir = True
                                tiempo = game.time.get_ticks()/vel_enemigo
                        while salir == True:
                                pantalla.blit(fondo,(0,0))
                                actual = game.time.get_ticks()/vel_enemigo
                                i = actual - tiempo
                                if i == cant_animaciones_enemigo: 
                                        player_pj.handle_event(0)
                                        player_enemigo.handle_event(0)
                                        atacar_boss(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                        salir = False               
                                elif i < cant_animaciones_enemigo:
                                        player_pj.handle_event(0)
                                        player_enemigo.handle_event(i)
                                        i += 1
                                #menu_stats
                                pantalla.blit(barra1,(180,500))
                                pantalla.blit(imagen_player,(70,435))
                                pantalla.blit(barra2,(730,130))
                                pantalla.blit(imagen_enemigo,(610,60))
                                pantalla.blit(player_enemigo.parte,player_enemigo.rect)
                                pantalla.blit(player_pj.parte,player_pj.rect)
                                cargar_barras(selec, enemigo)
                                game.display.update()

                if turno == 2:

                        if not menuC.validar_vida(enemigo):
                                salir = True
                                tiempo = game.time.get_ticks()/vel_enemigo
                        while salir == True:
                                pantalla.blit(fondo,(0,0))
                                actual = game.time.get_ticks()/vel_enemigo
                                i = actual - tiempo
                                if i == cant_animaciones_enemigo: 
                                        player_pj.handle_event(0)
                                        player_enemigo.handle_event(0)
                                        atacar_boss(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                        salir = False               
                                elif i < cant_animaciones_enemigo:
                                        player_pj.handle_event(0)
                                        player_enemigo.handle_event(i)
                                        i += 1
                                #menu_stats
                                pantalla.blit(barra1,(180,500))
                                pantalla.blit(imagen_player,(70,435))
                                pantalla.blit(barra2,(730,130))
                                pantalla.blit(imagen_enemigo,(610,60))
                                pantalla.blit(player_enemigo.parte,player_enemigo.rect)
                                pantalla.blit(player_pj.parte,player_pj.rect)
                                cargar_barras(selec, enemigo)
                                game.display.update()
                        
                        if not menuC.validar_vida(selec):
                                salir = True
                                tiempo = game.time.get_ticks()/vel_pj
                        while salir == True:
                                pantalla.blit(fondo,(0,0))
                                actual = game.time.get_ticks()/vel_pj
                                i = actual - tiempo
                                #el programa funciona por milisegundos, osea entrara al while 100 veces mientras el tiempo solo aumentara de 0 a 30
                                if selec_nom == "mago_old":
                                        if i == 14:     
                                                player_pj.handle_event(0)
                                                player_enemigo.handle_event(0)
                                                magia.handle_event(14)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False
                                        elif i < 7:
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                i += 1
                                        elif i < 13 and i > 7:
                                                magia.handle_event(13)
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                pantalla.blit(magia.parte,magia.rect)
                                                i += 1
                
                                elif selec_nom == "megaman":
                                        if i == 17:     
                                                bala.handle_event(17)
                                                player_pj.handle_event(0)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False
                                        elif i < 7:
                                                player_enemigo.handle_event(0)
                                                player_pj.handle_event(i)
                                                i += 1                
                                        elif i < 17 and i > 6:
                                                bala.handle_event(i)
                                                player_pj.handle_event(0)
                                                pantalla.blit(bala.parte,bala.rect)
                                                i += 1
                                else:
                                        if i == cant_animaciones: 
                                                player_pj.handle_event(0)
                                                player_enemigo.handle_event(0)
                                                atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno)
                                                salir = False               
                                        elif i < cant_animaciones:
                                                player_pj.handle_event(i)
                                                player_enemigo.handle_event(0)
                                                i += 1
                                #menu_stats
                                pantalla.blit(barra1,(180,500))
                                pantalla.blit(imagen_player,(70,435))
                                pantalla.blit(barra2,(730,130))
                                pantalla.blit(imagen_enemigo,(610,60))
                                pantalla.blit(player_enemigo.parte,player_enemigo.rect)
                                pantalla.blit(player_pj.parte,player_pj.rect)
                                cargar_barras(selec, enemigo)
                                game.display.update()

def cargar_barras(selec, enemigo):
        vida_max = menuC.estado.vida_max[selec]
        vida = menuC.estado.vida[selec]
        color = pintar(vida_max,vida)
        negro = ((0,0,0))
        hp.fill(color)
        barrita.fill(negro)
        
        for i in range(0,15):
                pantalla.blit(barrita,(198, i + 518))
                pantalla.blit(barrita,(vida_max + 200, i + 518))
        for i in range(200,vida_max + 200):
                if vida + 200 > i:
                        pantalla.blit(hp,(i,520))
                pantalla.blit(barrita,(i,518))
                pantalla.blit(barrita,(i,532))
                
        vida_max = menuC.estado.vida_max[enemigo]
        vida = menuC.estado.vida[enemigo]
        pantalla.blit(barrita,(vida - 1,149))
        pantalla.blit(barrita,(vida_max + 1,151))
        color = pintar(vida_max,vida)
        hp.fill(color)
        borde = 740
        
        #pinta el borde de la barra negra
        for i in range(0,15):
                pantalla.blit(barrita,(borde - 2, i + 148))
                pantalla.blit(barrita,(vida_max + borde, i + 148))
        #genera la barra de hp segun la vida del personaje
        for i in range(borde, vida_max + borde):
                if vida + borde > i:
                        pantalla.blit(hp,(i,150))
                pantalla.blit(barrita,(i,148))
                pantalla.blit(barrita,(i,162))

def pintar(vida_max,vida):
        if vida <= (vida_max/3):
                color = (250,0,0)
        elif vida <= (vida_max/2):
                color = (180,0,0)
        elif vida <= (vida_max/2) + (vida_max/5):
                color = (120,60,0)
        elif vida <= (vida_max/2) + (vida_max/4):
                color = (60,130,0)
        elif vida <= (vida_max/2) + (vida_max/3):
                color = (60,170,0)
        elif vida <= (vida_max/2) + (vida_max/2):
                color = (0,200,0)
        elif vida == vida_max:
                color = (0,250,0)
        return color
        

def disminuir_barra(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo):
        cargar_barras(selec, enemigo)
        pantalla.blit(barra1,(180,500))
        pantalla.blit(imagen_player,(70,435))
        pantalla.blit(barra2,(730,130))
        pantalla.blit(imagen_enemigo,(610,60))
        pantalla.blit(player_enemigo.parte,player_enemigo.rect)
        pantalla.blit(player_pj.parte,player_pj.rect)
        cargar_barras(selec, enemigo)
        game.display.update()
        pausa()

def batle(selec, enemigo, turno):
        cargar_barras(selec, enemigo)
        pelea(selec, enemigo, turno)

def conseguir_item(pj):
        menuC.estado.inventario_pj[pj][len(menuC.estado.inventario_pj[pj])] = randint(1,11)

def atacar(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno):
    fuente = game.font.Font(None, 20)
    lista = menuC.estado
    dano = randint(lista.dano_min[selec], lista.dano_max[selec]) + lista.puntos_objeto[lista.equipo_pj[selec][0]]
    defensa = lista.defensa[enemigo]
    if dano <= defensa:
            dano = 1
    else:
            dano = dano - defensa
    mensaje = fuente.render(lista.nombre[enemigo] + " ha recibido " + str(dano) + " puntos",0,(0,0,0))
    pantalla.blit(mensaje,(100,100))
    vida_ant = lista.vida[enemigo]
    lista.vida[enemigo] -= dano
    if lista.vida[enemigo] < 0:
            lista.vida[enemigo] = 0
            mensaje = fuente.render(lista.nombre[selec] + " ha muerto",0,(0,0,0))
    vida_act = lista.vida[enemigo]
    conseguir_item(selec)
    vida_max = lista.vida_max[enemigo]
    disminuir_barra(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo)
    
def atacar_boss(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo, turno): 
    fuente = game.font.Font(None, 20)
    lista = menuC.estado
    dano = randint(lista.dano_min[enemigo],lista.dano_max[enemigo])
    defensa = lista.defensa[selec] + lista.puntos_objeto[lista.equipo_pj[selec][1]] + lista.puntos_objeto[lista.equipo_pj[selec][2]]
    if dano <= defensa:
            dano = 1
    else:
            dano = dano - defensa
    mensaje = fuente.render(lista.nombre[selec] + " ha recibido " + str(dano) + " puntos",0,(0,0,0))
    vida_ant = lista.vida[selec]
    lista.vida[selec] -= dano
    if lista.vida[selec] < 0:
            lista.vida[selec] = 0
            mensaje = fuente.render(lista.nombre[selec] + " ha muerto",0,(0,0,0))
    pantalla.blit(mensaje,(150,100))
    vida_act = lista.vida[selec]
    vida_max = lista.vida_max[selec]
    disminuir_barra(selec, enemigo, player_pj, imagen_player, player_enemigo, imagen_enemigo)

def pausa():
            salir = True
            tiempo = game.time.get_ticks()/200
            while salir:
                actual = game.time.get_ticks()/200
                if actual - tiempo == 5:
                    salir = False
    
    
