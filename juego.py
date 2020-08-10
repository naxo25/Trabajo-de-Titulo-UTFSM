#!/usr/bin/env python
# -*- coding: utf-8 -*-

#modulos importados
import pygame
import sys
from menu_principal import *
from pygame.locals import *

#se ejecuta el juego
if __name__ == '__main__':
        pygame.init()
        menu = menu_principal()
        menu.cargar_menu_principal()
        sys.exit(0)
