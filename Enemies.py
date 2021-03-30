import pygame
import math
from enemy_sprites import Rot

class Enemy:
    imgs = []
    def __init__(self,weite,höhe):

        self.width = weite
        self.height = höhe
        self.img = None
        self.health = 10
        self.path = [(126, 4), (128, 549), (574, 554), (581, 257), (794, 264)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.vel = 3
        self.path_pos = 0
        self.move_count = 0


    def draw(self,screen):
        """
        Generiert die Gegener
        benötigte parameter = pygame.surface
        :return = None
        """
        self.img = self.imgs
        screen.blit(self.img,(self.x,self.y))
        self.move()

    def collission(self,X,Y):
        """
        Gibt an wenn ein gegner getroffen wird
        x = int
        y = int
        :return = Bool
        """
        if X<= self.x +self.width and X >= self.x:
            if Y <self.y + self.height and Y >= self.y:
                return True
        return False
    def move(self):
        """
        Ist für die Bewegung der Gegener zuständig
        :return: none
        """
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        dirn = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0] / length, dirn[1] / length)

        if dirn[0] < 0 and not (self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        # zum nächtesn punkt gehen
        if dirn[0] >= 0:  #  rechts bewegen
            if dirn[1] >= 0:  # links bewwegen
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  # links bewegen
            if dirn[1] >= 0:  # nach unten bewegen
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1


def hit(self):
        """
        Return ob Gegner schaden nimmt oder Gestorben ist
        :return: Bool
        """
        self.health -=10
        if self.health <= 0:
            return False