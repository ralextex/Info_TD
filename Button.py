import pygame
import sys

#define mode: 1 Light , 2 Dark

class Button():
    def __init__(self,screen,x,y,w,h,txt,font,col,id): 
        self.screen = screen

        self.id = id
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.mode = 0

        self.color = col
        self.color_light = (200,200,200)
        self.color_dark = (100,100,100)
        self.font = font
        self.text = txt

    def display_button(self,mode):
        if(mode == 1):
            pygame.draw.rect(self.screen,self.color_light,(self.x,self.y,self.w,self.h))
        elif(mode == 2):
            pygame.draw.rect(self.screen,self.color_dark,(self.x,self.y,self.w,self.h))
        else:
            pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.w,self.h))
        self.screen.blit( self.font.render((self.text), False,(0, 0, 0) ),(self.x,self.y))

    def highlight(self):
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if(self.inside(mouse_x,mouse_y)):
            self.mode = 1
        else:
            self.mode = 0
        
    def inside(self,x,y):
        if(self.x < x < self.x+self.w and self.y < y < self.y+self.h):
            return True
        else:
            return False

