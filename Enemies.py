import pygame
import math
import os

class Enemy():
    def __init__(self,x,y,path, health):
        """
        :param : spawn ort X, spawn ort Y, Weg
        """
        self.alive = True # Gegner noch lebendig
        self.size = 100 # Sprite bitte anpassen
        self.speed = 5 # Geschwindigkeit
        self.img = pygame.image.load("sprites/schwarz.png") # Bild für die Sprite
        self.path = path # Weg vom Start zur Ende
        self.path_seg = 0 # Weg stück
        self.x = x # X Position Mittelpunkt
        self.y = y # Y Position Mittelpunkt
        self.value = 10 # Wie viel Geld wert
        self.max_health = health # Wie viel Leben Maximal
        self.health = self.max_health # Zustand wie viel Leben

    def display(self, screen):
        """
        Zeigt der Gegner an
        :param screen: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        screen.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        """
        Genreirt eine Lebensanzeige über gegner
        :param screen: surface
        :return: None
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(screen, (255,0,0), (self.x-int(length/2), self.y-25, length, 10), 0)
        pygame.draw.rect(screen, (0, 255, 0), (self.x-int(length/2), self.y - 25, health_bar, 10), 0)

    def move(self):
        """
        Bewegt den Gegner
        :return: None
        """
        # Geht in X Richtung
        dir_x = self.path[self.path_seg][0] - self.x
        if(dir_x < 0):
            self.x -= self.speed
        elif (dir_x > 0):
            self.x += self.speed
            
        # Geht in Y Richtung
        dir_y = self.path[self.path_seg][1] - self.y
        if(dir_y < 0):
            self.y -= self.speed
        elif (dir_y > 0):
            self.y += self.speed
        
        # Ziel erreicht
        if(self.reached()):
            self.x = self.path[self.path_seg-1][0]
            self.y = self.path[self.path_seg-1][1]

    def reached(self):
        """
        Sagt ob das Gegner zum ende eines Segment gekommen ist
        :return: bool
        """
        if (abs(self.path[self.path_seg][0] - self.x)<self.speed and abs(self.path[self.path_seg][1] - self.y)<self.speed):
            self.path_seg += 1
            if(self.path_seg >= len(self.path)):
                self.alive = False
            return True
        else:
            return False