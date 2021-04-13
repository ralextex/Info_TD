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
        self.size =16
        self.price = [0,0,0]
        self.level = 1
        self.selected = False
        self.range = 100

        self.place_color = (0,0,255, 100)

    def draw(self, window):
        """
        Zeigt die Tower an
        :param win: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        window.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
    
    def draw_radius(self,window):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            window.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self,window):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        window.blit(surface, (self.x - 50, self.y - 50))


    # def click(self, X, Y):
    #     """
    #     returns if tower has been clicked on
    #     and selects tower if it was clicked
    #     :param X: int
    #     :param Y: int
    #     :return: bool
    #     """
    #     img = self.tower_imgs[self.level - 1]
    #     if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
    #         if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
    #             return True
    #     return False

    # def sell(self):
    #     """
    #     call to sell the tower, returns sell price
    #     :return: int
    #     """
    #     return self.sell_price[self.level-1]

    # def upgrade(self):
    #     """
    #     upgrades the tower for a given cost
    #     :return: None
    #     """
    #     if self.level < len(self.tower_imgs):
    #         self.level += 1
    #         self.damage += 1

    # def get_upgrade_cost(self):
    #     """
    #     returns the upgrade cost, if 0 then can't upgrade anymore
    #     :return: int
    #     """
    #     return self.price[self.level-1]
