import pygame
import sys
from Rect import Rect

class Button():
    def __init__(self,screen,x,y,w,h,txt,font,col,id):
        """
        :param : surface, X-Koordinate, Y-Koordinate, Weite, Höhe, Text, Font, Farbe, ID
        """
        self.screen = screen

        self.id = id # Funktion der Button
        
        # Param in self umgewandelt
        self.x = x # Pos x oben linker Ecke
        self.y = y # pos y oben linker Ecke
        self.w = w # Breite
        self.h = h # Hoehe

        # Rect wird definiert
        self.rect = Rect(x,y,x+w,y+h)

        # Display modus
        self.mode = 0

        # Farben
        self.color = col
        self.color_light = (200,200,200)
        self.color_dark = (100,100,100)
        
        # Font and Text
        self.font = font
        self.text = txt

    def display_button(self,mode):
        """
        Zeigt den Button an
        :param : Modus
        :return: None
        """
        if(mode == 1):
            pygame.draw.rect(self.screen,self.color_light,(self.x,self.y,self.w,self.h))
        elif(mode == 2):
            pygame.draw.rect(self.screen,self.color_dark,(self.x,self.y,self.w,self.h))
        else:
            pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.w,self.h))
        
        for i in range(len(self.text)):
            self.screen.blit( self.font.render((self.text[i]), False,(0, 0, 0) ),(self.x,self.y + i*40))
        
    def highlight(self):
        """
        Markiert den Button wenn Maus ueber Button
        :return: None
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if(self.rect.inside(mouse_x,mouse_y)):
            self.mode = 1
        else:
            self.mode = 0