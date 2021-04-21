import pygame
import sys
from Rect import Rect

class Button():
    def __init__(self,screen,x,y,w,h,txt,font,col,id):
        """
        Variablen
        :param : surface, X-Koordinate, Y-Koordinate, Weite, Höhe, Text, Font, Farbe, ID
        :return: None
        """
        self.screen = screen

        self.id = id
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.rect = Rect(x,y,x+w,y+h)

        self.mode = 0

        self.color = col
        self.color_light = (200,200,200)
        self.color_dark = (100,100,100)
        self.font = font
        self.text = txt

    def display_button(self,mode):
        """
        Zeigt die Buttons an
        :param : Modus
        :return: None
        """

        if(mode == 1):
            pygame.draw.rect(self.screen,self.color_light,(self.x,self.y,self.w,self.h))
        elif(mode == 2):
            pygame.draw.rect(self.screen,self.color_dark,(self.x,self.y,self.w,self.h))
        else:
            pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.w,self.h))
        self.screen.blit( self.font.render((self.text), False,(0, 0, 0) ),(self.x,self.y))
        
    def highlight(self):
        """
        Markiert den Button wenn Maus in Button
        :return: None
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if(self.rect.inside(mouse_x,mouse_y)):
            self.mode = 1
        else:
            self.mode = 0