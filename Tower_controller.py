from Tower import *
from Rect import *
import pygame

class Tower_controller():
    def __init__ (self,screen):
        self.screen = screen
        self.towers = []
        self.money = 500
        self.legal = [Rect(10,10,80,590),Rect(170,10,540,510),Rect(540,10,790,220),Rect(620,310,790,590)]
        self.illegal=[]
        self.space = 14
    
    def display_towers(self):
        for tower in self.towers:
            tower.draw(self.screen)
        #self.tower.draw_radius(self.screen)

    def legal_pos(self,x,y):
        for rect in self.legal:
            if(rect.inside(x,y)):
                for tow in self.towers:
                    if(tow.hitbox.inside(x,y)):
                        return False
                return True
        return False

    def add_tower(self ,x ,y):
        if(self.legal_pos(x,y)):
            tower = Tower(x, y)
            if(self.money >= tower.price):
                self.money -= tower.price
                self.towers.append(tower)
                return True
            else:
                print("Not Enough Money")
                return False
        else:
            print("Out Of Bounds")
            return False
        
    def attack(self, clk, enemies):
        for tower in self.towers:
            self.money += tower.target(clk,self.screen,enemies)

    def round_ready(self):
        for tower in self.towers:
            tower.prev = 0