from re import T
from Image import Image
from Ventana import *
from pygame import *
from Events import *
import sys
import pygame as pg


class play:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.SCREEN = pg.display.set_mode((self.width, self.height))
        self.poker = poker(self.SCREEN, self.width, self.height)
        self.arbol = arbol(self.SCREEN, self.width, self.height)
        self.grafo = grafo(self.SCREEN, self.width, self.height)

    def run(self):
        pg.init()
        pg.time.Clock().tick(60)
        btn_solitary = button(self.width - 160, self.height - 240, 150, 50, 'SOLITARIO')
        btn_arbol = button(self.width - 160, self.height - 180, 150, 50, 'ARBOL')
        btn_grafo = button(self.width - 160, self.height - 120, 150, 50, 'GRAFOS')
        btn_menu = button(self.width - 160, self.height - 60, 150, 50, 'MENU')

        self.wallpaper()
        while True:
            '''Eventos'''
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if btn_solitary.rectangle.collidepoint(pg.mouse.get_pos()):
                        self.poker.active = True
                        self.arbol.active = False
                        self.grafo.active = False
                    if btn_arbol.rectangle.collidepoint(pg.mouse.get_pos()):
                        self.arbol.active = True
                        self.poker.active = False
                        self.grafo.active = False
                    if btn_menu.rectangle.collidepoint(pg.mouse.get_pos()):
                        self.poker.active = False
                        self.arbol.active = False
                        self.grafo.active = False
                        self.run()
                    if btn_grafo.rectangle.collidepoint(pg.mouse.get_pos()):
                        self.grafo.active = True
                        self.arbol.active = False
                        self.poker.active = False
                self.poker.eventos(event)
                self.arbol.eventos(event)
                self.grafo.eventos(event)
            if self.poker.active:
                self.poker.draw()
            if self.arbol.active:
                self.arbol.draw()
            if self.grafo.active:
                self.grafo.draw()
            btn_solitary.draw(self.SCREEN)
            btn_arbol.draw(self.SCREEN)
            btn_menu.draw(self.SCREEN)
            btn_grafo.draw(self.SCREEN)
            pg.display.update()

    def wallpaper(self):
        fondo = Image(0, 0, self.width, self.height, 'img/main_background.jpg', 0)
        temp = image.load(fondo.route)
        temp = pg.transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))


GAME = game(1000, 650)
GAME.run()

'''carta global'''
carta = None


def draw_tree(SCREEN):
    contador = 0
    delta = 50
    for lista_aux in mi_arbol.ramas:
        for i in lista_aux:
            draw.circle(SCREEN, "black", (500, 100), 50)
        contador += 1


def general_draw(SCREEN):
    if btn_poker.active:
        pantalla_poker(SCREEN)
    if btn_arbol.active:
        tree_screen(SCREEN)


def tree_screen(SCREEN):
    '''Fondo'''
    fondo = Image(0, 0, width, height, 'img/man_background.jpg')
    temp = image.load(fondo.route)
    temp = transform.scale(temp, (fondo.width, fondo.height))
    SCREEN.blit(temp, (fondo.x, fondo.y))
    text_surface = base_font.render(nodo_a_anadir, True, (0, 0, 0))
    SCREEN.blit(text_surface, (0, 0))