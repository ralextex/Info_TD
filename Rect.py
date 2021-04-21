import pygame 

class Rect():
    # Definiert ein abstrakten Rechteck mit oben linker Ecke bis unten rechter Ecke
    def __init__ (self,x_ol,y_ol,x_ur,y_ur):
        """
        :param: X-Koordinate oben links, Y-Koordinate oben links, X-Koordinate unten rechts, Y-Koordinate unten rechts       
        """
        self.x_ol = x_ol
        self.y_ol = y_ol
        self.x_ur = x_ur
        self.y_ur = y_ur

    def inside(self,x,y):
        """
        Uberprueft ob xy innerhalb des Rechtecks  
        :return: bool
        """
        if(self.x_ol <= x <= self.x_ur and self.y_ol <= y <= self.y_ur):
             return True
        else:
            return False

    def display(self,screen):
        """
        Anzeige des Rechtecks (Debugging Purpose)
        :return: None
        """
        pygame.draw.rect(screen,(255,0,0),(self.x_ol, self.y_ol, self.x_ur-self.x_ol, self.y_ur-self.y_ol))
            