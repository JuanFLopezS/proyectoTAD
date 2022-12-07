import pygame as btn

class button():
    def __init__(self, x, y, width, high, word):
        self.rectangle = btn.Rect(x,y,width,high)
        self.word = word
        self.active = False

    def draw(self, SCREEN):
        font = btn.font.Font(None, 20)
        if self.rectangle.collidepoint(btn.mouse.get_pos()):
            btn.draw.rect(SCREEN, (47,54,55), self.rectangle, 0)
        else:
            btn.draw.rect(SCREEN, (57,96,102), self.rectangle, 0)
        txt = font.render(self.word, True, (0,0,0))
        SCREEN.blit(txt, (self.rectangle.x+(self.rectangle.width-txt.get_width())/2, self.rectangle.y+(self.rectangle.height-txt.get_height)/2))