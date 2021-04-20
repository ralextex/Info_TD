import pygame
import os
import math

class Tower():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("sprites/tower.png")
        self.width = 0
        self.height = 0
        self.size =32
        self.inRange = False
        self.range = 200

        self.place_color = (0,0,255, 100)

    def draw(self, window):
        """
        Zeigt die Tower an
        :param win: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        window.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
    
    def draw_placement(self,window):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (self.range, self.range), self.range, 0)

        window.blit(surface, (self.x - self.range, self.y - self.range))

    def target(self, enemies):
        """
        Greift Enemies an
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path[x.path_seg])
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if first_enemy.hit() == True:
                money += 1
                enemies.remove(first_enemy)
        return money
