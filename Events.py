import json
import pygame as pg
from Arbol import Arbol
from pygame import *
from Ventana import button
from Image import Image
from Node import Node
from Stack import Stack
from CollisionBox import collisionBox
from Elements import *
from Graph import Graph
import random
import sys


class poker:
    def __init__(self, SCREEN, width, height):
        self.active = False
        self.buttons = []
        self.SCREEN = SCREEN
        self.width = width
        self.height = height
        self.stacks = None
        self.winner_list = None
        self.hitbox = []
        self.carta = None
        self.define()

    def define(self):
        CARD_WIDTH = 140
        CARD_HEIGHT = 190
        card_2 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/2.png', 2)
        card_3 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/3.png', 3)
        card_4 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/4.png', 4)
        card_5 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/5.png', 5)
        card_6 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/6.png', 6)
        card_7 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/7.png', 7)
        card_8 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/8.png', 8)
        card_9 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/9.png', 9)
        card_10 = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/10.png', 10)
        card_A = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/As.png', 14)
        card_back = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/back.png', 0)
        card_J = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/J.png', 11)
        card_k = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/K.png', 12)
        card_Q = Image(0, 0, CARD_WIDTH, CARD_HEIGHT, 'Images/Q.png', 12)
        stack_1 = Stack([card_A, card_k, card_Q, card_J, card_4])
        stack_2 = Stack([card_7, card_8, card_6, card_10])
        stack_3 = Stack([card_5, card_2, card_3])
        stack_4 = Stack([card_9])
        self.stacks = [stack_1, stack_2, stack_3, stack_4]
        self.winner_list = [card_A, card_k, card_Q, card_J, card_10, card_9, card_8, card_7, card_6, card_5, card_4,card_3, card_2]
        hitbox1 = collisionBox(pg.Rect(80, 95, 135, 550))
        hitbox2 = collisionBox(pg.Rect(240, 95, 135, 550))
        hitbox3 = collisionBox(pg.Rect(400, 95, 135, 550))
        hitbox4 = collisionBox(pg.Rect(560, 95, 135, 550))
        self.hitbox.append(hitbox1)
        self.hitbox.append(hitbox2)
        self.hitbox.append(hitbox3)
        self.hitbox.append(hitbox4)

    def draw(self):
        self.fondo_poker()
        CARD_WIDTH = 130
        CARD_HEIGHT = 180
        counter = 0
        delta1 = 0
        delta2 = 0
        delta3 = 0
        delta4 = 0
        for stack in self.stacks:
            for aux in stack.pila:
                if counter == 0:
                    if aux != None:
                        temp = image.load(aux.route)
                        temp = transform.scale(temp, (aux.width, aux.height))
                        aux.x = 80
                        aux.y = 100 + delta1
                        self.SCREEN.blit(temp, (aux.x, aux.y))
                        delta1 += 30
                elif counter == 1:
                    if aux != None:
                        temp = image.load(aux.route)
                        temp = transform.scale(temp, (aux.width, aux.height))
                        aux.x = 240
                        aux.y = 100 + delta2
                        self.SCREEN.blit(temp, (aux.x, aux.y))
                        delta2 += 30
                elif counter == 2:
                    if aux != None:
                        temp = image.load(aux.route)
                        temp = transform.scale(temp, (aux.width, aux.height))
                        aux.x = 400
                        aux.y = 100 + delta3
                        self.SCREEN.blit(temp, (aux.x, aux.y))
                        delta3 += 30
                else:
                    if aux != None:
                        temp = image.load(aux.route)
                        temp = transform.scale(temp, (aux.width, aux.height))
                        aux.x = 560
                        aux.y = 100 + delta4
                        self.SCREEN.blit(temp, (aux.x, aux.y))
                        delta4 += 30
            counter += 1
        card_back = Image(714, 180, CARD_WIDTH, CARD_HEIGHT, 'Images/back.png', 0)
        temp = image.load(card_back.route)
        temp = transform.scale(temp, (card_back.width, card_back.height))
        self.SCREEN.blit(temp, (card_back.x, card_back.y))
        if self.carta != None:
            self.carta.x = mouse.get_pos()[0]
            self.carta.y = mouse.get_pos()[1]
            temp = image.load(self.carta.route)
            temp = transform.scale(temp, (self.carta.width, self.carta.height))
            self.SCREEN.blit(temp, (pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
        if self.stacks[0].ganador(self.winner_list) or self.stacks[1].ganador(self.winner_list) or self.stacks[
            2].ganador(self.winner_list) or self.stacks[3].ganador(self.winner_list):
            self.ganador()
            self.active = False

    def fondo_poker(self):
        '''Fondo'''
        fondo = Image(0, 0, self.width, self.height, 'Images/main_background.jpg', 0)
        temp = image.load(fondo.route)
        temp = transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))

    def eventos(self, evento: pg.event):
        if evento.type == MOUSEBUTTONDOWN:
            if self.hitbox[0].rect.collidepoint(mouse.get_pos()):
                if self.hitbox[0].active == False and self.hitbox[1].active == False and self.hitbox[
                    2].active == False and self.hitbox[3].active == False:
                    self.carta = self.stacks[0].head
                    self.stacks[0].eliminar()
                    self.hitbox[0].active = True
                elif self.hitbox[1].active:
                    if self.stacks[0].head != None:
                        if self.stacks[0].head.valor > self.carta.valor:
                            self.stacks[0].agregar(self.carta)
                            self.carta = None
                            self.hitbox[1].active = False
                    else:
                        self.stacks[0].agregar(self.carta)
                        self.carta = None
                        self.hitbox[1].active = False
                elif self.hitbox[2].active:
                    if self.stacks[0].head != None:
                        if self.stacks[0].head.valor > self.carta.valor:
                            self.stacks[0].agregar(self.carta)
                            self.carta = None
                            self.hitbox[2].active = False
                    else:
                        self.stacks[0].agregar(self.carta)
                        self.carta = None
                        self.hitbox[2].active = False
                elif self.hitbox[3].active:
                    if self.stacks[0].head != None:
                        if self.stacks[0].head.valor > self.carta.valor:
                            self.stacks[0].agregar(self.carta)
                            self.carta = None
                            self.hitbox[3].active = False
                    else:
                        self.stacks[0].agregar(self.carta)
                        self.carta = None
                        self.hitbox[3].active = False
                else:
                    if self.stacks[0].head != None:
                        if self.stacks[0].head.valor > self.carta.valor:
                            self.stacks[0].agregar(self.carta)
                            self.carta = None
                            self.hitbox[0].active = False
                    else:
                        self.stacks[0].agregar(self.carta)
                        self.carta = None
                        self.hitbox[0].active = False
                self.draw()
            if self.hitbox[1].rect.collidepoint(mouse.get_pos()):
                if self.hitbox[1].active == False and self.hitbox[0].active == False and self.hitbox[
                    2].active == False and self.hitbox[3].active == False:
                    self.carta = self.stacks[1].head
                    self.stacks[1].eliminar()
                    self.hitbox[1].active = True
                elif self.hitbox[0].active:
                    if self.stacks[1].head != None:
                        if self.stacks[1].head.valor > self.carta.valor:
                            self.stacks[1].agregar(self.carta)
                            self.carta = None
                            self.hitbox[0].active = False
                    else:
                        self.stacks[1].agregar(self.carta)
                        self.carta = None
                        self.hitbox[0].active = False
                elif self.hitbox[2].active:
                    if self.stacks[1].head != None:
                        if self.stacks[1].head.valor > self.carta.valor:
                            self.stacks[1].agregar(self.carta)
                            self.carta = None
                            self.hitbox[2].active = False
                    else:
                        self.stacks[1].agregar(self.carta)
                        self.carta = None
                        self.hitbox[2].active = False
                elif self.hitbox[3].active:
                    if self.stacks[1].head != None:
                        if self.stacks[1].head.valor > self.carta.valor:
                            self.stacks[1].agregar(self.carta)
                            self.carta = None
                            self.hitbox[3].active = False
                    else:
                        self.stacks[1].agregar(self.carta)
                        self.carta = None
                        self.hitbox[3].active = False
                else:
                    if self.stacks[1].head != None:
                        if self.stacks[1].head.valor > self.carta.valor:
                            self.stacks[1].agregar(self.carta)
                            self.carta = None
                            self.hitbox[1].active = False
                    else:
                        self.stacks[1].agregar(self.carta)
                        self.carta = None
                        self.hitbox[1].active = False
                self.draw()
            if self.hitbox[2].rect.collidepoint(mouse.get_pos()):
                if self.hitbox[2].active == False and self.hitbox[1].active == False and self.hitbox[
                    0].active == False and self.hitbox[3].active == False:
                    self.carta = self.stacks[2].head
                    self.stacks[2].eliminar()
                    self.hitbox[2].active = True
                elif self.hitbox[1].active:
                    if self.stacks[2].head != None:
                        if self.stacks[2].head.valor > self.carta.valor:
                            self.stacks[2].agregar(self.carta)
                            self.carta = None
                            self.hitbox[1].active = False
                    else:
                        self.stacks[2].agregar(self.carta)
                        self.carta = None
                        self.hitbox[1].active = False
                elif self.hitbox[0].active:
                    if self.stacks[2].head != None:
                        if self.stacks[2].head.valor > self.carta.valor:
                            self.stacks[2].agregar(self.carta)
                            self.carta = None
                            self.hitbox[0].active = False
                    else:
                        self.stacks[2].agregar(self.carta)
                        self.carta = None
                        self.hitbox[0].active = False
                elif self.hitbox[3].active:
                    if self.stacks[2].head != None:
                        if self.stacks[2].head.valor > self.carta.valor:
                            self.stacks[2].agregar(self.carta)
                            self.carta = None
                            self.hitbox[3].active = False
                    else:
                        self.stacks[2].agregar(self.carta)
                        self.carta = None
                        self.hitbox[3].active = False
                else:
                    if self.stacks[2].head != None:
                        if self.stacks[2].head.valor > self.carta.valor:
                            self.stacks[2].agregar(self.carta)
                            self.carta = None
                            self.hitbox[2].active = False
                    else:
                        self.stacks[2].agregar(self.carta)
                        self.carta = None
                        self.hitbox[2].active = False
                self.draw
            if self.hitbox[3].rect.collidepoint(mouse.get_pos()):
                if self.hitbox[2].active == False and self.hitbox[1].active == False and self.hitbox[
                    0].active == False and self.hitbox[3].active == False:
                    self.carta = self.stacks[3].head
                    self.stacks[3].eliminar()
                    self.hitbox[3].active = True
                elif self.hitbox[1].active:
                    if self.stacks[3].head != None:
                        if self.stacks[3].head.valor > self.carta.valor:
                            self.stacks[3].agregar(self.carta)
                            self.carta = None
                            self.hitbox[1].active = False
                    else:
                        self.stacks[3].agregar(self.carta)
                        self.carta = None
                        self.hitbox[1].active = False
                elif self.hitbox[0].active:
                    if self.stacks[3].head != None:
                        if self.stacks[3].head.valor > self.carta.valor:
                            self.stacks[3].agregar(self.carta)
                            self.carta = None
                            self.hitbox[0].active = False
                    else:
                        self.stacks[3].agregar(self.carta)
                        self.carta = None
                        self.hitbox[0].active = False
                elif self.hitbox[2].active:
                    if self.stacks[3].head != None:
                        if self.stacks[3].head.valor > self.carta.valor:
                            self.stacks[3].agregar(self.carta)
                            self.carta = None
                            self.hitbox[2].active = False
                    else:
                        self.stacks[3].agregar(self.carta)
                        self.carta = None
                        self.hitbox[2].active = False
                else:
                    if self.stacks[3].head != None:
                        if self.stacks[3].head.valor > self.carta.valor:
                            self.stacks[3].agregar(self.carta)
                            self.carta = None
                            self.hitbox[3].active = False
                    else:
                        self.stacks[3].agregar(self.carta)
                        self.carta = None
                        self.hitbox[3].active = False
                self.draw()

    def ganador(self):
        '''Fondo'''
        fondo = Image(0, 0, self.width, self.height, 'Images/winner.png', 0)
        temp = image.load(fondo.route)
        temp = transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))


