from Tower import *

class Tower_controller():
    def __init__ (self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y 
        self.tower = Tower(500, 500)
    
    def display_tower(self):
        self.tower.draw(self.screen)
        self.tower.draw_radius(self.screen)
        self.tower.draw_placement(self.screen)

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True