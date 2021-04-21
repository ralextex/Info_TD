from Tower import *
from Rect import *
import pygame

class Tower_controller():
    def __init__ (self, screen, price_scaling):
        """
        :param: screen, Geld scaling
        """
        self.screen = screen

        self.towers = []
        
        self.money = 500 
        self.price = 200
        self.price_scaling = price_scaling

        # Definiert die benuzbaren Flaechen oder Verbotene
        self.legal = [Rect(10,10,80,590),Rect(170,10,540,510),Rect(540,10,790,220),Rect(620,310,790,590)]
        self.illegal=[]
    
    def display_towers(self):
        """
        Anzeige der Tower
        :return: None
        """
        for tower in self.towers:
            tower.draw(self.screen)

    def check_pos(self,x,y):
        """
        Ubzerprueft ob position benutzbar ist
        :param: X-Koordinate, Y-Koordinate
        :return: bool
        """
        for rect in self.legal: # Zulassene flaeche
            if(rect.inside(x,y)):
                for tow in self.towers: # nicht uber ein andere
                    if(tow.hitbox.inside(x,y)):
                        return False
                return True
        return False

    def add_tower(self ,x ,y):
        """
        Falls Position und Geld passen neue Tower erstellen  
        :param: X-Koordinate, Y-Koordinate
        :return: bool
        """
        if(self.check_pos(x,y)): # Check Position
            if(self.money >= self.price): # Check Money
                tower = Tower(x, y)
                self.money -= self.price 
                self.towers.append(tower) # Neue Tower
                self.price *= self.price_scaling # Preis Steigerung
                int(self.price)
                return True
            else:
                print("Not Enough Money")
                return False
        else:
            print("Out Of Bounds")
            return False
        
    def attack(self, clk, enemies):
        """
        Greift die gegner an 
        :param: Clock, list of enemies
        :return: None
        :todo: Not Crosschecking every Tower with every Gegner
        """
        for tower in self.towers:
            self.money += tower.target(clk,self.screen,enemies)

    def round_ready(self):
        """
        Macht alle Tower bereit für neue Runde
        :return: None
        """
        for tower in self.towers:
            tower.prev = 0 