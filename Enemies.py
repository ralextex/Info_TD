import pygame
import math
import os

class Enemy():
    def __init__(self,x,y,path):
        self.alive = 1
        self.size = 100
        self.speed = 3
        self.img = pygame.image.load("sprites/rot.png")
        self.path = path
        self.path_seg = 0
        self.x = x #self.path[0][0]
        self.y = y #self.path[0][1]

    def display(self, window):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        window.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
        #self.draw_health_bar(win)

    # def draw_health_bar(self, win):
    #     """
    #     #draw health bar above enemy
    #     #:param win: surface
    #     #:return: None
    #     """
    #     length = 50
    #     move_by = round(length / self.max_health)
    #     health_bar = move_by * self.health

    #     pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
    #     pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0)
    
    # def collide(self, X, Y):
    #     """
    #     #Returns if position has hit enemy
    #     #:param x: int
    #     #:param y: int
    #     #:return: Bool
    #     """
    #     if X <= self.x + self.width and X >= self.x:
    #         if Y <= self.y + self.height and Y >= self.y:
    #             return True
    #     return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        dir_x = self.path[self.path_seg][0] - self.x
        if(dir_x < 0):
            self.x -= self.speed
        elif (dir_x > 0):
            self.x += self.speed

        dir_y = self.path[self.path_seg][1] - self.y
        if(dir_y < 0):
            self.y -= self.speed
        elif (dir_y > 0):
            self.y += self.speed

        if(self.reached()):
            self.x = self.path[self.path_seg-1][0]
            self.y = self.path[self.path_seg-1][1]

    def reached(self):
        if (abs(self.path[self.path_seg][0] - self.x)<self.speed and abs(self.path[self.path_seg][1] - self.y)<self.speed):
            self.path_seg += 1
            if(self.path_seg >= len(self.path)):
                self.alive = 0
            return True
        else:
            return False


    # def hit(self, damage):
    #     """
    #     #Returns if an enemy has died and removes one health
    #     #each call
    #     #:return: Bool
    #     """
    #     self.health -= damage
    #     if self.health <= 0:
    #         return True
    #     else:
    #         return False