class arbol:
    def __init__(self, SCREEN, width, height):
        self.active = False
        self.botones = []
        self.SCREEN = SCREEN
        self.width = width
        self.height = height
        self.mi_arbol = Arbol()
        self.text_field = None
        self.combo_box = None
        self.definir()

    def definir(self):
        self.combo_box = ComboBox('Recorrido', 870, 20, 120, 32)
        self.text_field = TextField('valor', 20, 40, 120, 23)
        self.combo_box.options.append('InOrden')
        self.combo_box.options.append('PostOrden')
        self.combo_box.options.append('PreOrden')
        self.combo_box.options.append('Amplitud')

    def draw(self):
        self.fondo_arbol()
        new_text = pg.font.SysFont("bahnschrift", 20).render('Nodo a añadir', True, "black")
        self.SCREEN.blit(new_text, (19, 10))
        self.text_field.draw_text_field(self.SCREEN)
        self.combo_box.deploy(self.SCREEN)
        if self.mi_arbol.raiz != None:
            self.dibujar_arbol()
        self.show_traversal()

    def fondo_arbol(self):
        '''Fondo'''
        fondo = Image(0, 0, self.width, self.height, 'img/main_background.jpg', 0)
        temp = image.load(fondo.route)
        temp = transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))

    def eventos(self, evento: pg.event):
        if evento.type == pg.KEYDOWN:
            if self.text_field.active:
                if evento.key == pg.K_BACKSPACE:
                    self.text_field.input = self.text_field.input[:-1]
                elif evento.key == pg.K_RETURN:
                    if self.text_field.input != "":
                        try:
                            nodo_temp = self.mi_arbol.buscar_nodo(self.mi_arbol.raiz, int(self.text_field.input))
                            print(nodo_temp)
                            if nodo_temp == None:
                                self.mi_arbol.agregar(int(self.text_field.input))
                            self.text_field.input = ''
                        except:
                            self.text_field.input = ''
                else:
                    self.text_field.input += evento.unicode
        if evento.type == pg.MOUSEBUTTONDOWN:
            if self.text_field.hitbox.collidepoint(pg.mouse.get_pos()):
                self.text_field.active = True
            else:
                self.text_field.active = False
            if self.combo_box.size.collidepoint(pg.mouse.get_pos()):
                if self.combo_box.deployed:
                    self.combo_box.deployed = False
                else:
                    self.combo_box.deployed = True
            if self.combo_box.deployed:
                self.combo_box.select_item()

    def dibujar_arbol(self):
        xDelta, yDelta = 150, 60
        xCoordenada = self.SCREEN.get_width() // 2

        def dfs(node: Node, level, xCoordenada, xDelta, r):
            x, y = xCoordenada, yDelta * (level + 1)
            if node.izquierda:
                draw.line(self.SCREEN, (0, 0, 0), (x, y), (x - xDelta, y + yDelta), 3)
            if node.derecha:
                draw.line(self.SCREEN, (0, 0, 0), (x, y), (x + xDelta, y + yDelta), 3)
            if node.izquierda != None:
                dfs(node.izquierda, level + 1, xCoordenada - xDelta, xDelta - (xDelta * 0.45), r - 1)
            if node.derecha != None:
                dfs(node.derecha, level + 1, xCoordenada + xDelta, xDelta - (xDelta * 0.45), r - 1)

            if node.izquierda == None and node.derecha == None and node != self.mi_arbol.raiz:
                draw.circle(self.SCREEN, (0, 0, 0), (x, y), r)
                draw.circle(self.SCREEN, (0, 0, 0), (x, y), r, 2)
            else:
                draw.circle(self.SCREEN, (0, 0, 0), (x, y), r)
                draw.circle(self.SCREEN, (0, 0, 0), (x, y), r, 2)

            node_value = pg.font.Font(None, 20).render(str(node.valor), True, (255, 255, 255))
            self.SCREEN.blit(node_value, (x - node_value.get_width() // 2, y - node_value.get_height() // 2))

        dfs(self.mi_arbol.raiz, 0, xCoordenada, xDelta, 25)

    def show_traversal(self):
        temp_font = pg.font.Font(None, 24)
        if self.combo_box.selected_item == 'InOrden':
            self.mi_arbol.inorder()
            txt = temp_font.render(self.combo_box.selected_item + ' = ' + str(self.mi_arbol.traversal), True, (0, 0, 0))
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 0)
            pg.draw.rect(self.SCREEN, (0, 0, 0),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 2)
            self.SCREEN.blit(txt, (self.SCREEN.get_width() // 2 - txt.get_width() // 2,
                                   self.SCREEN.get_height() - 100 + txt.get_height() // 2))
        elif self.combo_box.selected_item == 'PreOrden':
            self.mi_arbol.preorder()
            txt = temp_font.render(self.combo_box.selected_item + ' = ' + str(self.mi_arbol.traversal), True, (0, 0, 0))
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 0)
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 2)
            self.SCREEN.blit(txt, (self.SCREEN.get_width() // 2 - txt.get_width() // 2,
                                   self.SCREEN.get_height() - 100 + txt.get_height() // 2))
        elif self.combo_box.selected_item == 'PostOrden':
            self.mi_arbol.postorder()
            txt = temp_font.render(self.combo_box.selected_item + ' = ' + str(self.mi_arbol.traversal), True, (0, 0, 0))
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 0)
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 2)
            self.SCREEN.blit(txt, (self.SCREEN.get_width() // 2 - txt.get_width() // 2,
                                   self.SCREEN.get_height() - 100 + txt.get_height() // 2))
        elif self.combo_box.selected_item == 'Amplitud':
            self.mi_arbol.amplitud()
            txt = temp_font.render(self.combo_box.selected_item + ' = ' + str(self.mi_arbol.traversal), True, (0, 0, 0))
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 0)
            pg.draw.rect(self.SCREEN, (145, 171, 103),
                         (self.SCREEN.get_width() // 2 - txt.get_width() // 2 - 15, self.SCREEN.get_height() - 100, txt.get_width() + 30, 32), 2)
            self.SCREEN.blit(txt, (self.SCREEN.get_width() // 2 - txt.get_width() // 2,
                                   self.SCREEN.get_height() - 100 + txt.get_height() // 2))


class grafo:
    def __init__(self, SCREEN, width, height):
        self.active = False
        self.SCREEN = SCREEN
        self.width = width
        self.height = height
        self.btn_dijkstra = None
        self.peso_input = TextField("peso", 70, self.height - 40, 100, 30)
        self.mi_grafo = None
        self.combo_box_origen = ComboBox('ORIGEN', 10, 10, 80, 30)
        self.combo_box_destino = ComboBox('DESTINO', self.width - 245, 10, 80, 30)
        self.mi_grafo = Graph()
        self.ruta_dijkstra = None
        self.texto_recorrido = []
        self.costo_recorrido = ""
        self.definir()

    def draw(self):
        self.fondo_pantalla()
        self.combo_box_origen.deploy(self.SCREEN)
        self.combo_box_destino.deploy(self.SCREEN)
        self.mi_grafo.draw(self.SCREEN)
        self.btn_dijkstra.draw(self.SCREEN)
        self.peso_input.draw_text_field(self.SCREEN)
        new_text = pg.font.SysFont("bahnschrift", 20).render('PESO', True, "black")
        self.SCREEN.blit(new_text, (10, self.height - 40))
        recorrido_text = pg.font.SysFont("bahnschrift", 20).render('RECORRIDO:', True, "black")
        self.SCREEN.blit(recorrido_text, (180, self.height - 80))
        costo_recorrido_txt = pg.font.SysFont("bahnschrift", 20).render("COSTO VIAJE:", True, "black")
        self.SCREEN.blit(costo_recorrido_txt, (180, self.height - 40))
        text = pg.font.SysFont("bahnschrift", 20).render(str(self.texto_recorrido), True, "black")
        self.SCREEN.blit(text, (300, self.height - 80))
        costo_recorrido = pg.font.SysFont("bahnschrift", 20).render(str(self.costo_recorrido), True, "black")
        self.SCREEN.blit(costo_recorrido, (310, self.height - 40))
        if self.ruta_dijkstra != None:
            for i in range(len(self.ruta_dijkstra) - 1):
                pg.draw.line(self.SCREEN, (255, 0, 0), self.ruta_dijkstra[i].position, self.ruta_dijkstra[i + 1].position, 4)

    def definir(self):
        self.read_json()
        for vertice in self.mi_grafo.vertices:
            self.combo_box_origen.options.append(vertice.value)
            self.combo_box_destino.options.append(vertice.value)
        self.btn_dijkstra = button(self.width - 160, 350, 150, 50, "DIJKSTRA")

    def fondo_pantalla(self):
        '''Fondo'''
        self.SCREEN.fill((255, 255, 255))
        fondo = Image(250, 0, 500, 650, 'Images/mapa.png', 0)
        temp = image.load(fondo.route)
        temp = transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))

    def read_json(self):
        with open("ciudades.json") as data:
            ciudades = json.load(data)
            for ciudad in ciudades:
                self.mi_grafo.add_vertex(ciudad.get("id"), (ciudad.get("x"), ciudad.get("y")))
            for ciudad in ciudades:
                for destino in ciudad.get("destinations"):
                    self.mi_grafo.add_edge(ciudad.get("id"), destino, -1, False)

    def eventos(self, evento):
        if evento.type == pg.KEYDOWN:
            if self.peso_input.active:
                if evento.key == pg.K_BACKSPACE:
                    self.peso_input.input = self.peso_input.input[:-1]
                elif evento.key == pg.K_RETURN:
                    if self.peso_input.input != "":
                        try:
                            peso = int(self.peso_input.input)
                            origen = self.mi_grafo.index(str(self.combo_box_origen.selected_item))
                            destino = self.mi_grafo.index(str(self.combo_box_destino.selected_item))
                            if self.mi_grafo.matrix[origen][destino] == -1 or self.mi_grafo.matrix[origen][destino] > 0:
                                if int(self.peso_input.input) > 0:
                                    self.mi_grafo.matrix[origen][destino] = int(self.peso_input.input)
                                    self.mi_grafo.matrix[destino][origen] = int(self.peso_input.input)
                            self.peso_input.input = ""
                        except:
                            self.peso_input.input = ""
                else:
                    self.peso_input.input += evento.unicode
        if evento.type == pg.MOUSEBUTTONDOWN:
            if self.peso_input.hitbox.collidepoint(pg.mouse.get_pos()):
                self.peso_input.active = True
            else:
                self.peso_input.active = False
            if self.combo_box_origen.size.collidepoint(pg.mouse.get_pos()):
                if self.combo_box_origen.deployed:
                    self.combo_box_origen.deployed = False
                else:
                    self.combo_box_origen.deployed = True
            if self.combo_box_origen.deployed:
                self.combo_box_origen.select_item()
            if self.combo_box_destino.size.collidepoint(pg.mouse.get_pos()):
                if self.combo_box_destino.deployed:
                    self.combo_box_destino.deployed = False
                else:
                    self.combo_box_destino.deployed = True
            if self.combo_box_destino.deployed:
                self.combo_box_destino.select_item()
            if self.btn_dijkstra.rectangulo.collidepoint(pg.mouse.get_pos()):
                origen = self.mi_grafo.index(str(self.combo_box_origen.selected_item))
                destino = self.mi_grafo.index(str(self.combo_box_destino.selected_item))
                print(self.mi_grafo.matrix[origen][destino])
                if self.mi_grafo.matrix[origen][destino] > 0:
                    tupla_ciudades = self.mi_grafo.dijkstra(origen, destino)
                    ruta = tupla_ciudades[1]
                    lista = []
                    self.texto_recorrido.clear()
                    for i in ruta:
                        lista.append(self.mi_grafo.vertices[i])
                        self.texto_recorrido.append(self.mi_grafo.vertices[i].value)
                    self.ruta_dijkstra = lista
                    self.costo_recorrido = tupla_ciudades[0]